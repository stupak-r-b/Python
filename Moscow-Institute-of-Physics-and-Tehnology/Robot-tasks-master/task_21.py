#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    count = 1
    for i in range(13):
        move_down(n = 1); move_right(n = 1)
        for j in range(count):
            fill_cell()
            move_right(n = 1)
        move_left(n = count + 1)
        count += 1
    move_down(n = 1); move_right(n = 1)

if __name__ == '__main__':
    run_tasks()
