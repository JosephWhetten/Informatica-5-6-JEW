def main():

    message = input("Type in a message to cipher = ")
    encode_message(message)

def encode_message(code):
    plain = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"
    i = 0
    while i < len(code):
        print(f"{plain[cipher.find(code[i])]}", end="")
        i += 1
        if i % 5 == 0:
            print(" ", end="")
    print("")

main()