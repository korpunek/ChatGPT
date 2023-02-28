import tkinter as tk
from tkinter import ttk
import openai
import os
import ttkbootstrap as ttkbs
from dotenv import load_dotenv

load_dotenv('.env')

openai.api_key = os.environ.get("OPENAI_API_KEY")

def ask_chat_gpt(prompt):
    response = openai.Completion.create(
      engine="davinci",
      prompt=prompt,
      max_tokens=1024,
      n=1,
      stop=None,
      stream=false,
      temperature=0
    )

    answer = response.choices[0].text.strip()
    return answer

def ask_question():
    question = question_entry.get()
    answer = ask_chat_gpt(question)
    answer_label.config(text=answer)

root = tk.Tk()
root.title("ChatGPT")
root.geometry("1000x1000")

style = ttkbs.Style(theme="flatly")
frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True)

question_entry = ttk.Entry(frame)
question_entry.pack(pady=10)

ask_button = ttk.Button(frame, text="Ask", command=ask_question)
ask_button.pack(pady=10)

answer_label = ttk.Label(frame, text="")
answer_label.pack(pady=10)

root.mainloop()
