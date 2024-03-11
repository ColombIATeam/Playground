from pydantic import BaseModel

class QuestionIncorrectRequest(BaseModel):
    question: str
    correct_answer: str
    prompt: str