#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    if wall_is_above():
        if wall_is_on_the_left():
            while True:
                if not wall_is_on_the_right():
                    move_right(n = 1)
                else:
                    if wall_is_beneath(): break
                    move_down(n = 1)
        elif wall_is_on_the_right():
            while True:
                if not wall_is_on_the_left():
                    move_left(n = 1)
                else:
                    if wall_is_beneath(): break
                    move_down(n = 1)
    elif wall_is_beneath():
        if wall_is_on_the_left():
            while True:
                if not wall_is_on_the_right():
                    move_right(n = 1)
                else:
                    if wall_is_above(): break
                    move_up(n = 1)
        elif wall_is_on_the_right():
            while True:
                if not wall_is_on_the_left():
                    move_left(n=1)
                else:
                    if wall_is_above(): break
                    move_up(n=1)


if __name__ == '__main__':
    run_tasks()
