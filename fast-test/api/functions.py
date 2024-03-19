from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

_:bool = load_dotenv(find_dotenv())

client: OpenAI = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def get_response(prompt: str) -> str:
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return completion.choices[0].message.content