#!/usr/bin/env python
# coding: utf-8

import math


class Sorting:
    # class realizes the sorting for array of numbers
    arr = []

    def __init__(self, arr):
        if not isinstance(arr, list):
            raise TypeError
        is_elem_digit = self.is_digit(arr[0])        
        if not (is_elem_digit or type(arr[0]) == str):
            raise TypeError
        for i in range(len(arr)):
            if is_elem_digit:
                if not self.is_digit(arr[i]):
                    raise TypeError
            elif type(arr[i]) != str:
                raise TypeError
        self.arr = arr

    def batcher_sort(self):
        if len(self.arr) < 2:
            return
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
    
    def is_digit(self, value):
        if type(value) == int or type(value) == float:
            return True
        else:
            return False
