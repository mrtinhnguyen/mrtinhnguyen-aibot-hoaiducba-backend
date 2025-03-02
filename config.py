import os
from dotenv import load_dotenv

load_dotenv()  # Load biến môi trường từ file .env

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")