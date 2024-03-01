from tkinter import *
'''import dakhal_sal3a
import ta7wil
import tchof_sal3a
import front'''

# create a window
window = Tk()
window.title("Cool Zone")
window.geometry("400x400")
window.config(bg="#2e4d9b")

# change the  icon in window to CoolZone icon
icon = PhotoImage(file='coolzone.PNG')
window.iconphoto(True, icon)

# create a label
label = Label(window,
              text="Welcome to Cool Zone",
              font=("Georgia", 26),
              bg="#2e4d9b",
              fg="#ffffff")
label.pack()

# create buttons
enterbutton = Button(window,
                     text="Enter a product",
                     font=("Arial", 20),
                     bg="#c6d2ee",
                     fg="#0f1831",
                     activebackground="#0f1831",
                     #highlightthickness=10,
                     highlightbackground="#c6d2ee",
                     activeforeground="#c6d2ee")
enterbutton.pack(pady=42)

seebutton = Button(window,
                   text="See products",
                   font=("Arial", 20),
                   bg="#c6d2ee",
                   fg="#0f1831",
                   activebackground="#0f1831",
                   highlightbackground="#c6d2ee",
                   activeforeground="#c6d2ee")
seebutton.pack()

billbutton = Button(window,
                    text="Collect a bill",
                    font=("Arial", 20),
                    bg="#c6d2ee",
                    fg="#0f1831",
                    activebackground="#0f1831",
                    highlightbackground="#c6d2ee",
                    activeforeground="#c6d2ee")
billbutton.pack(pady=42)

backbutton = Button(window, text="<--")
backbutton.place(x=10, y=365, anchor=NW)

window.mainloop()