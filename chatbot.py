import json
import openai
from config import GEMINI_API_KEY
import google.generativeai as genai

# Khởi tạo Google Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def load_faq():
    """Load dữ liệu FAQ từ JSON"""
    with open("FAQ.json", "r", encoding="utf-8") as file:
        return json.load(file)

FAQ_DATA = load_faq()

def find_answer(user_question):
    """Tìm câu trả lời từ FAQ trước, nếu không có thì dùng Google Gemini"""
    return get_gemini_response(user_question)

def get_gemini_response(question):
    try:
        model = genai.GenerativeModel(model_name="gemini-pro-1.0")
        response = model.generate_content(question)
        return response.text  # Trả về nội dung phản hồi từ Gemini
    except Exception as e:
        return f"Lỗi khi gọi Gemini: {str(e)}"
