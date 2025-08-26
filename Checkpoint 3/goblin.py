import random
print("Welcome to the Goblin Game!")
print("(The best game ever)")
player_name = input("What is your name?\n")
print(f"{player_name}, can you find the goblin?")
print("|_||_||_||_||_|")
goblin_position = random.randint(1, 5)
keep_trying = True
while keep_trying:
    guessed_position = int(input("Guess where the goblin is =  "))
    if guessed_position != goblin_position:
        print("Wrong! Try again")
    else:
        print("Correct! Good job")
        keep_trying = False