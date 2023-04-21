import tkinter

window = tkinter.Tk()
window.title("Hello World")
window.minsize(600, 500)


my_label = tkinter.Label(text="Hello World!", font=("vardana", 23, "bold"))
my_label.pack()
tkinter.mainloop()