print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
input1 = input('You\'re on a crossroad. Where do you want to go? Type "left" to go the left'
      'and "right" to go to the right. ').lower()

if input1 == "left":
    input2 = input("You took the path to excellence, wisdom, and treasure. Suddenly, you encountered a bitch."
          " She asked you to do something by the lake. \nWhat do you want to do? Type \"wait\" if you want to"
          " wait or \"swim\" if you want to swim.").lower()
    if input2 == "wait":
        print("The bitch was a monster mermaid. She disintegrated and transported you to the center"
              " of the island. You were led to a room of three colored doors.")
        input3 = input("Which door will you open? Red, Blue, or Yellow? ").lower()
        if input3 == "yellow":
            print("You found the treasure of Nymphia Wind. Congratulations Gay!")
        elif input3 == "red":
            print("You found the door leading to hell. Most gays go to hell, tho, but no treasure. Game Over.")
        elif input3 == "blue":
            print("You found the door of Denali. This just means you lose. Game Over.")
        else:
            print("You opened a non-existent door. Check your spelling and instructions, adult. Game Over.")
    else:
        print("The bitch led you to the Lake of Trap. She sucked the soul out of your weak body. Game Over.")
else:
    print("You're a loser. You went the path to home. You lose. Game Over.")

