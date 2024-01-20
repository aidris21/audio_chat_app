from openai import OpenAI
import os
from dotenv import load_dotenv

def get_open_ai_token():
    load_dotenv()
    return os.environ.get("OPENAI_API_KEY")

def get_gpt_response_from_prompt(prompt: str) -> str:
    """
    Submit a single prompt to ChatGPT 3.5 and retrieve the response.

    Note: You must provide an API Key for OpenAI in a `.env` file in this directory:
    ```text
    OPENAI_API_KEY={YOUR-API-TOKEN}
    ```
    """
    client = OpenAI(api_key=get_open_ai_token())
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    if len(completion.choices) == 0:
        raise ValueError('No GPT response generated')
    
    return completion.choices[0].message.content