# input_string = input("Enter in a string = ")
# print(input_string)
# print("-"*len(input_string))

# input_string = input("Enter in a string = ")
# print(input_string[0])
# print(input_string[1])
# print(input_string[3],"\n")

input_string = input("Enter in a string = ")
i = 0
while i < len(input_string):
    print(input_string[i])
    i += 1

# print("\n",input_string[0:3])

# input_string = input("Enter in a string = ")
# if "x" in input_string:
#     print("The letter x is in the string")
# else: print("The letter x is not in the string")

input_string = input("Enter in a string = ")
print(input_string.find("x"))