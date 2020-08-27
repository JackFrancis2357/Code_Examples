import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
from tkinter import ttk

import urllib
import json

import pandas as pd
import numpy as np

matplotlib.use("TkAgg")

LARGE_FONT = ('Verdana', 12)
style.use('ggplot')

f = Figure(figsize=(3, 3), dpi=100)
a = f.add_subplot(111)


def animate(i):
    pullData = open('sampleData.txt', 'r').read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))
    a.clear()
    a.plot(xList, yList)


class SampleApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        tk.Tk.wm_title(self, 'SampleApp')

        container = ttk.Frame(self)

        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


def qf(param):
    print(param)


class StartPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text='Hello', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # Command has no parms or the function will be called.
        # If needed to pass, use lambda!!
        button1 = ttk.Button(self, text='Visit Page 1', command=lambda: controller.show_frame(PageOne))
        button1.pack(pady=10, padx=10)

        button2 = ttk.Button(self, text='Go to Page Two', command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text='Go to Page Three', command=lambda: controller.show_frame(PageThree))
        button3.pack()


class PageOne(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text='Page One', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Return to Start Page', command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text='Go to Page Two', command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text='Go to Page Three', command=lambda: controller.show_frame(PageThree))
        button3.pack()


class PageTwo(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text='Page Two', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Return to Start Page', command=lambda: controller.show_frame(StartPage))
        button1.pack()

        # button2 = ttk.Button(self, text='Go to Page One', command=lambda: controller.show_frame(PageOne))
        # button2.pack()

        button3 = ttk.Button(self, text='Go to Page Three', command=lambda: controller.show_frame(PageThree))
        button3.pack()


class PageThree(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text='Page Three', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Return to Start Page', command=lambda: controller.show_frame(StartPage))
        button1.pack()

        # button2 = ttk.Button(self, text='Go to Page One', command=lambda: controller.show_frame(PageOne))
        # button2.pack()
        #
        # button3 = ttk.Button(self, text='Go to Page Two', command=lambda: controller.show_frame(PageTwo))
        # button3.pack()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


app = SampleApp()
ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()
