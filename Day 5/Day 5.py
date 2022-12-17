# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 11:19:00 2022

@author: Noa
"""


'''part 1'''
x = open("day5in.txt", "r").read()

x, y = x.split("\n\n")
x, y = x.splitlines(), y.splitlines()

q = [""]*9

for i in range(len(x)-2, -1, -1):
    for r in range(1, len(x[0]), 4):
        if x[i][r].isupper():
            q[r//4] += x[i][r]
            
for i in y:
    a, b, c, d, e, f = i.split()

    b, d, f = int(b), int(d), int(f)

    d, f = d-1, f-1
    
    q[f] += q[d][-b:][::-1]
    q[d] = q[d][:-b]

t = ""
for i in q:
    try:
        t += i[-1]
    except:
        continue

print(f'The crate that ends at the top of each stack when using the cratemover 9000 is: {t}')


'''part 2'''
x = open("day5in.txt", "r").read()

x, y = x.split("\n\n")
x, y = x.splitlines(), y.splitlines()

q = [""]*9

for i in range(len(x)-2, -1, -1):
    for r in range(1, len(x[0]), 4):
        if x[i][r].isupper():
            q[r//4] += x[i][r]

for i in y:
    a, b, c, d, e, f = i.split()

    b, d, f = int(b), int(d), int(f)

    d, f = d-1, f-1

    q[f] += q[d][-b:]
    q[d] = q[d][:-b]

t = ""
for i in q:
    try:
        t += i[-1]
    except:
        continue

print(f'The crate that ends at the top of each stack when using the cratemover 9001 is: {t}')
