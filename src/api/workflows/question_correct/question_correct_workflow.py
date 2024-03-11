from api.workflows.question_correct.question_correct_gpt import GptQuestionCorrect
from api.workflows.question_correct.question_correct_request import QuestionCorrectRequest
from api.workflows.question_correct.question_correct_response import QuestionCorrectResponse
from openai import AzureOpenAI
from sqlalchemy import Engine
import logging


class QuestionCorrectWorkflow:
    _database_engine: Engine
    _gpt_question_correct: GptQuestionCorrect
    
    def __init__(
        self,
        database_engine: Engine,
        azure_openai_client: AzureOpenAI
    ) -> None:
        self._database_engine = database_engine
        self._gpt_question_correct = GptQuestionCorrect(client=azure_openai_client)


    def execute(self, request:QuestionCorrectRequest) -> QuestionCorrectResponse:
        logging.info(f"Executing GenCorrectWorkflow request={request}")
        correct_answer, prompt, prompt_improving = self._gpt_question_correct.get_prompt_correct(question=request.question,
                                                                                                 prompt_improving=request.prompt,
                                                                                                 msg=[])
        logging.info(f"GenCorrectWorkflow output correct_answer={correct_answer}, prompt={prompt}")
        return QuestionCorrectResponse(correct_answer=correct_answer, prompt=prompt, prompt_improving=str(prompt_improving))