money = int(0)
while money < 100:
    hello = input("Can I get a greeting? ").strip().lower()
    if hello == "hello":
        print(f"${money}")
    elif hello.startswith("h") == True:
        money = money + 20
        print(f"${money}")
    else:
        money = money + 100
        print(f"Your total is ${money}")