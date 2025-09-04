def main():

    message = input("Type in a message to cipher = ")
    encode_message(message)

def encode_message(code):
    plain = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"
    i = 0
    new_message = ""
    while i < len(code):
        if code[i] in plain:
            cipher_index = plain.find(code[i])
            new_message += cipher[cipher_index]
            i += 1
        elif code[i].isdigit():
            new_message += code[i]
            i += 1
        else:
            i += 1
        if len(new_message) % 5 == 0:
            new_message += " "
    print(f"{new_message}")

main()