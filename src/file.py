#!/usr/bin/env python3
#-*- coding: utf-8 -*-


import random


arr = sorted([random.randint(0, 100) for _ in range(11)])


def bin_search(data: list, low: int, high: int, target: int):
    if low > high:
        return
    global arr
    mid = (low + high) // 2
    # print(low, high, mid)
    if data[mid] == target:
        return mid
    elif arr[mid] < target:
        low = mid + 1
    elif arr[mid] > target:
        high = mid - 1
    return bin_search(data, low, high, target) if low <= high else None


def run():
    global arr
    print(arr)
    try:
        num = int(input("Insert a number: "))
    except ValueError:
        print("Only numbers")
        return
    res = bin_search(arr, 0, len(arr) - 1 , num)
    if res is not None:
        print("Found at index {}".format(res))
    else:
        print("Item {} not found".format(num))


if __name__ == '__main__':
    run()
