from tkinter import *

class Student():
    def __init__(self, name):
        self.first_name = name


    def get_grade(self):
        return self.grade

    def set_grade(self, grade):
        self.grade = grade

def show_grade():
    grade_label.config(text=csc_2[0].get_grade())


csc_2 = []

csc_2.append(Student("Boaz"))
csc_2[0].set_grade("Achieved")

window = Tk()
window.geometry("300x300")

students_listbox = Listbox(window)
students_listbox.pack()

students_listbox.insert(0, "Boaz")
students_listbox.insert(0, "Rehaan")
students_listbox.insert(0, "Aaran")


grade_label = Label()
grade_label.pack()

show_grade_btn = Button(text="Show Grade", command=show_grade)
show_grade_btn.pack()

window.mainloop()
