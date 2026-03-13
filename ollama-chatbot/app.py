from flask import Flask, request, jsonify, render_template, Response
import requests, json

app = Flask(__name__)
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3:mini"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    def generate():
        response = requests.post(OLLAMA_URL, json={
            "model": MODEL_NAME,
            "prompt": user_message,
            "stream": True        # ← streaming ON
        }, stream=True)

        for line in response.iter_lines():
            if line:
                chunk = json.loads(line)
                token = chunk.get("response", "")
                yield f"data: {json.dumps({'token': token})}\n\n"
                if chunk.get("done"):
                    break

    return Response(generate(), mimetype="text/event-stream")

if __name__ == "__main__":
    app.run(debug=True)