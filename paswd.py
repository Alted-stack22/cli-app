#!/usr/bin/env python3
#-*- coding: utf-8


from getpass import (
    getpass,
    getuser
)
from time import sleep


CREDENTIALS: dict[str, str] = {
    'username': 'ubuntu',
    'password': '12345678'
}
DELAY: float = 0.5


def request(func):
    def wrapper():
        username = getuser()
        passwd = getpass("passwd >> ")
        sleep(DELAY)
        print("Receiving...")
        sleep(DELAY)
        print("Processing...")
        sleep(DELAY)
        if username == CREDENTIALS['username'] and passwd == CREDENTIALS['password']:
            return func()
        else:
            print("Incorrect password. Access denied")
    return wrapper


@request
def login():
    print("Correct password. Access granted")


def run():
    login()


if __name__ == '__main__':
    run()
