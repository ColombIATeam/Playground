from pydantic import BaseModel

class QuestionIncorrectResponse(BaseModel):
    incorrect_answers: str
    prompt: str
    prompt_improving: str