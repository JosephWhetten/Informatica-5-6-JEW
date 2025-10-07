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
while i < 13:
    user_letters.append(list(alphabet.keys())[random.randint(0,25)])
    i += 1
print(user_letters)

word = input("Enter a word with these letters: ").upper()

for check_letter in word:
    if check_letter not in user_letters:
        print(f"The letter {check_letter} is not available")

with open("scrabble-words.txt" ,"r") as file:
    lines = file.readlines()
dictwords = []
for line in lines:
    dictwords.append(line.replace("\n",""))
if word.lower() in dictwords:
    print("Valid")
else: print("Not ok")

total = 0
for value in word:
    total += alphabet[value]
print(total)