import tkinter
import math

from tkinter import *
expr = ""

def press(key):
    global expr
    expr += str(key)
    display.set(expr)

def sqrt():
        global expr
        try:
            value = float(expr)
            result = str(math.sqrt(value))
            display.set(result)
            expr = result
        except:
            display.set("error")
            expr = ""

def equal():
    global expr
    try:
        result = str(eval(expr))
        display.set(result)
        expr = ""
    except:
        display.set("error")
        expr = ""

def clear():
    global expr
    expr = ""
    display.set("")

def apply_trig(func):
    global expr
    try:
        #get value
        value = float(expr)
        #trig
        new_expr = f"math.{func}({value})"
        display.set(new_expr)
        expr = new_expr

    except:
        display.set("error")
        expr = ""

def backspace():
    global expr
    expr = expr[:-1]
    display.set(expr)

if __name__ == "__main__":
    root = Tk()
    root.geometry("374x445")
    root.configure(bg="black")
    root.title("Calculator")


    display = StringVar()
    entry = Entry(root, textvariable=display)
    entry.grid(columnspan=10, ipadx=125)

        #Buttonset1
    button1 = Button(root, text='1', bg='black', fg='white', command=lambda: press(1), width=12, height=4)
    button1.grid(row=2, column=0)
    button2 = Button(root, text='2', bg='black', fg='white', command=lambda: press(2), width=12, height=4)
    button2.grid(row=2, column=1)
    button3 = Button(root, text='3', bg='black', fg='white', command=lambda: press(3), width=12, height=4)
    button3.grid(row=2, column=2)
    button4 = Button(root, text='4', bg='black', fg='white', command=lambda: press(4), width=12, height=4)
    button4.grid(row=3, column=0)
    button5 = Button(root, text='5', bg='black', fg='white', command=lambda: press(5), width=12, height=4)
    button5.grid(row=3, column=1)
    button6 = Button(root, text='6', bg='black', fg='white', command=lambda: press(6), width=12, height=4)
    button6.grid(row=3, column=2)
    button7 = Button(root, text='7', bg='black', fg='white', command=lambda: press(7), width=12, height=4)
    button7.grid(row=4, column=0)
    button8 = Button(root, text='8', bg='black', fg='white', command=lambda: press(8), width=12, height=4)
    button8.grid(row=4, column=1)
    button9 = Button(root, text='9', bg='black', fg='white', command=lambda: press(9), width=12, height=4)
    button9.grid(row=4, column=2)
    button0 = Button(root, text='0', bg='black', fg='white', command=lambda: press(0), width=12, height=4)
    button0.grid(row=5, column=0)
     #Button2
    plus = Button(root, text='+', bg='black', fg='white', command=lambda: press('+'), width=12, height=4)
    plus.grid(row=2, column=3)
    minus = Button(root, text='-', bg='black', fg='white', command=lambda: press('-'), width=12, height=4)
    minus.grid(row=3, column=3)
    mult = Button(root, text='*', bg='black', fg='white', command=lambda: press('*'), width=12, height=4)
    mult.grid(row=4, column=3)
    div = Button(root, text='/', bg='black', fg='white', command=lambda: press('/'), width=12, height=4)
    div.grid(row=5, column=3)

     #Buttonset3
    eq = Button(root, text='=', bg='black', fg='white', command=equal, width=12, height=4)
    eq.grid(row=5, column=2)
    clr = Button(root, text='C', bg='black', fg='white', command=clear, width=12, height=4)
    clr.grid(row=5, column=1)
    dot = Button(root, text='.', bg='black', fg='white', command=lambda: press('.'), width=12, height=4)
    dot.grid(row=6, column=0)
    percent = Button(root, text='%', bg='black', fg='white', command=lambda: press('/100'), width=12, height=4)
    percent.grid(row=7, column=0)
    back = Button(root, text='⌫', bg='black', fg='white', command=backspace, width=12, height=4)
    back.grid(row=7, column=2)
    sqrt_button = Button(root, text='√', bg='black', fg='white', command=sqrt, width=12, height=4)
    sqrt_button.grid(row=7, column=1)

    sin_button = Button(root, text='sin', bg='black', fg='white', command=lambda: apply_trig("sin"), width=12, height=4)
    sin_button.grid(row=6, column=1)
    cos_button = Button(root, text='cos', bg='black', fg='white', command=lambda: apply_trig("cos"), width=12, height=4)
    cos_button.grid(row=6, column=2)
    tan_button = Button(root, text='tan', bg='black', fg='white', command=lambda: apply_trig("tan"), width=12, height=4)
    tan_button.grid(row=6, column=3)


    root.mainloop()