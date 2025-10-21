def main():
    import random
    alphabet = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }
    user_letters = []
    i = 0
    while i < 13:                                                           # Picks 13 random letters from the alphabet
        user_letters.append(list(alphabet.keys())[random.randint(0,25)])
        i += 1
    print(user_letters)

    word = input("Enter a word with these letters: ").upper()
    score = 0
    while True:
        
        if word != "":                                              # Checks if the input is ENTER
            check_scrabble(word)
            for letter in word:                                     # Removes the letters the user entered
                user_letters.pop(user_letters.index(letter))        
            for value in word:                                      # Adds the value of every letter
                score += alphabet[value]
            print(f"Your total score is: {score}")
            print(f"Remaining letters: \n{user_letters}")
            word = input("Enter a word with the remaining letters, press ENTER to stop: ").upper()
        else: break
    print(f"Thank you for playing! Your final score is {score}")
        
    
def check_scrabble(word):                               # Checks if the word is in the dictionary
    with open("scrabble-words.txt" ,"r") as file:       # Opens the word file of the words in the dictionary of scrabble
        lines = file.readlines()
    dictwords = []
    for line in lines:
        dictwords.append(line.replace("\n",""))
    if word.lower() in dictwords:                       # Reads if the word is in the dictionary
        print("Valid")
    else: 
        word = input("Not valid, try again: ")

main()