from pydantic import BaseModel
from openai.types.beta.threads.run import RequiredAction, LastError
from typing import Optional

class ThreadMessage(BaseModel):
    content: str
    role: str
    hidden: bool 
    id: str
    created_at: int

class Thread(BaseModel):
    messages: list[ThreadMessage]

class CreateMessage(BaseModel):
    content: str

class RunStatus(BaseModel):
    run_id: str
    thread_id: str
    status: str
    required_action: Optional[RequiredAction]
    last_error: Optional[LastError]