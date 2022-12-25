from tkinter import*
import tkinter as tk
from sympy import symbols,Eq,solve

root=Tk()


root.geometry("300x300")

root.title("Sally's Calc")

def press(item):
    global expression
    expression=expression+str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression=""
    input_text.set("")

def equalpress():
        global expression
        total = str(eval(expression))
        input_text.set(total)
        expression = ""

expression="" 
input_text=StringVar()
 
input_field = Entry(font = ('arial', 18, 'bold'), textvariable = input_text, width = 50, bg = "#fff", bd = 0, justify = RIGHT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10)

buttonframe=tk.Frame(root)
buttonframe.columnconfigure(0,weight=1)
buttonframe.columnconfigure(1,weight=1)
buttonframe.columnconfigure(2,weight=1)
buttonframe.columnconfigure(3,weight=1)

btn1=tk.Button(buttonframe,text="1",font=("Arial",18),height=1,width=7,command=lambda:press(1))
btn1.grid(row=0, column=0)

btn2=tk.Button(buttonframe,text="2",font=("Arial",18),height=1,width=7,command=lambda:press(2))
btn2.grid(row=0,column=1)

btn3=tk.Button(buttonframe,text="3",font=("Arial",18),height=1,width=7,command=lambda: press(3))
btn3.grid(row=0,column=2)

btn4=tk.Button(buttonframe,text="4",font=("Arial",18),height=1,width=7,command=lambda:press(4))
btn4.grid(row=1,column=0)

btn5=tk.Button(buttonframe,text="5",font=("Arial",18),height=1,width=7,command=lambda:press(5))
btn5.grid(row=1,column=1)

btn6=tk.Button(buttonframe,text="6",font=("Arial",18),height=1,width=7,command=lambda:press(6))
btn6.grid(row=1,column=2)

btn7=tk.Button(buttonframe,text="7",font=("Arial",18),height=1,width=7,command=lambda:press(7))
btn7.grid(row=2,column=0)

btn8=tk.Button(buttonframe,text="8",font=("Arial",18),height=1,width=7,command=lambda:press(8))
btn8.grid(row=2,column=1)

btn9=tk.Button(buttonframe,text="9",font=("Arial",18),height=1,width=7,command=lambda:press(9))
btn9.grid(row=2,column=2)

btn10=tk.Button(buttonframe,text="+",font=("Arial",18),height=1,width=7,command=lambda:press('+'))
btn10.grid(row=0,column=3)

btn11=tk.Button(buttonframe,text="*",font=("Arial",18),height=1,width=7,command=lambda:press('*'))
btn11.grid(row=1,column=3)

btn12=tk.Button(buttonframe,text="/",font=("Arial",18),height=1,width=7,command=lambda:press('/'))
btn12.grid(row=2,column=3)

btn13=tk.Button(buttonframe,text="-",font=("Arial",18),height=1,width=7,command=lambda:press('-'))
btn13.grid(row=3,column=3)

btn14=tk.Button(buttonframe,text="0",font=("Arial",18),height=1,width=7,command=lambda:press(0))
btn14.grid(row=3,column=0)

btn15=tk.Button(buttonframe,text="clear",font=("Arial",18),height=1,width=7,command=lambda:btn_clear())
btn15.grid(row=3,column=1)

btn16=tk.Button(buttonframe,text="=",font=("Arial",18),height=1,width=7,command=lambda:equalpress())
btn16.grid(row=4,column=0)

btn17=tk.Button(buttonframe,text=".",font=("Arial",18),height=1,width=7,command=lambda:press('.'))
btn17.grid(row=3,column=2)


buttonframe.pack(fill="x")


root.mainloop()