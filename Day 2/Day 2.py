# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 13:11:42 2022

@author: Noa
"""


'''Part 1'''
with open('day2in.txt', 'r') as file:
    x = file.read().splitlines() # list of all games played

    dic1 = {'A X': 3, 'A Y': 6, 'A Z': 0, 
            'B X': 0, 'B Y': 3, 'B Z': 6,
            'C X': 6, 'C Y': 0, 'C Z': 3}

    game_scores = []

    # gets the net score of the game and adds it to 'game_scores'
    for game in x:
        if game[2] == 'X':
            shape_score = 1
        if game[2] == 'Y':
            shape_score = 2
        if game[2] == 'Z':
            shape_score = 3

        outcome_score = dic1[game]
        game_score = shape_score + outcome_score
        game_scores.append(game_score)

    print(f'The total score for strategy 1 would be: {sum(game_scores)}')


'''part 2'''
with open('day2in.txt', 'r') as file:
    x = file.read().splitlines()  # list of all games played

    dic2 = {'A X': 3, 'A Y': 1, 'A Z': 2,
            'B X': 1, 'B Y': 2, 'B Z': 3,
            'C X': 2, 'C Y': 3, 'C Z': 1}

    game_scores = []

    # gets the net score of the game and adds it to 'game_scores'
    for game in x:
        if game[2] == 'X':
            shape_score = 0
        if game[2] == 'Y':
            shape_score = 3
        if game[2] == 'Z':
            shape_score = 6

        outcome_score = dic2[game]
        game_score = shape_score + outcome_score
        game_scores.append(game_score)

    print(f'The total score for strategy 2 would be: {sum(game_scores)}')


