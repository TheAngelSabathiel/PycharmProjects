programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}


#defining
programming_dictionary["Bug"] = "An animal species attacking the computer."
#looping
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
#clearing data
programming_dictionary["Bug"] = ""
print(programming_dictionary["Bug"])

#empty a dictionary
programming_dictionary = {}
print(programming_dictionary)