# Personal Ai Chatbot

A simple AI-powered chatbot built with **Flask** and **Ollama**, running entirely on your local machine. No API costs. No data sent to the cloud.

---

##  Prerequisites

| Requirement | Version |
|---|---|
| Python | 3.8+ |
| Ollama | Latest |
| pip | Latest |

---

## 📁 Project Structure

```
flask-chatbot/
├── app.py
├── requirements.txt
├── README.md
└── templates/
    └── index.html
```

---

##  Installation

### 1. Install Ollama

Download and install from [https://ollama.ai](https://ollama.ai)

### 2. Pull a model

Open a terminal and run:

```bash
ollama pull tinyllama
```

Verify it downloaded:

```bash
ollama list
```

### 3. Install Python dependencies

```bash
pip install flask requests
```

---

## 🚀 Running the App

> **Note:** Ollama starts automatically on Windows. You do **not** need to run `ollama serve` manually.

Start the Flask server:

```bash
python app.py
```

Then open your browser and go to:

```
http://localhost:5000
```

---

## 💬 How It Works

```
Browser → POST /chat → Flask → Ollama API (localhost:11434) → Flask → Browser
```

1. User types a message and clicks **Send**
2. Flask receives the message at `/chat`
3. Flask forwards it to Ollama's local API
4. Ollama runs the model and returns a response
5. The response is displayed in the chat window

---

## 🔧 Configuration

In `app.py`, you can change these two settings:

```python
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "tinyllama"   # change to any model from: ollama list
```

### Available Models

| Model | Size | Command |
|---|---|---|
| TinyLlama | 637 MB | `ollama pull tinyllama` |
| Llama 3.2 1B | 1.3 GB | `ollama pull llama3.2:1b` |
| Mistral | 4 GB | `ollama pull mistral` |
| Gemma 3 | 3 GB | `ollama pull gemma3` |

---

## 🛠️ API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Loads the chat web interface |
| POST | `/chat` | Sends a message and returns AI reply |

### Example API call (without browser)

```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello!"}'
```

Response:

```json
{
  "reply": "Hello! How can I help you today?"
}
```

---

## ❗ Troubleshooting

| Problem | Fix |
|---|---|
| `Connection refused` on port 11434 | Ollama is not running. Check system tray or run `ollama serve` |
| `bind: Only one usage of each socket address` | Ollama is already running — skip `ollama serve` |
| `invalid model name` | Run `ollama list` to see exact model names, update `MODEL_NAME` in `app.py` |
| `no matches` in `ollama list` | Pull a model first: `ollama pull tinyllama` |
| Slow responses | Normal for local models. Larger models = slower responses |

---

## 🧰 Tech Stack

- **[Flask](https://flask.palletsprojects.com/)** — Python web framework
- **[Ollama](https://ollama.ai/)** — Local LLM runner
- **[TinyLlama](https://ollama.com/library/tinyllama)** — Lightweight local AI model
- **Vanilla JS** — Frontend chat interface

---

## 📄 License

This project is for educational purposes. Free to use and modify.
