import os
from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.colors as colors


class Board:
    def __init__(self, arrStart):
        self.arrA = arrStart
        self.arrB = deepcopy(arrStart)


def nextGen(arr1, arr2):

    # not the fanciest but it works and is easy to understand
    # two nested loops, every value checks neighbors for values
    # temp is the neighbor count
    # reads arr1, writes arr2, the update function below exchanges these every loop

    for indexY, y in enumerate(arr1):
        for indexX, x in enumerate(y):
            temp = 0

            if indexX != 0:
                if arr1[indexY][indexX-1] > 0:
                    temp += 1

            if indexX != len(arr1[indexY])-1:
                if arr1[indexY][indexX+1] > 0:
                    temp += 1

            if indexY != 0:
                if arr1[indexY-1][indexX] > 0:
                    temp += 1

            if indexY != len(arr1)-1:
                if arr1[indexY+1][indexX] > 0:
                    temp += 1

            if indexX != 0 and indexY != 0:
                if arr1[indexY-1][indexX-1] > 0:
                    temp += 1

            if indexX != len(arr1[indexY])-1 and indexY != len(arr1)-1:
                if arr1[indexY+1][indexX+1] > 0:
                    temp += 1

            if indexX != 0 and indexY != len(arr1)-1:
                if arr1[indexY+1][indexX-1] > 0:
                    temp += 1

            if indexX != len(arr1[indexY])-1 and indexY != 0:
                if arr1[indexY-1][indexX+1] > 0:
                    temp += 1

            live = 0
            arr2[indexY][indexX] = 0

            if x > 0:
                if temp == 2 or temp == 3:
                    arr2[indexY][indexX] = 1
                    live = 1
            if x == 0:
                if temp == 3:
                    arr2[indexY][indexX] = 1
                    live = 1

    # print(f"x = {x}, index X = {indexX}, index Y = {indexY}, temp = {temp}, live = {live}")


# ---

# change the array/matrix size here, or make your own by uncommenting the manual array below
arr_size = 20
randoArray = np.random.randint(2, size=(arr_size, arr_size))

"""
randoArray = [[1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0],
              [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1],
              [0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
              [0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
              [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1],
              [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
              [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
              [0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
              [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1],
              [0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
              [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0],
              [0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1]]

"""

# ---

board1 = Board(randoArray)


# graphical display begins here

cmap = colors.ListedColormap(['white', 'black'])


def update(i):

    # update function loop

    os.system('clear')

    print(i)

    # interchanging arrays

    if i % 2 == 0:
        nextGen(board1.arrA, board1.arrB)
        mArr.set_array(np.matrix(board1.arrB))
    else:
        nextGen(board1.arrB, board1.arrA)
        mArr.set_array(np.matrix(board1.arrA))


fig, ax = plt.subplots()

mArr = ax.matshow(np.matrix(board1.arrB), cmap=cmap)

ani = FuncAnimation(fig, update, interval=500)

plt.xticks(np.arange(0, arr_size, 1))
plt.yticks(np.arange(0, arr_size, 1))


plt.show()
