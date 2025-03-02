from flask import Flask, request, jsonify
from chatbot import find_answer
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app, resources={r"/chat": {"origins": "*"}})  # Cho phép tất cả nguồn gốc truy cập API
@app.route("/", methods=["GET"])
def home():
    return "Chatbot API is running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    
    if not user_message:
        return jsonify({"reply": "Xin lỗi, tôi không hiểu câu hỏi của bạn."})
    response_text = find_answer(user_message)
    return jsonify({"reply": response_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)