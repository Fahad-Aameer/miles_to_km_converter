from tkinter import *

window = Tk()
window.title("Miles to Kms converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)


def button_click():
    my_result = round(float(miles_entry.get()) * 1.609, 1)
    result.config(text=f"{my_result}")


equal_to = Label(text="is equal to", font=("Ariel", 18, "normal"))
equal_to.grid(column=0, row=1)
equal_to.config(padx=10, pady=10)

result = Label(text="0", font=("Ariel", 18, "normal"))
result.grid(column=1, row=1)
result.config(padx=10, pady=10)

miles = Label(text="Miles", font=("Ariel", 18, "normal"))
miles.grid(column=2, row=0)
miles.config(padx=10, pady=10)

km = Label(text="Km", font=("Ariel", 18, "normal"))
km.grid(column=2, row=1)
km.config(padx=10, pady=10)

miles_entry = Entry(width=5)
miles_entry.grid(column=1, row=0)
miles.config(padx=10, pady=10)

button = Button(text="Calculate", command=button_click)
button.grid(column=1, row=2)
button.config(padx=10, pady=10)

window.mainloop()
