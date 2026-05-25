import os
from dotenv import load_dotenv

load_dotenv()
token_telegram = os.getenv("TOKEN_TG")
token_openai_key = os.getenv("TOKEN_OPENAI")



if __name__ == '__main__':
    print(token_telegram)


