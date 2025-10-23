import random

letter_values = {
"A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
"D": 2, "G": 2,
"B": 3, "C": 3, "M": 3, "P": 3,
"F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
"K": 5,
"J": 8, "X": 8,
"Q": 10, "Z": 10,
}

turn_letters = []
points = 0

for random_letter in range(13):
    random_index = random.randint(0, len(letter_values) - 1)
    letter_list = list(letter_values.keys())
    new_letter = letter_list[random_index]
    turn_letters.append(new_letter)

print("Welcome to Scrabble!")
print(f"Your letters are:")
print(turn_letters)

while len(turn_letters) > 0:
    print("Type your word (blank to finish the game):")
    word_attempt = input().upper()
    if word_attempt == "":
        break
    if set(word_attempt).issubset(set(turn_letters)):
        for l in range(len(word_attempt)):
            points += letter_values[word_attempt[l]]
            turn_letters.remove(word_attempt[l])
    else:
        print("Please type a word that uses your letters.")

print("Points:", points)

if len(turn_letters) > 0:
    print("Remaining letters:")
    print(turn_letters)
else:
    print("No remaining characters.")

print("GAME OVER")
print("Total points:", points)