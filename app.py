import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledText
from ttkbootstrap.dialogs import MessageDialog
from tkinter.filedialog import askopenfilename
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
import openai
import os
from dotenv import load_dotenv

load_dotenv('.env')

openai.api_key = os.environ.get("OPENAI_API_KEY")


app = ttk.Window(title="Klient ChatGPT v. 0.1", themename="superhero", iconphoto ='ai32.png', size=(1200, 800))
app.place_window_center()

colors = app.style.colors

img1 = ImageTk.PhotoImage(file="info_2_32.png")
img2 = ImageTk.PhotoImage(file="trash_1_32.png")


def ask_chat_gpt(prompt):
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "user", "content": prompt}]
    )
    answer = completion.choices[0].message.content
    return answer

def ask_question():
    question = question_entry.get()
    if len(question) > 0:
      answer = ask_chat_gpt(question)
      st1.insert(END, "\n * " + question.upper())
      st1.insert(END, answer)
      st1.insert(END, "\n---------------------------------------------------------------------------------------------------------------------------------\n")
    else:
      md = MessageDialog(message = 'Treść pytania jest pusta', title = 'Błąd', buttons=["OK:primary"])
      md.show()        
        
def clear_notes():
    st1.delete('1.0', END)
    question_entry.delete(0, END)

def about():
    md = MessageDialog(message = 'Klient ChatGPT 0.1\n\nUmożliwia zadawanie pytań do ChatGPT poprzez API\n\nAutor: Leszek Owczarek\nLicencja: MIT', title = 'Informacja', buttons=["OK:primary"])
    md.show()

container1 = ttk.Frame()
container1.pack(fill=X, expand=YES, pady=5)
question_entry = ttk.Entry(master=container1)
question_entry.pack(side=LEFT, pady=5, expand=YES, fill=BOTH)
ask_button = ttk.Button(master=container1, text="Pytanie", bootstyle=SUCCESS, command=ask_question)
ask_button.pack(side=LEFT,pady=5, padx=5)
clear_button = ttk.Button(master=container1, image=img2, command=clear_notes)
clear_button.pack(side=LEFT,pady=5, padx=5)
b5 = ttk.Button(master=container1, image=img1, command=about)
b5.pack(side=RIGHT, padx=5, pady=5)

# NOTES Z WYNIKIEM
st1 = ScrolledText(app, padding=5, height=25, autohide=True)
st1.pack(fill=BOTH, expand=YES)


if __name__ == "__main__":
    app.mainloop()