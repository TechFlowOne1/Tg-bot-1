from openai import AsyncOpenAI

# class ChatGptService:
#     def __init__(self, api_key: str):
#         self.client = AsyncOpenAI(api_key=api_key)
#
#     async def ask(self, user_text:str,role_text:str) -> str:
#         response = await self.clien.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {
#                     "role": "system",
#                     "content": role_text,
#                 },
#                 {
#                     "role": "user",
#                     "content": user_text,
#                 }
#             ],
#             max_tokens=700,
#             temperature=0.4,
#         )
#         answer = response.choices[0].message.content
#         return answer
#
