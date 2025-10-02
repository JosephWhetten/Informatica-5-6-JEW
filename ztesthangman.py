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
    print(f"{len(word)}")
    hidden_word = "_"
    blank = list(hidden_word*len(word))
    print(blank)
    listword = []
    for element in word:
        listword.append(element)
    print(listword)
    i = 0
    while i < len(word):
        guess = input("Type a letter: ")
        if guess in listword:
            
            c = 0
            if c < listword.count(guess):
                blank.pop(listword.index(guess))
                blank.insert(listword.index(guess),guess)
                listword.insert(listword.index(guess),"_")
                listword.pop(listword.index(guess))
            print(blank)
            print(listword)
            i += 1
            

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