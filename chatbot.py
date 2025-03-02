import json
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY
client = openai()
def load_faq():
    """Load dữ liệu FAQ từ JSON"""
    with open("FAQ.json", "r", encoding="utf-8") as file:
        return json.load(file)

FAQ_DATA = load_faq()

def find_answer(user_question):
    """Tìm câu trả lời từ FAQ trước, nếu không có thì dùng OpenAI"""
    return get_openai_response(user_question)

def get_openai_response(question):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": question}],
        response_format={
        "type": "text"
    },
    temperature=1,
    max_completion_tokens=2048,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response["choices"][0]["message"]["content"]