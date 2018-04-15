#!/usr/bin/python

import time
import random

print("-------------------------------------------------------")
print ("Welcome to Human vs. Computer in Scissors, Paper, Rock!")
print("-------------------------------------------------------")
print("Moves: choose scissors, paper or rock by typing in your selection.")
print("Rules: scissors cuts paper, paper covers rock and rock crushes scissors.")
print("Good luck!")
print("------------\n")

name = input("What is your name? ")
print("Hello " + name.lower())

moves = ['paper', 'scissors', 'rock']
computer_move = random.choice(moves)
human_move = input("What is your next move? scissors, paper or rock? ")

print("Computer played: " + computer_move)
time.sleep(0.1)

print("Human played: " + human_move)
time.sleep(0.1)

if computer_move == "paper" and human_move == "scissors":
	print("Human won the round!")
elif computer_move == "paper" and human_move == "rock":
	print("Computer won the round!")
elif computer_move == "scissors" and human_move == "rock":
	print("Human won the round!")
elif computer_move == "scissors" and human_move == "paper":
	print("Computer won the round!")
elif computer_move == "rock" and human_move == "paper":
	print("Human won the round!")
elif computer_move == "rock" and human_move == "scissors":
	print("Computer won the round!")
else:
	print("Both played the same move")