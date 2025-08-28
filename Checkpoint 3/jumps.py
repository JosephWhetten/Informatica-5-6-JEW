def main():

    num = input("Enter a limit number: ")
    test(num)
    step = int(input("Enter a step number: "))
    i = step
 

    while i < int(num):
        if step == 0:
            step = int(input("Enter another number that's not 0: "))
        else: print(f"{i}")
        i += step

    print("Thank you for your cooperation")

def test(x):
    while True:
        if x.isdigit():
            return int(x)
        else: 
            x = input("Enter a limit NUMBER: ")

main()

