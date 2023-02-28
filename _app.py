import openai
import os
from dotenv import load_dotenv

load_dotenv('.env')

openai.api_key = os.environ.get("OPENAI_API_KEY")

def ask_chat_gpt(prompt):
    response = openai.Completion.create(
      engine="davinci",
      prompt=prompt,
      max_tokens=1024,
      n=1,
      stream=false,
      stop=None,
      temperature=0
    )

    answer = response.choices[0].text.strip()
    return answer

question = "Napisz w języku angielskim krótki list o następującej treści: Niestety nie mogę przybyć na dzisiejsze spotkanie z powodów zdrowotnych."
answer = ask_chat_gpt(question)
print(answer)
