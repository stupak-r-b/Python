#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_2():
    while True:
        if not wall_is_above(): fill_cell()
        if wall_is_on_the_right():
            if not cell_is_filled(): fill_cell()
            if wall_is_on_the_right(): break
        move_right(n = 1)


if __name__ == '__main__':
    run_tasks()
