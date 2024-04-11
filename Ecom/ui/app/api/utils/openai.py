from openai import OpenAI
from app.api.utils.settings import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_message(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content