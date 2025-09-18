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
    blank_word = hidden_word*len(word)
    print(blank_word)

main()