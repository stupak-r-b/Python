#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    count = 1; count1 = 0
    while not wall_is_on_the_right(): move_right(n = 1); count += 1
    move_left(n = count-1); middle_point = (count // 2) + 1
    while True:
        if count == 1:
            while not wall_is_beneath(): move_down(n = 1)
            while not wall_is_on_the_left(): move_left(n = 1)
            break
        for j in range(count - 2):
            move_right(n = 1)
            fill_cell()
        move_right(n = 1)
        for k in range(count - 2):
            move_down(n = 1)
            fill_cell()
        move_down(n = 1)
        for z in range(count - 2):
            move_left(n = 1)
            fill_cell()
        move_left(n = 1)
        for o in range(count - 2):
            move_up(n = 1)
            fill_cell()
        move_up(n = 1)
        move_right(n = 1); move_down(n = 1); count -= 2






if __name__ == '__main__':
    run_tasks()
