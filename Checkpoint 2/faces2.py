def main():

    x = input("Put an emoji face\n").strip()
    print(f"This is how it should look like = ", convert(x))

def convert(face):
    return face.replace(":)", "😊").replace(":(", "😞")

main()