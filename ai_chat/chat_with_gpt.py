from openai import OpenAI
import os

def get_open_ai_token():
    return os.environ.get("OPENAI_API_KEY")

def get_gpt_response_from_prompt(prompt: str) -> str:
    client = OpenAI(api_key=get_open_ai_token())
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            prompt
        ]
    )

    if len(completion.choices) == 0:
        raise ValueError('No GPT response generated')
    
    return completion.choices[0].message