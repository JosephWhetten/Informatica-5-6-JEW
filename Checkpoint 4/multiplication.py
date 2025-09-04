def main():

    num = input("Enter in a positive integer = ")
    while True:
        if num.isdigit() == True and int(num) > 0:
            num = int(num)
            break
        else:
            num = input("I said enter in a positive integer = ")
    multiplication_table(num)

def multiplication_table(y):
    x = 1
    i = 1
    while i <= y:
        while x <= y:
            print(f"{i} x {x} = {i*x}")
            x += 1
        i += 1
        x = 1

main()