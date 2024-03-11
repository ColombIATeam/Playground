from api.workflows.question_incorrect.question_incorrect_gpt import GptQuestionIncorrect
from api.workflows.question_incorrect.question_incorrect_request import QuestionIncorrectRequest
from api.workflows.question_incorrect.question_incorrect_response import QuestionIncorrectResponse
from openai import AzureOpenAI
from sqlalchemy import Engine
import logging


class QuestionIncorrectWorkflow:
    _database_engine: Engine
    _gpt_question_incorrect: GptQuestionIncorrect
    
    def __init__(
        self,
        database_engine: Engine,
        azure_openai_client: AzureOpenAI
    ) -> None:
        self._database_engine = database_engine
        self._gpt_question_incorrect = GptQuestionIncorrect(client=azure_openai_client)


    def execute(self, request:QuestionIncorrectRequest) -> QuestionIncorrectResponse:
        logging.info(f"Executing GenCorrectWorkflow request={request}")
        incorrect_answers, prompt, prompt_improving = self._gpt_question_incorrect.get_prompt_incorrect(question=request.question,
                                                                                                     question_correct=request.correct_answer,
                                                                                                     prompt_improving=request.prompt,
                                                                                                     msg=[])
        logging.info(f"GenIncorrectWorkflow output incorrect_answers={incorrect_answers}, prompt_improving={prompt_improving}")
        return QuestionIncorrectResponse(incorrect_answers=f'{incorrect_answers}', prompt=prompt, prompt_improving=f'{prompt_improving}')