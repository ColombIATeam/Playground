from api.workflows.question_correct.question_correct_request import QuestionCorrectRequest
from api.workflows.question_correct.question_correct_response import QuestionCorrectResponse
from api.workflows.question_incorrect.question_incorrect_request import QuestionIncorrectRequest
from api.workflows.question_incorrect.question_incorrect_response import QuestionIncorrectResponse
from api.common.dependency_container import DependencyContainer
from fastapi import APIRouter


router = APIRouter(prefix="/question", tags=["questions"])

@router.post("/question_correct")
def question_correct(request: QuestionCorrectRequest) -> QuestionCorrectResponse:
    return DependencyContainer.get_question_correct_workflow().execute(request)

@router.post("/question_incorrect")
def question_incorrect(request: QuestionIncorrectRequest) -> QuestionIncorrectResponse:
    return DependencyContainer.get_question_incorrect_workflow().execute(request)