from atexit import register
from time import time, ctime, sleep
import matplotlib.pyplot as plt
import datetime
import numpy as np
import math
from scatter_item import scatter_item
import figshow
import excel_word
import os
from matplotlib.widgets import Button, RadioButtons

figshow.flag_of_start_and_stop
figshow.quit_program

def button_press(event):
    figshow.flag_of_start_and_stop = 0

def button_press2(event):
    figshow.flag_of_start_and_stop = 1

def button_press3(event):
    figshow.quit_program = 1

def main():
    ax = figshow.initial_plt()
    global flag_of_start_and_stop
    global quit_program
    global button1
    size = plt.axes([0.68, 0.015, 0.13, 0.06])
    button1 = Button(size, 'stop')
    # register button.
    button1.on_clicked(button_press)

    global button2
    size2 = plt.axes([0.05, 0.015, 0.6, 0.06])
    button2 = Button(size2, 'click quit to exit')
    # register button.
    button2.on_clicked(button_press2)

    global button3
    size = plt.axes([0.84, 0.015, 0.13, 0.06])
    button3 = Button(size, 'quit')
    # register button.
    button3.on_clicked(button_press3)

    count = 0
    while(1):
        while(1):
            figshow.show_color(1)

            if(figshow.flag_of_start_and_stop==0):
                figshow.flag_of_start_and_stop = 1
                sleep(15)

            count += 1
            # the frame of one round.
            if count > 300:
                count = 0
                break
        figshow.scatter_500.line_and_taken = []
        figshow.spread_fast_to_slow(1)

        while (1):
            figshow.show_color(2)

            if(figshow.flag_of_start_and_stop==0):
                figshow.flag_of_start_and_stop = 1
                sleep(15)

            count += 1
            # the frame of one round.
            if count > 300:
                count = 0
                break
        figshow.scatter_500.line_and_taken = []
        figshow.spread_fast_to_slow(2)

        while (1):
            figshow.show_color(3)

            if(figshow.flag_of_start_and_stop==0):
                figshow.flag_of_start_and_stop = 1
                sleep(15)

            count += 1
            # the frame of one round.
            if count > 300: 
                count = 0
                break
        figshow.scatter_500.line_and_taken = []
        figshow.spread_fast_to_slow(3)


@register 
def atexit():
     print('all done at:' + ctime())

if __name__ == '__main__':
    time_begin = datetime.datetime.now()
    main()
    time_end = datetime.datetime.now()
    print(str((time_end - time_begin).microseconds) + 'us')

