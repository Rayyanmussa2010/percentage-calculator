# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 15:39:28 2022

@author: DELL
"""

from tkinter import*
from tkinter import ttk
root=Tk()
root.geometry("900x900")
root.title("Percentage Calculation")

grade3=Label(root)
grade5=Label(root)
grade10=Label(root)

class grade_3():
    def __init__(self, science, maths):
        self.science=science
        self.maths=maths
    def percentage(self):
        total_marks=self.science+self.maths
        total_marks1=total_marks*100
        total_marks2=total_marks1/200
        grade3["text"]=total_marks2

object_grade3=grade_3(50, 40)
btn1=Button(root, text="Grade 3", command=object_grade3.percentage)
btn1.place(relx=0.5, rely=0.1, anchor=CENTER)
grade3.place(relx=0.5, rely=0.2, anchor=CENTER)

class grade_5():
    def __init__(self, science, maths):
        self.science=science
        self.maths=maths
    def percentage(self):
        total_marks=self.science+self.maths
        total_marks1=total_marks*100
        total_marks2=total_marks1/200
        grade5["text"]=total_marks2

object_grade5=grade_5(50, 70)
btn1=Button(root, text="Grade 5", command=object_grade5.percentage)
btn1.place(relx=0.5, rely=0.3, anchor=CENTER)
grade5.place(relx=0.5, rely=0.4, anchor=CENTER)

class grade_10():
    def __init__(self, science, maths):
        self.science=science
        self.maths=maths
    def percentage(self):
        total_marks=self.science+self.maths
        total_marks1=total_marks*100
        total_marks2=total_marks1/200
        grade10["text"]=total_marks2

object_grade10=grade_10(50, 75)
btn1=Button(root, text="Grade 10", command=object_grade10.percentage)
btn1.place(relx=0.5, rely=0.5, anchor=CENTER)
grade10.place(relx=0.5, rely=0.6, anchor=CENTER)



















root.mainloop()