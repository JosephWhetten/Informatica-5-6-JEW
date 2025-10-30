def main():

    while True:
        try:
            num = int(input("Enter a positive integer: "))
            break
        except ValueError:
            print("Only accepts Integers")
    print(factorial(num))

def factorial(num):
    if num < 0:
        raise ValueError("Does not accept negative integers")
    
    new_num = 1
    for i in range(2, num + 1):
        new_num = new_num * i
    return new_num

main()