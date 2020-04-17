#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_7():
    while True:
        if not wall_is_above() and not wall_is_beneath(): break
        move_right(n = 1)


if __name__ == '__main__':
    run_tasks()
