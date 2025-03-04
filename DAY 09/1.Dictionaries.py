programming_dictionary = {
    "bug": "an error in a program that prevents the program from running as expected.",
    "function": "a piece of code that you can easily call over and over again.",
    "loop": "the action of doing something over and over again."
}

print(programming_dictionary["loop"])


#loop through a dictionary
for thing in programming_dictionary:
    print(thing)
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


#wipe an exsisting dictionary
empty_dictionary = {}
programming_dictionary = empty_dictionary
print(programming_dictionary)


#edit item in dictionary
programming_dictionary["bug"]= "shreya"
print(programming_dictionary)

