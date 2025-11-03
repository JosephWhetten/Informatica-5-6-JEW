# import random
# coin = random.choice(["Heads", "Tails"])
# print(coin)

# number = random.randint(1, 10)
# print(number)

# cards = ["Jack", "Queen", "King", "Ace"]
# random.shuffle(cards)
# for card in cards:
#     print(card)


import statistics
# print(statistics.mean([100,90]))


import sys
# print("Hello, my name is", sys.argv[1])

# # First use cd to go to your Folder (cd "Checkpoint 11")
# # While there, write python, the name of the File and your arguments (python libraries.py Joseph 50 100)
# print(f"The mean between {sys.argv[2]} and {sys.argv[3]} is {statistics.mean([int(sys.argv[2]),int(sys.argv[3])])}")

import cowsay

# To see if there's no arguments
try:
    cowsay.cow("Hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguents")
    sys.exit()

