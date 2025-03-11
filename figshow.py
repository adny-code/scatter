import matplotlib.pyplot as plt
import numpy as np
import math
from time import time, ctime, sleep
from scatter_item import scatter_item
import excel_word
import os

flag_of_start_and_stop = 1
quit_program = 0

word_line = excel_word.sahpe_to_line(excel_word.filename1)
word_line1 = excel_word.sahpe_to_line(excel_word.filename2)
word_line2 = excel_word.sahpe_to_line(excel_word.filename3)

# number of scatter items.
nums_scatter = 390

# generate scatters object.
scatter_500 = scatter_item(nums_scatter, 200, 100, -200, -100)

# generate scatters size.
size_numbers = list(np.random.randint(20, 600, nums_scatter))

def initial_plt():
    fig = plt.figure(num='scatter_word', figsize=(16,8), dpi= 128, frameon = False)
    ax = fig.add_subplot(111)
    ax.set_autoscale_on(False)
    ax.set_xticks([-200, 200])
    ax.set_yticks([-100, 100])
    ax.grid(False)
    return ax

def scatter_show(x, y):
    point_numbers = list(range(nums_scatter))
    """
    marker: shape of point
    alpha: transparency of point
    cmap: color of point
    """
    plt.scatter(x, y, c = point_numbers, marker = 'o', alpha = 0.8,
                cmap = plt.cm.Reds, edgecolors = 'none',
                s = size_numbers)

"""
calculate one frame of the plot.
"""
def show_color(chose = 1):
    global quit_program
    if chose == 1:
        ax = initial_plt()
        ax.set_title('CHINA')
        scatter_500.on_word_or_not(word_line)
    if chose == 2:
        ax = initial_plt()
        ax.set_title('CHINA NO.1')
        scatter_500.on_word_or_not(word_line1)
    if chose == 3:
        ax = initial_plt()
        ax.set_title('I LOVE CHIAN')
        scatter_500.on_word_or_not(word_line2)

    scatter_show(scatter_500.x, scatter_500.y)
    scatter_500.on_board_or_not()
    scatter_500.move_scatter()
    if (quit_program == 1): 
        os._exit(0)
    plt.pause(0.01)
    plt.cla()


def spread_fast_to_slow(chose):
    global flag_of_start_and_stop
    global quit_program
    if chose == 1:
        # change the speed of scatter from fast to slow in 5 frame.
        for i in range(5):
            for j in range(15 + i * 1):
                scatter_500.spread(4 - i)
                ax = initial_plt()
                ax.set_title('CHINA')
                scatter_show(scatter_500.x, scatter_500.y)
                scatter_500.on_board_or_not()
                scatter_500.move_scatter()
                if (quit_program == 1): 
                    os._exit(0)
                if (flag_of_start_and_stop == 0):
                    flag_of_start_and_stop = 1
                    sleep(15)
                plt.pause(0.01)
                plt.cla()
    if chose == 2:
        for i in range(5):
            for j in range(15 + i * 1):
                scatter_500.spread(4 - i)
                ax = initial_plt()
                ax.set_title('CHINA NO.1')
                scatter_show(scatter_500.x, scatter_500.y)
                scatter_500.on_board_or_not()
                scatter_500.move_scatter()
                if (quit_program == 1): 
                    os._exit(0)
                if (flag_of_start_and_stop == 0):
                    flag_of_start_and_stop = 1
                    sleep(15)
                plt.pause(0.01)
                plt.cla()
    if chose == 3:
        for i in range(5):
            for j in range(15 + i * 1):
                scatter_500.spread(4 - i)
                ax = initial_plt()
                ax.set_title('I LOVE CHIAN')
                scatter_show(scatter_500.x, scatter_500.y)
                scatter_500.on_board_or_not()
                scatter_500.move_scatter()
                if (quit_program == 1): 
                    os._exit(0)
                if (flag_of_start_and_stop == 0):
                    flag_of_start_and_stop = 1
                    sleep(15)
                plt.pause(0.01)
                plt.cla()


