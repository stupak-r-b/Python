#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    count = 0
    while count != 5:
        move_right(n = 1)
        if cell_is_filled(): count += 1


if __name__ == '__main__':
    run_tasks()
