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
number_of_games = int(input("How many games do you want to play? "))
moves = ['paper', 'scissors', 'rock']

human_counter = 0
computer_counter = 0
for i in range(number_of_games):
	computer_move = random.choice(moves)
	human_move = input("What is your next move? scissors, paper or rock? ").lower()

	if (human_move in moves) == False:
		human_move = input("That was incorrect. What is your next move? scissors, paper or rock? ").lower()

	print("Computer played: " + computer_move)
	time.sleep(0.1)

	print("Human played: " + human_move)
	time.sleep(0.1)

	if computer_move == "paper" and human_move == "scissors":
		print("Human won the round!")
		human_counter += 1
	elif computer_move == "paper" and human_move == "rock":
		print("Computer won the round!")
		computer_counter += 1
	elif computer_move == "scissors" and human_move == "rock":
		print("Human won the round!")
		human_counter += 1
	elif computer_move == "scissors" and human_move == "paper":
		print("Computer won the round!")
		computer_counter += 1
	elif computer_move == "rock" and human_move == "paper":
		print("Human won the round!")
		human_counter += 1
	elif computer_move == "rock" and human_move == "scissors":
		print("Computer won the round!")
		computer_counter += 1
	else:
		print("Both played the same move")

print("GAME OVER!")
print("Human won " + str(human_counter) + " games")
print("Computer won " + str(computer_counter) + " games")

if computer_counter > human_counter:
	winner = "Computer"
else:
	winner = "Human"

print(winner + " is the winner!!")

