from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

messages = []

def chat_with_gemini(user_message):
    messages.append(f"User: {user_message}")

    prompt = "\n".join(messages)

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    reply = response.text

    messages.append(f"Jarvis: {reply}")

    return reply