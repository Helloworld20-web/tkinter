from tkinter import *

window = Tk()

window.title("I calculate")
window.geometry("800x600")

def calculate_OR_uhhh():
    try:
        num1 = int(entry.get()) 
        num2 = int(entry2.get())

        production = num1 * num2

        equaled.config(text=f"The Product: {production}")


    except:
        print("Oh noes :( number problem")

label1 = Label(text="Enter First Number", bg="black", fg="white")
entry = Entry()

label2 = Label(text="Enter Second Number", bg="white", fg="black")
entry2 = Entry()

calculated = Button(text="Calculate", bg="blue", fg="white", command=calculate_OR_uhhh)

equaled = Label(bg="white", fg="black")

label1.pack(pady=5)
entry.pack(pady=5)

label2.pack(pady=5)
entry2.pack(pady=5)

calculated.pack(pady=10)

equaled.pack(pady=5)

window.mainloop()
