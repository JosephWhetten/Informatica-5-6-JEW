hangman6 ='''
        ___ 
        |  |
        O  |
       /|\ |
       / \ |
      _____|___'''

hangman5 ='''
        ___ 
        |  |
        O  |
       /|\ |
       /   |
      _____|___'''

hangman4 ='''
        ___ 
        |  |
        O  |
       /|\ |
           |
      _____|___'''

hangman3 ='''
        ___ 
        |  |
        O  |
       /|  |
           |
      _____|___'''

hangman2 ='''
        ___ 
        |  |
        O  |
        |  |
           |
      _____|___'''

hangman1 ='''
        ___ 
        |  |
        O  |
           |
           |
      _____|___'''

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

    hidden_word = "_"
    correct_guess = list(hidden_word*len(word))
    correct_guess = []
    for letter in word:
        if letter == " ":
            correct_guess.append(" ")
        else: correct_guess.append(hidden_word)
    print(correct_guess)

    testword = []
    for element in word:
        testword.append(element)
    
    wrong_guess = []
    i = 0
    while i < len(word):
        if len(wrong_guess) == 0:
            print(hangman0,end="\n\t")
        elif len(wrong_guess) == 1:
            print(hangman1,end="\n\t")
        elif len(wrong_guess) == 2:
            print(hangman2,end="\n\t")
        elif len(wrong_guess) == 3:
            print(hangman3,end="\n\t")
        elif len(wrong_guess) == 4:
            print(hangman4,end="\n\t")
        elif len(wrong_guess) == 5:
            print(hangman5,end="\n\t")
        elif len(wrong_guess) == 6:
            print(hangman6,end="\n\t")
            print("You died!")
            break

        for letter in wrong_guess:
            print(letter,end =" ")
        print("")
        
        for letter in correct_guess:
            print(letter,end=" ")

        guess = input("\nType a letter: ")
        
        # Test if it's not in the alphabet
        if guess not in alphabet:
            print("Invalid Input")
            
        elif guess in correct_guess or guess in wrong_guess:
            print("You already used this letter")
        # Test if you already guessed it
        
        elif guess in testword:
            # alphabet.remove(guess)
            
            for count in range(0, testword.count(guess)):
                correct_guess.pop(testword.index(guess))
                correct_guess.insert(testword.index(guess),guess)
                testword.insert(testword.index(guess),"_")
                testword.pop(testword.index(guess))
                i += 1
        else:
            wrong_guess.append(guess)
    for letter in correct_guess:
        print(letter,end=" ")
    print("\nYou finished the game")
            
main()