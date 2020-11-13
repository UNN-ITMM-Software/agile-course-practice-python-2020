#!/usr/bin/env python
# coding: utf-8

import math


class Sorting:
    # class realizes the sorting for array of numbers
    arr = []

    def __init__(self, arr):
        self.arr = arr

    def batcher_sort(self):
        t = int(math.log(len(self.arr), 2))
        p = 2 ** (t - 1)
        while p > 0:
            q = 2 ** (t - 1)
            d = p
            while q >= p:
                i = 0
                while i < len(self.arr) - d:
                    if self.arr[i] > self.arr[i + d]:
                        self.arr[i], self.arr[i + d] = self.arr[i + d], self.arr[i]
                    i += 1
                d = q - p
                q = int(q / 2)
            p = p // 2

    def result_str(self):
        string = ''
        for j in range(len(self.arr)):
            space = ''
            if j < len(self.arr) - 1:
                space = ' '
            string += str(self.arr[j]) + space
        return string

