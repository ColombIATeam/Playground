from openai import AzureOpenAI
from sqlalchemy import Engine
from api.workflows.test_questions.test_gpt import GptTest
from api.workflows.test_questions.test_request import TestRequest
from api.workflows.test_questions.test_response import GenerarTestsResponse

class TestWorkflow:
    _database_engine: Engine
    _gpt_test: GptTest
    
    def __init__(self,
        database_engine: Engine,
        azure_openai_client: AzureOpenAI
    ) -> None:
        self._database_engine = database_engine
        self._gpt_test = GptTest(client=azure_openai_client)

    def execute(self, request: TestRequest) -> GenerarTestsResponse:
        preguntas = self._gpt_test.get_text_test(request.text,request.prompt,msg=[])
        
        output = GenerarTestsResponse(test=preguntas['test'])
        return output