# -*- coding:utf-8 -*-
"""
@author:Ls
@file:main.py
@time:2018/7/30 16:14
"""

import tkinter as tk


def compute_conv():
    var_w = int(W.get())
    var_h = int(H.get())
    var_d = int(D.get())
    var_f = int(F.get())
    var_k = int(K.get())
    var_s = int(S.get())
    var_p = int(P.get())
    out_w = ((var_w - var_f + (2 * var_p)) / var_s) + 1
    out_h = ((var_h - var_f + (2 * var_p)) / var_s) + 1
    out_d = var_k
    if ((var_w - var_f + (2 * var_p)) % var_s) or ((var_h - var_f + (2 * var_p)) % var_s):
        var.set('bad parameter！')
    else:
        var.set('')
    w.delete(0,tk.END)
    h.delete(0,tk.END)
    d.delete(0,tk.END)

    w.insert('insert', int(out_w))
    h.insert('insert', int(out_h))
    d.insert('insert', int(out_d))

def compute_pool():
    var_w = int(W.get())
    var_h = int(H.get())
    var_d = int(D.get())
    var_f = int(F.get())
    var_k = int(K.get())
    var_s = int(S.get())
    var_p = int(P.get())
    out_w = ((var_w - var_f) / var_s) + 1
    out_h = ((var_h - var_f) / var_s) + 1
    out_d = var_d
    if ((var_w - var_f) % var_s) or ((var_h - var_f) % var_s):
        var.set('bad parameter！')
    else:
        var.set('')
    w.delete(0, tk.END)
    h.delete(0, tk.END)
    d.delete(0, tk.END)
    w.insert('insert', int(out_w))
    h.insert('insert', int(out_h))
    d.insert('insert', int(out_d))


def copy():
    var_w = int(w.get())
    var_h = int(h.get())
    var_d = int(d.get())
    W.delete(0, tk.END)
    H.delete(0, tk.END)
    D.delete(0, tk.END)
    W.insert('insert', int(var_w))
    H.insert('insert', int(var_h))
    D.insert('insert', int(var_d))


window = tk.Tk()
window.title('DNN-parameter-calculator')
window.geometry('800x500')


tk.Label(window, text='in put', font=('Arial', 12), width=15, height=2).place(x=100, y=10, anchor='nw')
tk.Label(window, text='out put', font=('Arial', 12), width=15, height=2).place(x=550, y=10, anchor='nw')
tk.Label(window, text='filter size', font=('Arial', 12), width=15, height=2).place(x=10, y=300, anchor='nw')
tk.Label(window, text='filter number', font=('Arial', 12), width=15, height=2).place(x=10, y=340, anchor='nw')
tk.Label(window, text='stride', font=('Arial', 12), width=15, height=2).place(x=10, y=380, anchor='nw')
tk.Label(window, text='padding', font=('Arial', 12), width=15, height=2).place(x=10, y=420, anchor='nw')


canvas = tk.Canvas(window, height=250, width=700)
canvas.place(x=50, y=50, anchor='nw')
image_file = tk.PhotoImage(file='timg.png')
canvas.create_image(10, 10, anchor='nw', image=image_file)
canvas.create_image(700, 10, anchor='ne', image=image_file)

W = tk.Entry(window)
W.place(x=150, y=120, width=30, height=20, anchor='nw')
H = tk.Entry(window)
H.place(x=60, y=180, width=30, height=20, anchor='nw')
D = tk.Entry(window)
D.place(x=110, y=80, width=30, height=20, anchor='nw')
F = tk.Entry(window)
F.place(x=150, y=310, width=30, height=20, anchor='nw')
K = tk.Entry(window)
K.place(x=150, y=350, width=30, height=20, anchor='nw')
S = tk.Entry(window)
S.place(x=150, y=390, width=30, height=20, anchor='nw')
P = tk.Entry(window)
P.place(x=150, y=430, width=30, height=20, anchor='nw')

w = tk.Entry(window)
w.place(x=580, y=120, width=30, height=20, anchor='nw')
h = tk.Entry(window)
h.place(x=480, y=180, width=30, height=20, anchor='nw')
d = tk.Entry(window)
d.place(x=540, y=80, width=30, height=20, anchor='nw')


conv = tk.Button(window, text='convolution', width=30, height=20, command=compute_conv)
conv.place(x=250, y=320, width=150, height=50, anchor='nw')
pool = tk.Button(window, text='pooling', width=30, height=20, command=compute_pool)
pool.place(x=250, y=400, width=150, height=50, anchor='nw')
copy = tk.Button(window, text='copy', width=30, height=20, command=copy)
copy.place(x=450, y=320, width=150, height=130, anchor='nw')

var = tk.StringVar()
l = tk.Label(window, textvariable=var, font=('Arial', 12), width=15, height=2)
l.place(x=630, y=320, width=150, height=130, anchor='nw')

window.mainloop()