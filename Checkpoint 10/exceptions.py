# SyntaxError
# print("Hello, world)



# def spam(divided_by):
#     try:
#         return 42 / divided_by
#     except ZeroDivisionError:
#         print("Error: Invalid argument")

# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not a number")
    else:
        print(f"x is equal to {x}")
        break


def read_small_integer():
    while True:
        try:
            input_str = input("Please type in an integer: ")
            number = int(input_str)
            if number < 100 and number >= 0:
                return number
        except ValueError:
            pass
        print("This input is invalid")
        
number = read_small_integer()
print(number, "to the power of three is", number**3)