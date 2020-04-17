#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_22():
    while True:
        if wall_is_above() and wall_is_on_the_right() and wall_is_on_the_left() or \
           wall_is_beneath() and wall_is_above() and wall_is_on_the_right() or \
           wall_is_beneath() and wall_is_above() and wall_is_on_the_left(): break
        elif not wall_is_above():
            while True:
                if wall_is_above(): break
                move_up(n = 1)
        elif not wall_is_on_the_right():
            while True:
                if wall_is_on_the_right(): break
                move_right(n = 1)
        elif not wall_is_on_the_left():
            while True:
                if wall_is_on_the_left(): break
                move_left(n = 1)


if __name__ == '__main__':
    run_tasks()
