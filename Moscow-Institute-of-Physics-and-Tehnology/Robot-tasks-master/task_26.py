#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    count = 0; count1 = 0
    for i in range(5):
        for j in range(10):
            move_right(n=1); fill_cell(); move_right(n=1)
            move_down(n=1); fill_cell(); move_left(n=1); fill_cell(); move_left(); fill_cell()
            move_down(n=1); move_right(n=1); fill_cell(); move_right(n=1)
            move_up(n=2); move_left(n=2)
            count += 1
            if count < 10:
                move_right(n=4)
        if count1 < 4:
            move_left(n = 36); move_down(n = 4); count = 0; count1 += 1
        else: move_left(n = 36)

if __name__ == '__main__':
    run_tasks()
