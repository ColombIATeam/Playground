from api.common.services.openai_api import OpenAIAPI
from openai import AzureOpenAI
import json, logging, os


class GptQuestionCorrect:
    _gpt_utils: OpenAIAPI
    _openai_client: AzureOpenAI

    def __init__(self, client: AzureOpenAI) -> None:
        self._gpt_utils = OpenAIAPI()
        self._openai_client = client

    def get_prompt_correct(self, question:str, prompt_improving:str, msg):
        logging.info(
            f"get_answer_correct_gpt input question={question}, prompt={prompt_improving}"
        )
        prompt, params, _ = self._gpt_utils.load_sys_prompt(
            os.path.join(
                os.sep.join(__file__.split(os.sep)[:-1]),
                "prompts",
                "question_correct.json",
            )
        )
        if prompt_improving=="":
            prompt_improving = 'Analyze the question and give me the correct answer, adding complexity and value to the subject.'
        entrada = str({'Question':f'{question}', 'Prompt Improving':f'{prompt_improving}'})
        last_msg: list[dict[str, str]] = []
        for i in msg[-4:]:
            last_msg.append({"role": "user", "content": i["Alumno"]})
            last_msg.append({"role": "assistant", "content": i["Profesor"]})
        output = self._gpt_utils.call_api(
            system_msg=prompt.replace('{}', prompt_improving),
            user_msg=entrada,
            params=params,
            examples=last_msg,
            is_json=True,
            client=self._openai_client,
        )
        json_answer = json.loads(str(output))
        logging.info(f"get_answer_correct_gpt output correct_answer={json_answer['Correct Answer']}, prompt={json_answer['Prompt Improving']}")
        return json_answer['Correct Answer'], prompt_improving, json_answer['Prompt Improving']