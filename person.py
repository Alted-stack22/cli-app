#!/usr/bin/env python3
#-*- coding: utf-8 -*-


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    def __str__(self) -> str:
        return "Hello, my name is {} and I'm {} years old.".format(self.name, self.age)


def run():
    p_1 = Person("David", 26)
    print(p_1)


if __name__ == '__main__':
    run()
