import random

def guess():
	guess_num = int(input("Input your guess: "))
	if to_guess == guess_num:
		print("Correct.")
		return 11
	elif to_guess < guess_num:
		print("Lower.")
		return 1
	elif to_guess > guess_num:
		print("Higher.")
		return 1
	else:
		print("Wrong input.")
		return 1

print(f"Hello, Welcome to the Number Guessing Game.")
difficulty = input("Choose difficulty. Easy or Hard?\n").lower()

to_guess = random.randint(1,100)
print(to_guess)

if difficulty == "easy":
	lives = 10
elif difficulty == "hard":
	lives = 5
else:
	print(f"You choose the wrong option. Automatically switching to hard mode.")
	lives = 5

while lives > 0:
	lives -= guess()
	if lives > 0:
		print(f"Lives left: {lives} lives")
	else:
		print("Game Over.")