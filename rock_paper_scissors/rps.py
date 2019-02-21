#!/usr/bin/python

# returns all possible plays of r-p-s
# n = number of  plays per round
# output should be list of lists containing strings, each inner list should be equal to length of input n

# n = 1 [["rock"], ["paper"], ["scissors"]]
# n = 2 [['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'],
# ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'],
# ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]
# n = 3 = 27
# 3^n
# input n is number of plays
# have a list that all possibilities can hold
# append all plays in a list
# define possibilities
# define base case, so that if a condition is met, exit recursion
# helper function that will execute if condition is not met

import sys


def rock_paper_scissors(n):
    # options of r,p,s
    options = ['rock', 'paper', 'scissors']
    # total list of possibilities
    possibilities = []
    print(f"possibilities: {possibilities}")
    #

    def play_choice(play, roundNum):
        if roundNum == 0:
            possibilities.append(play)
            return
        for option in options:
            play_choice(play + [option], roundNum - 1)

    play_choice([], n)
    return possibilities

    #
    # if n == 0:
    #     return possibilities

    # choice_arr = play_choice(n, [], options)
    # print(f"choice arr: {choice_arr}")
    # possibilities.append(choice_arr)
    # print(f"possibilities: {possibilities}")
    # rock_paper_scissors(n-1)
    # rock_paper_scissors(n-1)


# def play_choice(rounds_left, choice, options):
#     if rounds_left == 0:
#         return choice
#     for option in options:
#         # print(option)
#         # choice.append([option]+choice)
#         play_choice(rounds_left-1, [option]+choice, options)
#         print(choice)


results = rock_paper_scissors(3)
print(results)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
