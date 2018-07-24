#!/bin/python3

import sys

def miniMaxSum(arr):
    print(sum(arr)-max(arr),sum(arr)-min(arr))
    return 0

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)
