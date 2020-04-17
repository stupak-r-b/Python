#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    while True:
        if wall_is_beneath() and not wall_is_above():
            if wall_is_on_the_right():
                while not wall_is_on_the_left():
                    fill_cell(); move_left(n = 1)
                break
            elif wall_is_on_the_left():
                fill_cell()
                break
        elif wall_is_above() and wall_is_on_the_left() and not wall_is_beneath():
            while not wall_is_on_the_right():
                fill_cell(); move_right(n = 1)
        elif wall_is_on_the_left() and not wall_is_on_the_right():
            fill_cell(); move_down(n = 1)
            while not wall_is_on_the_right():
                fill_cell(); move_right(n = 1)
        elif wall_is_on_the_right() and not wall_is_on_the_left():
            fill_cell(); move_down(n = 1)
            while not wall_is_on_the_left():
                fill_cell(); move_left(n = 1)
        else:
            fill_cell()
            break

if __name__ == '__main__':
    run_tasks()
