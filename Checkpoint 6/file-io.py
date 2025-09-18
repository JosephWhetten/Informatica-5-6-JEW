# names = []

# for i in range(3):
#     names.append(input("What's your name? "))      Adds names in a list using a for loop in a range from 0-2, then orders the list

# for name in sorted(names):
#     print(f"Hello {name}")


# name = input("What's your name? ")
# file = open("names.txt","a")          The "a" tells the computer we want to append something, "w" means write
# file.write(f"\n{name}")               Creates a new file called names.txt and writes in it and closes it
# file.close


# with open("names.txt.", "a") as file:                 Does the same thing but with less lines
#     file.write(f"{input("What's your name? ")}")

with open("names.txt", "r") as file:
    lines = file.readlines()

for line in sorted(lines):
    print(f"Hello {line.rstrip()}")