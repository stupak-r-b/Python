#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    count = 0
    while True:
        if count == 3 or wall_is_on_the_right(): break
        move_right(n = 1)
        if cell_is_filled(): count += 1
        elif not cell_is_filled(): count = 0
if __name__ == '__main__':
    run_tasks()
