#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import random


arr = sorted([random.randint(0, 100) for _ in range(10)])


def bin_search(data: list, target: int):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1


def run():
    global arr
    print("List:", arr)
    try:
        num = int(input("Insert a number: "))
    except ValueError:
        print("Insert a valid number!")
        return
    res = bin_search(arr, num)
    if res is not None:
        print("Found in index {}".format(res))
    else:
        print("Item {} not found!".format(num))


if __name__ == '__main__':
    run()
