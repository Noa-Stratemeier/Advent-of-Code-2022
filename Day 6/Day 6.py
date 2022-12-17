# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 17:38:19 2022

@author: Noa
"""

'''part 1'''
with open('day6in.txt', 'r') as file:
    x = file.read()

    for i in range(len(x) - 3):
        a = x[i] + x[i+1] + x[i+2] + x[i+3]

        if len(set(a)) == len(a):
            b = i + 4
            break

    print(f'The number of characters needed to be processed before the first start-of-packet marker is detected is: {b}')


'''part 2'''
with open('day6in.txt', 'r') as file:
    x = file.read()

    for i in range(len(x) - 13):
        a = ''

        for j in range(14):
            a += x[i + j]

        if len(set(a)) == len(a):
            b = i + 14
            break

    print(f'The number of characters needed to be processed before the first start-of-message marker is detected is: {b}')
