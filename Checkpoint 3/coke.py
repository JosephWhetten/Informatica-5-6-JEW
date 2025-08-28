def main():
    
    name = input("What is your name? ").strip().title()
    #coin = int(input("A coke costs 50 cents, enter a coin: "))
    #test(coin)
    total = 0
    cost = 50

    while total < cost:
        coin = int(input("A coke costs $50 cents, insert a coin: "))
        #test1(coin)
        if coin == 25 or coin == 10 or coin == 5:
            total += coin
        else:
            while True:
                if coin == 25 or coin == 10 or coin == 5:
                    total += coin
                    break
                else:
                    coin = int(input("We only accept 25, 10, or 5, enter a coin: "))
        print(f"Total: ${total}")
        
    print(f"Your change is ${total - cost} cents. Here's a coke for {name}")


def test1(x):
    while x != 25 or x != 10 or x != 5:
        x = int(input("We only accept 25, 10 or 5, insert a coin: "))

def test(x):
    while True:
        if x == 25 or x == 10 or x == 5:
            break
        else:
            x = int(input("We only accept 25, 10, or 5, enter a coin: "))

main()