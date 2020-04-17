#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    count = 0
    while True:
        move_right(n = 1); count += 1
        if not wall_is_above():
            while not wall_is_above():
                move_up(n = 1); fill_cell()
            else:
                while not wall_is_beneath():
                    move_down(n = 1)
        if wall_is_beneath() and wall_is_on_the_right():
            move_left(n = count)
            break



if __name__ == '__main__':
    run_tasks()
