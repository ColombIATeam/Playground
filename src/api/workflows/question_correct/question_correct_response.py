from pydantic import BaseModel

class QuestionCorrectResponse(BaseModel):
    correct_answer: str
    prompt: str
    prompt_improving: str