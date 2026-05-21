import os
from dotenv import load_dotenv

load_dotenv()
token_telegram = os.getenv("TOKEN_TG")
token_openai_key = os.getenv("TOKEN_OPENAI")
# token_openai = "sk-proj-" + token_openai_key[:3:-1] if token_openai_key.startswith('gpt:') else token_openai_key



if __name__ == '__main__':
    print(token_openai)
    print(token_telegram)

