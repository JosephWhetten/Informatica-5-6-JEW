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

hangm0 ='''
                ___ 
                |  |
                   |
                   |
                   |
              _____|___'''

def main():

    word = input("What is the word going to be? = ")

    hidden_word = "_"
    blank = list(hidden_word*len(word))
    print(blank)

    testword = []
    for element in word:
        testword.append(element)
    print(testword)
    
    print(hangm0)
    wrong_letter = []
    i = 0
    while i < len(word):
        guess = input("Type a letter: ")
        if len(guess) > 1:
            print("Only enter one letter")
            print(type(guess))
        elif guess in blank:
            print("You already used this letter")
        elif guess in testword:
            
            for count in range(0, testword.count(guess)):
                blank.pop(testword.index(guess))
                blank.insert(testword.index(guess),guess)
                testword.insert(testword.index(guess),"_")
                testword.pop(testword.index(guess))
                i += 1
            print(blank)
            print(testword)
        else:
            wrong_letter.append(guess)
            print(wrong_letter)
            print(len(wrong_letter))
            
main()