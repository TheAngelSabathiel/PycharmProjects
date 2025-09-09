import random
from game_data import data
from art import logo
from art import vs

def ask_if_wanna_play():
    check = "y"
    ask_play = input("Do you want to continue playing? Press 'y' to continue.").lower()
    if ask_play == check:
        return True
    else:
        return False

def game():
    is_game_over = False
    score = 0
    first_item = {}
    second_item = {}
    while not is_game_over:
        if score != 0:
            print(f"Score: {score}")
        input("Enter any key to continue.\n") #put dummy variable if it does not work
        if not first_item:
            first_item = random.choice(data)
        second_item = random.choice(data)
        print(f"{first_item["name"]} has {first_item["follower_count"]} million "
              f"followers on Instagram. \n{first_item["description"]} from {first_item["country"]}.")
        print(vs)
        print(f"{second_item["name"]} has ____________ followers. \n{second_item["description"]} from {second_item["country"]}.")
        if first_item["follower_count"] < second_item["follower_count"]:
            correct = "higher"
        elif first_item["follower_count"] > second_item["follower_count"]:
            correct = "lower"
        else:
            correct = "equal"
        while True:
            try:
                guess = input("\nHigher or Lower or Equal?\n").lower()
                if guess != "higher" and guess != "lower" and guess != "equal":
                    print("Invalid input. Please guess among 'Higher', 'Lower', or 'Equal' only.")
                elif guess == correct:
                    score +=1
                    print("\nCorrect.")
                    first_item = second_item
                    break
                else:
                    print(f"\nWrong. Game Over. Your final score is {score}.")
                    is_game_over = True
                    break
            except ValueError:
                print("Invalid input or Error. Please guess among 'Higher', 'Lower', or 'Equal' only.")

wanna_play = True

while wanna_play:
    print(logo)
    game()
    wanna_play = ask_if_wanna_play()
print("Thank you for playing!")