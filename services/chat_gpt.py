from openai import AsyncOpenAI
import config

client = AsyncOpenAI(api_key=config.token_openai_key)

user_history = {}

async def ask_gpt(user_id: int, user_message: str, temperature: float = 0.3) -> str:
    """
    Отправляем запрос в чат GPT и проверяем, есть ли история сообщений
    Если нет, создаём историю, что бы наш ботик помнил контекст
    Используем аргумент 'temperature' для регулировки строгости ответа
    """
    if user_id not in user_history:
        user_history[user_id] = []
        user_history[user_id].append({"role": "system", "content": "Ты полезный бот-помощник."})

    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=user_history[user_id],
        temperature=temperature,
    )

    answer = response.choices[0].message.content
    user_history[user_id].append({"role": "assistant", "content": answer})
    return answer
