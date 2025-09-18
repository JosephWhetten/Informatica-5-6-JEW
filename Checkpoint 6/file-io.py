# names = []

# for i in range(3):
#     names.append(input("What's your name? "))

# for name in sorted(names):
#     print(f"Hello {name}")

name = input("What's your name? ")
file = open("names.txt","a")
file.write(f"\n{name}")
file.close