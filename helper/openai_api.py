import os

import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')


def text_complition(query: str) -> dict:
    prompt = '''
    You are friendly AI Assistant at Health Care Center , if user's question is not related to health care bring the user to topic.
    '''
    # print(prompt)
    try:
        response = openai.Completion.create(
            model='text-davinci-003',
            prompt=f'System:{prompt}\nHuman: {query}\nAI: ',
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=['Human:', 'AI:']
        )
        return {
            'status': 1,
            'response': response['choices'][0]['text']
        }
    except:
        return {
            'status': 0,
            'response': ''
        }
