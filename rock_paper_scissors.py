

import random

#setting condition for replaying
while True:

    #setting player and computer choices
    choices = ("rock", "paper", "scissors")
    #setting computer into selecting randomly
    computer = random.choice(choices)
    #testing for computer choices
    #print(computer)
    player = None

    #setting an exception to entries
    while player not in choices:
        player = input("Enter your selection:[Rock/Paper/Scissors] ").lower()

    # setting game conditions 
    if computer == player:
        print(f"computer: {computer}")
        print(f"player: {player}")
        print("It's a TIE !!!")
    elif player == "rock":
        if computer == "paper":
            print(f"computer: {computer}")
            print(f"player: {player}")
            print("YOU LOSE !!!")
        if computer == "scissors":
            print(f"computer: {computer}")
            print(f"player: {player}")
            print("YOU WIN !!!")
    elif player == "scissors":
        if computer == "rock":
            print(f"computer: {computer}")
            print(f"player: {player}")
            print("YOU LOSE !!!")
        if computer == "paper":
            print(f"computer: {computer}")
            print(f"player: {player}")
            print("YOU WIN !!!")
    elif player == "paper":
        if computer == "scissors":
            print(f"computer: {computer}")
            print(f"player: {player}")
            print("YOU LOSE !!!")
        if computer == "rock":
            print(f"computer: {computer}")
            print(f"player: {player}")
            print("YOU WIN !!!")

    play_again = input("Woud you like to replay: [Yes/No]").lower()
    if play_again != "yes":
        break

print("BYE! Thanks for playing.")