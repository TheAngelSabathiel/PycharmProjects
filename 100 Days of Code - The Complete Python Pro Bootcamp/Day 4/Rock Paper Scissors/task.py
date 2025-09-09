rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

print("Rock - Paper - Scissors Game")
player_choice = int(input("Can you beat the computer? What do you choose?"
                          " Type 0 for Rock, 1 for Paper, or 2 for Scissors:\n"))
computer_choice = random.randint(0,2)
hand = [rock, paper, scissors]
hand_description = ["Rock", "Paper", "Scissors"]

if 0 <= player_choice <= 2:
    print(f"You chose {hand_description[player_choice]}.")
    print(hand[player_choice])
    print(f"Computer chose {hand_description[computer_choice]}.")
    print(hand[computer_choice])
    if player_choice == computer_choice:
        print("The Game is a draw. Try again.")
    else:
        if player_choice == 0:
            if computer_choice == 1:
                print("You lose. Try again.")
            if computer_choice == 2:
                print("You win. Congratulations.")
        elif player_choice == 1:
            if computer_choice == 0:
                print("You win. Congratulations.")
            elif computer_choice == 2:
                print("You lose. Try again.")
        elif player_choice == 2:
            if computer_choice == 0:
                print("You lose. Try again.")
            elif computer_choice == 1:
                print("You win. Congratulations.")
else:
    print("You typed an invalid value. Try again.")