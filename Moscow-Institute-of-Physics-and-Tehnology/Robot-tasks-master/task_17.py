#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
    while True:
        if cell_is_filled():
            move_right(n = 1)
            if cell_is_filled():
                break
            else:
                move_left(n = 2)
                break
        move_up(n = 1)


if __name__ == '__main__':
    run_tasks()
