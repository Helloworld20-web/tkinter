from tkinter import *
from datetime import date

window = Tk()

window.title("This is a window")
window.geometry("900x800")

label = Label(text="Hello there", bg="black", fg="white", height=1, width=300)

name_label = Label(text="Type a username please", bg="orange", height=1, width=300)

the_entry = Entry()

id_label = Label(text="Enter a id number please", bg="black", fg="white", height=1, width=300)

the_entry_id = Entry()


def display():
    many_words.delete("1.0", "end")
    thy_name = the_entry.get()
    thy_id = the_entry_id.get()

    global speak
    speak = "Welcome to the Window you have chosen or have been chosen to use this Program \nCurrent Date is: "
    user_name = "\nWelcome" " "+thy_name+ ""
    id = "\nYour current id is:" " "+thy_id+ ""
    
    many_words.insert(END, speak)
    many_words.insert(END, date.today())
    many_words.insert(END, user_name)
    many_words.insert(END, id)

many_words = Text(height=4)

btn = Button(text="Please press me", command=display, height=3, bg="darkblue", fg="white")

label.pack()
name_label.pack()
the_entry.pack()
id_label.pack()
the_entry_id.pack()
many_words.pack()
btn.pack()

window.mainloop()