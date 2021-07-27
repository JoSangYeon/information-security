# from matplotlib import pyplot as plt
# from matplotlib import animation
# import numpy as np
# import random
# import time
# #
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib.figure import Figure
# import tkinter as Tk
#
# fig = plt.figure()     #figure(도표) 생성
#
#
#
# ax = plt.subplot(211, xlim=(0, 50), ylim=(0, 1024))
# ax_2 = plt.subplot(212, xlim=(0, 50), ylim=(0, 512))
#
#
# max_points = 50
# max_points_2 = 50
#
#
# line, = ax.plot(np.arange(max_points),
#                 np.ones(max_points, dtype=np.float)*np.nan, lw=1, c='blue',ms=1)
# line_2, = ax_2.plot(np.arange(max_points_2),
#                 np.ones(max_points, dtype=np.float)*np.nan, lw=1,ms=1)
#
#
# def init():
#     return line
# def init_2():
#     return line_2
#
#
# def animate(i):
#     y = random.randint(0,1024)
#     old_y = line.get_ydata()
#     new_y = np.r_[old_y[1:], y]
#     line.set_ydata(new_y)
#     print(new_y)
#     return line
#
# def animate_2(i):
#     y_2 = random.randint(0,512)
#     old_y_2 = line_2.get_ydata()
#     new_y_2 = np.r_[old_y_2[1:], y_2]
#     line_2.set_ydata(new_y_2)
#     print(new_y_2)
#     return line_2
#
#
#
#
# root = Tk.Tk() #추가
# label = Tk.Label(root,text="라벨").grid(column=0, row=0)#추가
# canvas = FigureCanvasTkAgg(fig, master=root) #
# canvas.get_tk_widget().grid(column=0,row=1) #
#
#
#
# anim = animation.FuncAnimation(fig, animate  , init_func= init ,frames=200, interval=50, blit=False)
# anim_2 = animation.FuncAnimation(fig, animate_2  , init_func= init_2 ,frames=200, interval=10, blit=False)
# Tk.mainloop()


import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np


root = tkinter.Tk()
root.wm_title("Embedding in Tk")

fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.