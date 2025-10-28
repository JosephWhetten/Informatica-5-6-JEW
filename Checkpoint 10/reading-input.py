def main():
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)

def read_input(text, x, y): # Insert missing parameters
    while True:
        try:
            num = input(f"{text}")
            if x <= int(num) <= y:
                return num
            else:
                print(f"Please type a number between {x} and {y}")
        except ValueError:
            print(f"This input is invalid")

    # Complete the program here

main()