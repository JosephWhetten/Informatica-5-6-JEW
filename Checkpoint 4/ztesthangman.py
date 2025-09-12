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
    i = 0
    while i < len(word):
        print(word[i])
        i += 1
    hidden_word = "_"
    blank_word = hidden_word*len(word)
    x = 0
    while x < len(word):
        guess = input("Guess = ")
        if guess in word:
            word.remove[word.find[guess]]
            word.insert[word.find[guess],guess]
            print(blank_word)
main()