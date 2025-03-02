import json
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY
def load_faq():
    """Load dữ liệu FAQ từ JSON"""
    with open("FAQ.json", "r", encoding="utf-8") as file:
        return json.load(file)

FAQ_DATA = load_faq()

def find_answer(user_question):
    """Tìm câu trả lời từ FAQ trước, nếu không có thì dùng OpenAI"""
    for entry in FAQ_DATA:
        if entry["cau_hoi"].lower() in user_question.lower():
            return entry["tra_loi"]

    return get_openai_response(user_question)

def get_openai_response(question):
    """Gọi OpenAI để tạo câu trả lời"""
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        store=True,
        messages=[{"role": "user", "content": question}]
    )
    return response["choices"][0]["message"]["content"]