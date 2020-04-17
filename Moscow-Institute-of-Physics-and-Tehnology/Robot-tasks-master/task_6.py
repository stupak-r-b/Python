#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_3():
    n = 1
    value = True
    while value:
        if not wall_is_beneath(): move_right(n)
        elif wall_is_beneath():
            move_right(n)
            if not wall_is_beneath(): break



if __name__ == '__main__':
    run_tasks()
