from flask import Flask, request, jsonify
from chatbot import find_answer
from flask_cors import CORS  # Import CORS
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
CORS(app, resources={r"/chat": {"origins": "*"}})  # Cho phép tất cả nguồn gốc truy cập API
@app.route("/", methods=["GET"])
def home():
    return "Chatbot API is running!"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        raw_data = request.data.decode("utf-8")  # Lấy dữ liệu thô
        app.logger.debug(f"📥 Dữ liệu gốc: {raw_data}")

        data = request.get_json(silent=True)
        app.logger.debug(f"Dữ liệu nhận được: {data} (Loại: {type(data)})")
        if not isinstance(data, dict):  # Nếu data không phải dictionary, trả về lỗi
                return jsonify({"error": "Dữ liệu không hợp lệ"}), 400;
        if "message" not in data:
                return jsonify({"error": "Thiếu message!"}), 400
        user_message = data.get("message", "")
        
        if not user_message:
            return jsonify({"reply": "Xin lỗi, tôi không hiểu câu hỏi của bạn."})
        response_text = find_answer(user_message)
        return jsonify({"reply": response_text})
    
    except Exception as e:
        app.logger.error(f"🔥 LỖI SERVER: {str(e)}", exc_info=True)
        return jsonify({"error": "Lỗi server"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)