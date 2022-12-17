# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 19:15:26 2022

@author: Noa
"""


import string

'''part 1'''
with open('day3in.txt', 'r') as file:
    x = file.read().splitlines()

    alph = list(string.ascii_lowercase) + list(string.ascii_uppercase) # dictionary of upper and lowercase letters with assigned int values
    dic1 = {alph[i-1]: i for i in range(1, 53)}

    tot = 0

    # finds the common item between the two compartments in the rucksack and adds its integer value to 'tot'
    for rucksack in x:
        compartment_1, compartment_2 = set(
            rucksack[:len(rucksack)//2]), set(rucksack[len(rucksack)//2:])

        a = compartment_1 & compartment_2
        b = list(a)[0]  # common letter
        c = dic1[b]  # integer value of common letter

        tot += c

    print(f'The sum of the priorities of common item types between all compartments is: {tot}')


'''part 2'''
with open('day3in.txt', 'r') as file:
    x = file.read().splitlines()

    tot = 0
    
    # finds the common item between each triplet of elves and adds its integer value to 'tot'
    for i in range(0, len(x), 3):
    
        elf0 = set(x[i])
        elf1 = set(x[i+1])
        elf2 = set(x[i+2])
    
        a = elf0 & elf1 & elf2
        b = list(a)[0] # common letter
        c = dic1[b]  # integer value of common letter
    
        tot += c
    
    print(f'The sum of the priorities of common item types between all elf triplets is: {tot}')
