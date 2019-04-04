#########################################
# Daniel Johnson
# Assignment 4.2
# 3/8/19
#
# Description: This program builds a dictionary from the given text file and then allows the user
# to input a word jumble that will match up to one of the words in the dictionary
#
# Inputs: This program takes a text file as input and a sequence of characters/word scramble as input
#
# Outputs: This outputs a list of possible words for a given string of scrambled letters
#########################################



################################
# Purpose: This function creates
# a dictionary based on a string
# of words
#
# Input: This takes a string of
# words separated by spaces
#
# Return/Output: This returns
# a dictionary of words
###############################
def build_dict(text):
    word_dict = {}
    text = text.split(" ")
    for x in text:
        temp_str = ''.join(sorted(x.lower()))
        if temp_str in word_dict:
            word_dict[temp_str].append(x)
        else:
            word_dict[temp_str] = [x]
    return word_dict





################################
# Purpose: This function
# unscrambles a string of letters
# and returns a list of possible
# words
#
# Input: This takes a string of
# random characters as input
# along with a dictionary created
# by the build_dict function
#
# Return/Output: This returns
# a list of words
###############################
def unscramble(jumble, dictionary):
    temp_str = ''.join(sorted(jumble.lower()))
    if temp_str in dictionary:
        temp_var = dictionary[temp_str]
        return temp_var
    else:
        return 'Nothing'




#imports words from text file
f = open('Words.txt', 'r')
words = f.read()
f.close()


dictionary = build_dict(words)


#Hardcode test as asked in the assignment prompt
jumble = 'asewes'
print(jumble, "unscrambles to:", unscramble(jumble, dictionary))
jumble = 'enost'
print(jumble, "unscrambles to:", unscramble(jumble, dictionary))
jumble = 'aaabcs'
print(jumble, "unscrambles to:", unscramble(jumble, dictionary))
print()


#repeat
yn = 'yes'
while yn == 'yes' or yn == 'y':
    yn = ''
    jumble = input("Please enter a jumble to solve:")
    print()
    print(jumble, "unscrambles to:", unscramble(jumble, dictionary))
    print()

    while not (yn == "yes" or yn == "y" or yn == "no" or yn =="n"):
        yn = input("Would you like to enter another word? Reply \"Yes\" or \"No\".").lower()
        print()

print("Thanks for using me. Goodbye.")
