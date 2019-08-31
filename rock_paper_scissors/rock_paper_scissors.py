import random


# Gets the players choice.
player_choice = input("Rock, paper, or scissors? ").lower()
while player_choice not in ["rock", "paper", "scissors"]:
    player_choice = input("You must enter either: rock, paper, or scissors. ").lower()

# Randomly selects the computer's option.
computer_choice = random.randint(1,3)
if computer_choice == 1:
    computer_choice = "rock"
elif computer_choice == 2:
    computer_choice = "paper"
else:
    computer_choice = "scissors"

# Compares player_choice to computer_choice and prints out a win or loss.
if computer_choice == player_choice:
    print("You tied!")
elif computer_choice == "rock" and player_choice == "paper":
    print("You win!")
elif computer_choice == "paper" and player_choice == "scissors":
    print("You win!")
elif computer_choice == "scissors" and player_choice == "rock":
    print("You win!")
else:
    print("You lose!")