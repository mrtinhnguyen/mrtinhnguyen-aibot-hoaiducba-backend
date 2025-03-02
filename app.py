from flask import Flask, request, jsonify
from chatbot import find_answer

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Chatbot API is running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    
    response_text = find_answer(user_message)
    return jsonify({"reply": response_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)