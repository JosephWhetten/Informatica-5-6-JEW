#    ___ 
#    |  |
#    O  |
#   /|\ |
#   / \ |
#  _____|___

#    ___ 
#    |  |
#    O  |
#   /|\ |
#   /   |
#  _____|___

#    ___ 
#    |  |
#    O  |
#   /|\ |
#       |
#  _____|___

#    ___ 
#    |  |
#    O  |
#   /|  |
#       |
#  _____|___

#    ___ 
#    |  |
#    O  |
#    |  |
#       |
#  _____|___

#    ___ 
#    |  |
#    O  |
#       |
#       |
#  _____|___

#    ___ 
#    |  |
#       |
#       |
#       |
#  _____|___

def main():

    word = input("What is the word going to be? = ")

    hidden_word = "_"
    blank = list(hidden_word*len(word))
    print(blank)

    realword = []
    for element in word:
        realword.append(element)
    print(realword)
    
    i = 0
    while i < len(word):
        guess = input("Type a letter: ")
        if guess in realword:
            
            i = 0
            while i < realword.count(guess):
                blank.pop(realword.index(guess))
                blank.insert(realword.index(guess),guess)
                realword.insert(realword.index(guess),"_")
                realword.pop(realword.index(guess))
                i += 1
            print(blank)
            print(realword)
            
            

    # for letter in word:
    #     guess = input("Type in a letter = ")
    #     if guess in word:
    #         c = 0
    #         while c < word.count(guess):
    #             blank.pop(word.index(guess))
    #             list(word).pop(word.index(guess))


    # i = 0
    # while i < len(word):
    #     guess = input("Type in a letter =  ")
    #     if guess in word:
    #         blank.pop(word.index(guess))
    #         blank.insert(word.index(guess),guess)
    #         print(blank)
    #         i += 1

main()