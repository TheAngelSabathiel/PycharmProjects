# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")

greet_with(location = "Pasay", name = "Xander")


def calculate_love_score(name1, name2):
    true = 0
    love = 0
    true_list = ["T", "R", "U", "E", "t", "r", "u", "e"]
    love_list = ["L", "O", "V", "E", "l", "o", "v", "e"]
    for x in range(len(name1)):
        for y in true_list:
            if name1[x] == y:
                true += 1
    for x in range(len(name2)):
        for y in true_list:
            if name2[x] == y:
                true += 1

    for x in range(len(name1)):
        for y in love_list:
            if name1[x] == y:
                love += 1
    for x in range(len(name2)):
        for y in love_list:
            if name2[x] == y:
                love += 1
    love_score = true * 10 + love
    print(love_score)

calculate_love_score("Kanye West", "Kim Kardashian")