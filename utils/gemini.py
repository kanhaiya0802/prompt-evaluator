import os

from dotenv import load_dotenv
from google import genai

from utils.helpers import load_prompt


load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def evaluate_prompt(user_prompt):
    evaluation_prompt = load_prompt()

    full_prompt = f"""
{evaluation_prompt}

User Prompt:

{user_prompt}
"""

    response = client.models.generate_content(
        model=os.getenv("MODEL_NAME"),
        contents=full_prompt
    )

    return response.text