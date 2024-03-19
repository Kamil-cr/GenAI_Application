from openai.types.beta import Assistant
from openai import OpenAI

client: OpenAI = OpenAI()

def create_assistant():
    assistant: Assistant = client.beta.assistants.create(
    name="Travel AI Assistant",
    model="gpt-3.5-turbo",
    instructions="You are a helpful AI Assistant that can write and execute code, and has access to a digital map to display information.",
    )
    return assistant