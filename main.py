from tkinter import *
import random, string, pyperclip

root = Tk()
root.title("Simple text generator")
root['bg'] = 'black'


def string_generator():
    my_string = ''
    symbols = entry.get()
    val = var.get()
    if val == 1:
        i = 0
        while i != int(symbols):
            my_string += random.choice(string.digits)
            i += 1
        pyperclip.copy(my_string)
        text.delete('1.0', END)
        text.insert(1.0, my_string)
    elif val == 2:
        i = 0
        while i != int(symbols):
            my_string += random.choice(string.ascii_letters)
            i += 1
        pyperclip.copy(my_string)
        text.delete('1.0', END)
        text.insert(1.0, my_string)
    else:
        i = 0
        my_string = ''
        while i != int(symbols):
            my_string += random.choice(random.choice(string.ascii_letters) + random.choice(string.digits))
            i += 1
        pyperclip.copy(my_string)
        text.delete('1.0', END)
        text.insert(1.0, my_string)


label = Label(text="Введите кол-во символов:", fg="white", bg="black")
entry = Entry()
btn = Button(root, text="Generate", bg="black", fg="black", highlightbackground='black', command=string_generator)
var = IntVar()
rbutton1 = Radiobutton(root, text='Integer values only', variable=var, value=1, bg="black", fg="black",
                       highlightbackground='black')
rbutton2 = Radiobutton(root, text='String values only', variable=var, value=2, bg="black", fg="black",
                       highlightbackground='black')
rbutton3 = Radiobutton(root, text='Integer and String Values', variable=var, value=3, bg="black", fg="black",
                       highlightbackground='black')
text = Text(root, height=10, width=60, font='Arial 14')

label.pack()
entry.pack()
rbutton1.pack()
rbutton2.pack()
rbutton3.pack()
btn.pack()
text.pack()
root.mainloop()