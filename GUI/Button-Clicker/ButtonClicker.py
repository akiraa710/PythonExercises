from tkinter import *

def btn_click():
    print("Button Clicked")
    btn = Button(window, text="Click me!", command=btn_click)

window = Tk()
btn = Button(window, text="Click me!", command=btn_click)
btn.pack()
window.mainloop()
