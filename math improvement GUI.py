from tkinter import *
import random
import time
win = Tk()
win.title("Math Improvement")
win.configure(background="black")
win.geometry("500x500")
c=0

def clicked_add():
    global c,ans
    if(c==0):
        button_add_start["state"]=DISABLED
        a = random.randint(3, 99)
        b = random.randint(3, 99)
        ans = a + b
        s = str(a) + "+" + str(b)
        l_add_question.config(text=s)
    l_add_time.config(text=str(c))
    c=c+1
    if(c!=8):
        l_add_time.after(1000, clicked_add)
    else:
        c=0
        l_add_question.config(text=str(ans))
        button_add_start["state"] = NORMAL

def clicked_Sub():
    global c,ans
    if(c==0):
        button_sub_start["state"]=DISABLED
        a = random.randint(3, 999)
        b = random.randint(3, 999)
        ans = a - b
        s = str(a) + "-" + str(b)
        l_sub_question.config(text=s)
    l_sub_time.config(text=str(c))
    c=c+1
    if(c!=8):
        l_sub_time.after(1000, clicked_Sub)
    else:
        c=0
        l_sub_question.config(text=str(ans))
        button_sub_start["state"] = NORMAL

def clicked_mul():
    global c,ans
    if(c==0):
        button_mul_start["state"]=DISABLED
        a = random.randint(3, 12)
        b = random.randint(3, 12)
        ans = a * b
        s = str(a) + " X " + str(b)
        l_mul_question.config(text=s)
    l_mul_time.config(text=str(c))
    c=c+1
    if(c!=6):
        l_mul_time.after(1000, clicked_mul)
    else:
        c=0
        l_mul_question.config(text=str(ans))
        button_mul_start["state"] = NORMAL

def clicked_div():
    global c,ans
    if(c==0):
        button_div_start["state"]=DISABLED
        a = random.randint(3, 12)
        b = random.randint(3, 12)
        if not(a>=b):
            s=a
            a=b
            b=s

        ans = round(a / b)
        s = str(a) + " / " + str(b)
        l_div_question.config(text=s)
    l_div_time.config(text=str(c))
    c=c+1
    if(c!=6):
        l_div_time.after(1000, clicked_div)
    else:
        c=0
        l_div_question.config(text=str(ans))
        button_div_start["state"] = NORMAL

#main page functions:
def btnAdd():
    global l_add_time
    global button_add_start, l_add_question
    winAdd=Tk()
    winAdd.title("Math Improvement-Addition")
    winAdd.configure(background="white")
    winAdd.geometry("400x400")
    button_add_start=Button(winAdd,text="click me to start",bg="white" , command=clicked_add)
    button_add_start.pack()
    l_add_time=Label(winAdd,bg="grey",fg="White",text="0" , font="Helvetica 48")
    l_add_time.pack()
    l_add_question=Label(winAdd,bg="black",fg="green",text="QUESTION",font="Helvetica 48")
    l_add_question.pack()
    winAdd.mainloop()
def btnSub():
    global l_sub_time
    global button_sub_start, l_sub_question
    winSub = Tk()
    winSub.title("Math Improvement-Subtraction")
    winSub.configure(background="white")
    winSub.geometry("400x400")
    button_sub_start = Button(winSub, text="click me to start", bg="white", command=clicked_Sub)
    button_sub_start.pack()
    l_sub_time = Label(winSub, bg="grey", fg="White", text="0", font="Helvetica 48")
    l_sub_time.pack()
    l_sub_question = Label(winSub, bg="black", fg="green", text="QUESTION", font="Helvetica 48")
    l_sub_question.pack()
    winSub.mainloop()
def btnmul():
    global l_mul_time
    global button_mul_start, l_mul_question
    winmul = Tk()
    winmul.title("Math Improvement-Multiplication")
    winmul.configure(background="white")
    winmul.geometry("400x400")
    button_mul_start = Button(winmul, text="click me to start", bg="white", command=clicked_mul)
    button_mul_start.pack()
    l_mul_time = Label(winmul, bg="grey", fg="White", text="0", font="Helvetica 48")
    l_mul_time.pack()
    l_mul_question = Label(winmul, bg="black", fg="green", text="QUESTION", font="Helvetica 48")
    l_mul_question.pack()
    winmul.mainloop()
def btndiv():
    global l_div_time
    global button_div_start, l_div_question
    windiv = Tk()
    windiv.title("Math Improvement-Division")
    windiv.configure(background="white")
    windiv.geometry("400x400")

    button_div_start = Button(windiv, text="click me to start", bg="white", command=clicked_div)
    button_div_start.pack()
    l_div_time = Label(windiv, bg="grey", fg="White", text="0", font="Helvetica 48")
    l_div_time.pack()
    l_div_question = Label(windiv, bg="black", fg="green", text="QUESTION", font="Helvetica 48")
    l_div_question.pack()
    windiv.mainloop()


Label(win,bg="black",fg="white",text="Math",height="3",font="Sans 20 bold").pack()
l_select=Label(win,bg="black",fg="white",text="what do you wish to practice?",font="sans 10" ).place(x=10,y=100)
buttonAdd= Button(win, text="Addition",command=btnAdd).place(x=30,y=130)
buttonSub= Button(win, text="Subtraction",command=btnSub).place(x=30,y=160)
buttonMul= Button(win, text="Multiplication",command=btnmul).place(x=30,y=190)
buttonDiv= Button(win, text="Division",command=btndiv).place(x=30,y=220)




win.mainloop()