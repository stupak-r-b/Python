#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    count = 0
    for i in range(5):
        move_right(n=1); fill_cell(); move_right(n=1)
        move_down(n=1); fill_cell(); move_left(n=1); fill_cell(); move_left(); fill_cell()
        move_down(n=1); move_right(n=1); fill_cell(); move_right(n=1)
        move_up(n=2); move_left(n=2)
        count += 1
        if count < 5:
            move_right(n = 4); move_up(n = 1)


if __name__ == '__main__':
    run_tasks()
