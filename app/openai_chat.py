from dotenv import load_dotenv
import os
import openai
from typing import Generator

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def ai_response(prompt):
    """This function is used to get the response from the AI"""
    text = f'''{prompt}'''
    responses = []
    op = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {'role': 'user', "content": text}
        ]
        )
    
    for i in op['choices']:
        if i['finish_reason'] == 'stop':
            responses.append(i['message']['content'])
            output = responses[0]
    return output


def streamed_response(prompt):
    """This function is used to stream the response from the AI"""
    text = f'''{prompt}'''

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {'role': 'user', "content": text}
        ],
        stream=True,
    )
    return response


def generate_response(prompt: str, stream: bool = False) -> str | Generator[str, None, None]:
    """This function is used to generate the response from the AI"""
    if stream:
        return streamed_response(prompt)
    else:
        return ai_response(prompt)
