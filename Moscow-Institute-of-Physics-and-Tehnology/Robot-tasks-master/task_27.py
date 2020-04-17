#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    count = 1; value = True
    move_right(n = 1); fill_cell()
    while True:
        try:
            move_right(n = count); fill_cell()
            count += 1
        except:
            break

if __name__ == '__main__':
    run_tasks()
