import tkinter as tk
import random


git_hab = "https://github.com/GreenSans2010/facts-and-github.git"

facts = [
   "Бананы радиоактивны и излучают, \n небольшое количество гамма-излучения.",
   "Человек может обойтись без пищи до 2 месяцев, \n а без воды — всего несколько дней.",
   "Голубые киты ежедневно потребляют \n около 4 тонн пищи.",
   "Пчёлы могут распознавать лица людей.",
   "Существует 6 000 видов бананов, \n а не только один."
]


def rd():
    te = facts[random.randint(0, 4)]
    Label.configure(text=f"{te}")

app = tk.Tk()

app.geometry("360x400")
frame = tk.Frame(app, width=340, height=300, bg="#A9A9A9")
Label = tk.Label(frame, bg="#A9A9A9")
Button = tk.Button(app, width=39, height=3, command=rd, text="Показать факт")

frame.place(x=10, y=10)
Label.place(x=10, y=10)
Button.place(x=10, y=320)

app.mainloop()
