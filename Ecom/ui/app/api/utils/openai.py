from openai import OpenAI
from app.api.utils.settings import OPENAI_API_KEY
from app.api.utils.services import create_order, update_order, cancel_order
client = OpenAI(api_key=OPENAI_API_KEY)
from fastapi import FastAPI, Cookie

# filepath = "./StyleHub.pdf"
# file_object = client.files.create(filepath=open(filepath, "rb"), purpose="assistants")

# assistant = client.beta.assistants.create(
#     name="StyleHub",
#     file=file_object.id,
#     model="gpt-3.5-turbo",
#     instructions="",
#     tools={""}
# )

def generate_message(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content