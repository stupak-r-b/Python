#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    while True:
        if wall_is_on_the_right():
            while not wall_is_on_the_left():
                move_left(n = 1)
                if not wall_is_above() and wall_is_beneath():
                    while not wall_is_above(): move_up(n = 1)
                elif wall_is_on_the_left():
                    break
            break
        elif wall_is_on_the_left():
            while not wall_is_on_the_right():
                move_right(n = 1)
                if not wall_is_above() and wall_is_beneath():
                    while not wall_is_above(): move_up(n = 1)
        else: move_right(n = 1)


if __name__ == '__main__':
    run_tasks()
