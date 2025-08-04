import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")

def get_ai_feedback(prompt: str) -> str:
    try:
        chat = model.start_chat()
        response = chat.send_message(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating content: {e}"
