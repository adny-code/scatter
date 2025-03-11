import numpy as np
import math

class scatter_item():
    def __init__(self, nums, board_x_up, board_y_up, board_x_l, board_y_l,):
        self.nums = nums

        # border of plot.
        self.board_x_up = board_x_up
        self.board_y_up = board_y_up
        self.board_x_l = board_x_l
        self.board_y_l = board_y_l

        # on pattern or not.
        self.on_postion = 0

        # generate numbers random position\direction\speed\scattetr size in plot.
        self.x = np.random.randint(-200, 201, nums)
        self.y = np.random.randint(-100, 101, nums)
        self.direction_x = np.random.choice([-1, 1], nums)
        self.direction_y = np.random.choice([-1, 1], nums)
        self.speed = np.random.randint(3, 6, nums)
        self.scatter_size = np.random.randint(200, 500, nums)

        # ocuppied index of pattern.
        self.line_and_taken = []

    """
    determine whether the scatter is on the plot board or not, if it is, change the direction.
    """
    def on_board_or_not(self):
        for i in range(self.nums):
            if((self.x[i] > self.board_x_up) or (self.x[i] < self.board_x_l)):
                self.direction_x[i] = - self.direction_x[i]
                # if the scatter is still out of the board, move it back.
                if (self.x[i] > self.board_x_up): self.x[i] -= 3
                if (self.x[i] < self.board_x_up): self.x[i] += 3
            if((self.y[i] > self.board_y_up) or (self.y[i] < self.board_y_l)):
                self.direction_y[i] = - self.direction_y[i]
                # if the scatter is still out of the board, move it back.
                if (self.y[i] > self.board_y_up): self.y[i] -= 3
                if (self.y[i] < self.board_y_up): self.y[i] += 3

    """
    move the scatter in the plot.
    """
    def move_scatter(self):
        self.x += self.direction_x * self.speed
        self.y += self.direction_y * self.speed

    """
    reset the speed of scatter."""
    def spread(self, level=0):
        if level == 0:
            self.speed = np.random.randint(3, 6, self.nums)
        if level == 1:
            self.speed = np.random.randint(4, 7, self.nums)
        if level == 2:
            self.speed = np.random.randint(5, 8, self.nums)
        if level == 3:
            self.speed = np.random.randint(6, 9, self.nums)
        if level == 4:
            self.speed = np.random.randint(7, 10, self.nums)


    """
    determine whether the scatter is on the pattern or not, if it is, stop it.
    """
    def on_word_or_not(self, word_shape_line):
        for i in range(self.nums):
            # calculate weather the scatter is on the pattern. 
            x = int(self.x[i] * 0.25 + 50)
            y = int(self.y[i] * (-0.25) + 25)
            line = 100 * y + x

            # stop scatter.
            if(line in word_shape_line and line not in self.line_and_taken):
                self.speed[i] = 0
                self.line_and_taken.append(line)

