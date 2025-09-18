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
    print(list(word))
    i = 0
    while i < len(word):
        guess = input("Type in a letter =  ")
        if guess in word:
            c = 0
            # while c < list(word).count(guess):

            blank.pop(word.index(guess))
            blank.insert(word.index(guess),guess)
            print(blank)
            i += 1

main()