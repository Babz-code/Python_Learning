import tkinter

window = tkinter.Tk()
window.title("Mile to Kilometers Converter")
window.minsize(500, 300)

def mile_to_km():
    cal = float(space.get()) * 1.609
    label_4.config(text=f"{cal}")

space = tkinter.Entry(width=10)
space.grid(column=2, row=1)

label = tkinter.Label(text="Miles")
label.grid(column=3, row=1)

label_2 = tkinter.Label(text="is equal to")
label_2.grid(column=1, row=2)

label_3 = tkinter.Label(text="Km")
label_3.grid(column=3, row=2)

label_4 = tkinter.Label(text="0")
label_4.grid(column=2, row=2)

button = tkinter.Button(text="Calculate", command = mile_to_km)
button.grid(column=2, row=3)






window.mainloop()