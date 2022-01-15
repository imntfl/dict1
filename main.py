from tkinter import *
from tkinter import messagebox
 
def write_txt(data):
    with open('db.txt','a') as file:
        file.write(data + '\n')

def click():
    text = entry.get()
    write_txt(text)

root = Tk()
root.title("Словарь")
root.geometry("777x333")
 
message = StringVar()
 
entry = Entry(textvariable=message)
entry.place(relx=.5, rely=.2, anchor="c")
 
button = Button(text="Сохранить", command=click)
button.place(relx=.5, rely=.5, anchor="c")
 
exit = Button(root, text='Выход', command=root.destroy)
exit.place(relx=.5, rely=.8, anchor="c")


root.mainloop()

# Create file "db.txt" in directory when is our main.py




