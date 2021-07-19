"""
import webbrowser
from tkinter import *
from tkinter import ttk
root = Tk()
style = ttk.Style()
open_facebook = webbrowser.open('http://www.facebook.com')
open_google = webbrowser.open('http://www.google.com')
open_yahoo = webbrowser.open('http://www.yahoo.com')
open_youtube = webbrowser.open('http://www.youtube.com')
style.configure("TButton",
                font="Serif 18",
                padding=10)
main_frame = Frame(root)
main_frame.grid(row=0, columnspan=4)
button_facebook = ttk.Button(main_frame, text='Facebook', command=open_facebook).grid(row=1, column=0)
button_google = ttk.Button(main_frame, text='Google', command=open_google).grid(row=1, column=1)
button_yahoo = ttk.Button(main_frame, text='Yahoo', command=open_yahoo).grid(row=1, column=2)
button_youtube = ttk.Button(main_frame, text='Youtube', command=open_youtube).grid(row=1, column=3)
root.mainloop()
"""