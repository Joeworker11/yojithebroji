# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 17:01:27 2021

@author: József
"""

from tkinter import *


class Buildself:
    pass
"""
    def __init__(self):
        self.a.geometry("700x700")
        self.a.Label(text="Heti Beosztás",
                     fg="red",
                     font = "Helvetica 16 bold italic").pack
        
"""


def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)
    
def Save_it_as_PDF():
    pass


    

window = Tk()

label = Label(window,text="megbeszélés", bg="red",width=10,height=3)
label.place(x=0,y=0)

label2 = Label(window,text="edzés", bg="blue",width=10,height=3)
label2.place(x=100,y=100)

label3 = Label(window,text="japán óra", bg="gold",width=10,height=3)
label3.place(x=200,y=200)

label4 = Label(window,text="angol óra", bg="yellow",width=10,height=3)
label4.place(x=300,y=300)

label5 = Label(window,text="kertrendezés", bg="green",width=10,height=3)
label5.place(x=400,y=400)

label6 = Label(window,text="kikapcsolódás", bg="purple",width=10,height=3)
label6.place(x=500,y=500)

label7 = Label(window,text="önfejlesztés", bg="orange",width=10,height=3)
label7.place(x=600,y=600)

label8 = Label(window,text="programozás", bg="greenyellow",width=10,height=3)
label8.place(x=350,y=350)

label9 = Label(window,text="családi program", bg="silver",width=11,height=3)
label9.place(x=450,y=450)

label10 = Label(window,text="ügyintézés", bg="teal",width=10,height=3)
label10.place(x=550,y=550)

label11 = Label(window,text="vendég", bg="cyan",width=10,height=3)
label11.place(x=650,y=650)

label.bind("<Button-1>",drag_start)
label.bind("<B1-Motion>",drag_motion)

label2.bind("<Button-1>",drag_start)
label2.bind("<B1-Motion>",drag_motion)

label3.bind("<Button-1>",drag_start)
label3.bind("<B1-Motion>",drag_motion)

label4.bind("<Button-1>",drag_start)
label4.bind("<B1-Motion>",drag_motion)

label5.bind("<Button-1>",drag_start)
label5.bind("<B1-Motion>",drag_motion)

label6.bind("<Button-1>",drag_start)
label6.bind("<B1-Motion>",drag_motion)

label7.bind("<Button-1>",drag_start)
label7.bind("<B1-Motion>",drag_motion)

label8.bind("<Button-1>",drag_start)
label8.bind("<B1-Motion>",drag_motion)

label9.bind("<Button-1>",drag_start)
label9.bind("<B1-Motion>",drag_motion)

label10.bind("<Button-1>",drag_start)
label10.bind("<B1-Motion>",drag_motion)

label11.bind("<Button-1>",drag_start)
label11.bind("<B1-Motion>",drag_motion)

if __name__ == "__main__":
    Buildself()

window.mainloop()