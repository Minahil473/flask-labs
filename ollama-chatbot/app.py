from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "tinyllama"  # ✅ matches your ollama list

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = requests.post(OLLAMA_URL, json={
            "model": MODEL_NAME,
            "prompt": user_message,
            "stream": False
        })
        result = response.json()
        return jsonify({"reply": result.get("response", "No response")})

    except requests.exceptions.ConnectionError:
        return jsonify({"error": "Ollama is not running!"}), 503

if __name__ == "__main__":
    app.run(debug=True)