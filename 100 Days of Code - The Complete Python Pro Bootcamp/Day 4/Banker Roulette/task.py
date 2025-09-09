friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
import random
print("Who will pay the food?")
x = random.randint(0,4)
print(f"The one who will pay is {friends[x]}.")

#or random.choice(friends)