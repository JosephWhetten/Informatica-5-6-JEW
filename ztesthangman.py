#     ___ 
#    |  |
#    O  |
#   /|\ |
#   / \ |
#  _____|___

#     ___ 
#    |  |
#    O  |
#   /|\ |
#   /   |
#  _____|___

#     ___ 
#    |  |
#    O  |
#   /|\ |
#       |
#  _____|___

#     ___ 
#    |  |
#    O  |
#   /|  |
#       |
#  _____|___

#     ___ 
#    |  |
#    O  |
#    |  |
#       |
#  _____|___

#     ___ 
#    |  |
#    O  |
#       |
#       |
#  _____|___

hangman0 ='''
          ___ 
         |  |
            |
            |
            |
       _____|___'''

import getpass

def main():

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    word = getpass.getpass("What is the word going to be? = ")
    print(len(alphabet))

    hidden_word = "_"
    correct_guess = list(hidden_word*len(word))
    print(correct_guess)

    testword = []
    for element in word:
        testword.append(element)
    print(testword)
    
    print(hangman0)
    
    wrong_guess = []
    i = 0
    while i < len(word):
        guess = input("Type a letter: ")
        
        # Test if it's not in the alphabet
        if guess not in alphabet:
            print("Invalid Input")
            
        elif guess in correct_guess or guess in wrong_guess:
            print("You already used this letter")
        # Test if you already guessed it
        
        elif guess in testword:
            
            for count in range(0, testword.count(guess)):
                correct_guess.pop(testword.index(guess))
                correct_guess.insert(testword.index(guess),guess)
                testword.insert(testword.index(guess),"_")
                testword.pop(testword.index(guess))
                i += 1
            print(correct_guess)
            print(testword)
        else:
            wrong_guess.append(guess)
            print(wrong_guess)
            print(len(wrong_guess))
            
main()