def main():
    
    name = input("What is your name? ").strip().title()
    coin = int(input("A coke costs 50 cents, enter a coin: "))
    test(coin)
    total = 0
    cost = 50

    while total < cost:
        total += coin
        print(f"Total: ${total}")
        if total < cost:
            coin = int(input("Enter another coin: "))
            test(coin)
        
    print(f"Your change is ${total - cost} cents. Here's a coke for {name}")


def test(x):
    while x != 25 or x != 10 or x != 5:
        x = int(input("We only accept 25, 10, or 5, enter a coin: "))
    return x

main()