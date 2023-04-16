import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_KEY')

def ai_response(prompt):
    
    text=f'''{prompt}'''
    d={'role':'user',"content":text}
    responses=[]
    op=openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[d])
    for i in op['choices']:
    # print(i.keys(),'a')
      if i['finish_reason']=='stop':
        responses.append(i['message']['content'])
        output = responses[0]
    # print(output)
    return output