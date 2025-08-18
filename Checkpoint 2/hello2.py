def main():
    name = input("Hello, what's your name?\n").strip().title()
    hello(name)
    hello()

def hello(to="world"):
    print(f"Hello,", to)

main()