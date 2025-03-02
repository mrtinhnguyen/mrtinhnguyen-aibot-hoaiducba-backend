import json
#import openai
from config import DEEPSEEK_API_KEY
#import google.generativeai as genai
import requests

API_KEY = DEEPSEEK_API_KEY
ENDPOINT = "https://api.deepseek.com/v1/chat/completions"


# Khởi tạo Google Gemini API
# genai.configure(api_key=GEMINI_API_KEY)

def load_faq():
    """Load dữ liệu FAQ từ JSON"""
    with open("FAQ.json", "r", encoding="utf-8") as file:
        return json.load(file)

FAQ_DATA = load_faq()

def find_answer(user_question):
    """Tìm câu trả lời từ FAQ trước, nếu không có thì dùng Google Gemini"""
    return get_deepseek_response(user_question)

def get_deepseek_response(user_message):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek-chat",  # Kiểm tra tên model chính xác từ Deepseek
        "messages": [{"role": "user", "content": user_message}],
        "temperature": 0.7,
        "max_tokens": 1024
    }
    
    response = requests.post(ENDPOINT, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error {response.status_code}: {response.text}"

# Test API
print(get_deepseek_response("Xin chào!"))