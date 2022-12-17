# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 21:06:17 2022

@author: Noa
"""


'''part 1'''
x = open("day4in.txt", "r").read().splitlines()

pairs = 0

for i in range(0, len(x)):
    a = x[i]

    b = a.partition(',')
    e1, e2 = b[0], b[2]

    c, d = e1.partition('-'), e2.partition('-')
    e1s, e1e = int(c[0]), int(c[2])
    e2s, e2e = int(d[0]), int(d[2])

    e1Set = set(range(e1s, e1e+1))
    e2Set = set(range(e2s, e2e+1))

    if e1Set.issubset(e2Set) or e2Set.issubset(e1Set):
        pairs += 1

print(f'The number of assignment pairs where one range fully contains the other is: {pairs}')


'''part 2'''
overlap = 0

for i in range(0, len(x)):
    a = x[i]

    b = a.partition(',')
    e1, e2 = b[0], b[2]

    c, d = e1.partition('-'), e2.partition('-')
    e1s, e1e = int(c[0]), int(c[2])
    e2s, e2e = int(d[0]), int(d[2])

    e1Set = set(range(e1s, e1e+1))
    e2Set = set(range(e2s, e2e+1))

    if not (e1Set.isdisjoint(e2Set) or e2Set.isdisjoint(e1Set)):
        overlap += 1

print(f'The number of assignment pairs where the ranges overlap is: {overlap}')
