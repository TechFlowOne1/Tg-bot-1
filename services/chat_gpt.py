from openai import AsyncOpenAI
import config

client = AsyncOpenAI(api_key=config.token_openai)

async def ask_gpt(user_message: str, temperature: float = 0.3) -> str:
    """
    Отправляем запрос в чат GPT и возвращаем ответ
    Используем аргумент 'temperature' для регулировки строгости ответа
    """
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": user_message}
        ],
        temperature=temperature,
    )
    return response.choices[0].message.content