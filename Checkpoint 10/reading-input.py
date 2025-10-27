def main():
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)

def read_input(text, x, y): # Insert missing parameters
    num = input(f"{text}")
    while True:
        try:
            if int(num) >= x and int(num) <= y:
                return num
            else:
                num = input("Please type in another number: ")
        except ValueError:
            num = input(f"This input is invalid\n{text}")

    # Complete the program here

main()