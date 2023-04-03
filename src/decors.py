#!/usr/bin/env python3
#-*- coding: utf-8 -*-


from time import sleep


SPACES: int = 40
DELAY: float = 0.5


def debug(func):
    def wrapper(*args: tuple, **kwargs: dict):
        print("Receiving...")
        sleep(DELAY)
        print("Processing...")
        sleep(DELAY)
        print(" Status ".center(SPACES, "*"))
        sleep(DELAY)
        res = func(*args, **kwargs)
        sleep(DELAY)
        print(f"Name -> {func.__name__}".center(SPACES, " "))
        sleep(DELAY)
        print(f"Checking -> {args} {kwargs}".center(SPACES, " "))
        sleep(DELAY)
        print(" Status ".center(SPACES, "*"))
        sleep(DELAY)
        print("Finalizing...")
        return res
    return wrapper

@debug
def show(*args: tuple, **kwargs: dict):
    #? Debug options:
    #? for idx, element in enumerate(args): print(f"Func | {idx}: {element}".center(SPACES, " "))
    #? for key, value in kwargs.items(): print(f"Func | {key}: {value}".center(SPACES, " "))
    print(f"Func | {args} {kwargs}".center(SPACES, " "))


def run():
    req = show(0, 1, 2, opt="sum")
    if req is not None:
        print(req)


if __name__ == '__main__':
    run()
