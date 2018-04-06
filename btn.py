from tkinter import *
from tkinter import messagebox
from time import clock

cnt = 0

def click():
    global cnt
    if (clock() <= 3.0):
        cnt += 1
        print(cnt)

    else:
        cnt += 1
        print(cnt)
        btn1["text"] = "終わり"
        print(clock())
        dialog(cnt,clock())
        sysexit()

def dialog(cnt,time):
    cnts = cnt/time
    print(time)
    messagebox.showinfo(
        "clicks",
        "秒間%.2fクリックです。"%cnts
)

def sysexit():
    btn1["command"] = exit

root = Tk()
root.title("fpsclicker")
root.geometry("100x150")

btn1 = Button(
    root,
    activeforeground="red",
    text="click here",
    command=click
)

btn1.place(
    relx = 0.2,
    rely = 0.2,
    relheight = 0.6,
    relwidth = 0.6
)

root.mainloop()


