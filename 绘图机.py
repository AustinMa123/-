from tkinter import *
from time import sleep

window = Tk()
window.title('遇见外星人！')
frame_window = Frame(window)
c = Canvas(window, height=300, width=400)
c.pack()
frame_window.pack()
body = c.create_oval(100, 150, 300, 250, fill='green')
eye = c.create_oval(170, 70, 230, 130, fill='white')
eyeball = c.create_oval(190, 90, 210, 110, fill='black')
mouth = c.create_oval(150, 220, 250, 340, fill='red')
neck = c.create_line(200, 150, 200, 130)
hat = c.create_polygon(180, 75, 220, 75, 200, 20, fill='blue')


def mouth_open():
    c.itemconfig(mouth, fill='black')


def mouth_close():
    c.itemconfig(mouth, fill='red')


def blink():
    c.itemconfig(eye, fill='green')
    c.itemconfig(eyeball, skate=HIDDEN)


def not_blink():
    c.itemconfig(eye, fill='white')
    c.itemconfig(eyeball, skate=NORMAL)


sleep(100)
