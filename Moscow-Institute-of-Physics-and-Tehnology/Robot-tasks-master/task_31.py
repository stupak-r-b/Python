#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.07)
def task_8_30():
    count = 0
    while True:
        if wall_is_beneath() and wall_is_on_the_left() or wall_is_beneath() and wall_is_on_the_right():
            count += 1
            if count > 1 and wall_is_on_the_left(): break
        while not wall_is_on_the_right():
            move_right(n = 1)
            if not wall_is_beneath():
                while not wall_is_beneath():move_down(n = 1); count = 0
        while not wall_is_on_the_left():
            move_left(n = 1)
            while not wall_is_beneath():move_down(n = 1); count = 0

if __name__ == '__main__':
    run_tasks()
