#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    value = True
    while value:
        if not wall_is_beneath():
            move_down(n = 1)
        else:
            while value:
                if wall_is_beneath():
                    move_right(n = 1)
                else:
                    move_down(n = 1)
                    move_left(n = 1)
                    while value:
                        if wall_is_on_the_left(): value = False
                        elif wall_is_above():
                            move_left(n = 1)



if __name__ == '__main__':
    run_tasks()
