Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> 
>>> def btn_click():
...     print("Button Clicked")
... 
...     
>>> window = Tk()
>>> btn = Button(window, text="Click me!", command=btn_click)
>>> 
>>> btn.pack()
>>> 
>>> window.mainloop()
