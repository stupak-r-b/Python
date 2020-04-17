#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_11():
    while True:
        if wall_is_above() and wall_is_beneath():
            fill_cell()
            if wall_is_on_the_right(): break
        if not wall_is_beneath():
            move_down(n = 1)
            fill_cell()
            move_up(n = 1)
            if not wall_is_above():
                move_up(n = 1)
                fill_cell()
                move_down(n = 1)
            if wall_is_on_the_right(): break
        elif not wall_is_above():
            move_up(n = 1)
            fill_cell()
            move_down(n = 1)
            if not wall_is_beneath():
                move_down(n = 1)
                fill_cell()
                move_up(n = 1)
            if wall_is_on_the_right(): break
        move_right(n = 1)

if __name__ == '__main__':
    run_tasks()
