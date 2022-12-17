# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 17:34:17 2022

@author: Noa
"""


with open('day1in.txt', 'r') as file:

    x = file.read().splitlines() # list of all calories, calories carried by each elf are seperated by ''

    elves = []
    current_cal = 0

    # adds total calories carried by each elf to 'elves'
    for item in x:
        if item == '':
            elves.append(current_cal)
            current_cal = 0
        else:
            current_cal += int(item)

    # part 1
    print(f'The largest number of calories carried by an elf is: {max(elves)}')
    # part 2
    print(f'The sum of the top 3 most calorie carrying elves is: {sum(sorted(elves)[-3:])}')
