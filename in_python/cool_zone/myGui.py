from tkinter import *
# widgets = GUI  elemntes, texetboxes, labels, images
# windows = serves as a container to hold or contain these widgets
window = Tk()
window.geometry("420x420")
window.title("Kiraina first")

label = Label(window, text="Hello, User", font=("Arial", 16))
label.pack()

window.mainloop()