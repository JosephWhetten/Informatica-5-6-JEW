gas = input("Enter your remaining gas in fraction (x/y): ").split("/")
while True:
    try:
        num = int(gas[0])
        den = int(gas[1])
        if num > den:
            gas = input("Invalid input, try again: ").split("/")
        elif num/den*100 <= 1:
            print("E")
            break
        elif num/den*100 >= 99:
            print("F")
            break
        else:
            print(f"{(int(gas[0]) / int(gas[1]) * 100):.0f}%")
            break
    except (ValueError, ZeroDivisionError):
        gas = input("Invalid input, try again: ")