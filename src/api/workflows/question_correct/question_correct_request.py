from pydantic import BaseModel

class QuestionCorrectRequest(BaseModel):
    question: str
    prompt: str