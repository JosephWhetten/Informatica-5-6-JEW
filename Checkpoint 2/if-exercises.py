def main():


    abs = int(input("Write a number: "))
    if abs < 0:
        abs = abs * -1
    print(f"{abs}")

    x = int(input("Give me the value of x: "))
    y = int(input("Give me the value of y: "))
    oper = input("Give me an operation: ")
    if oper == "+":
        num = x + y
    if oper == "-":
        num = x - y
    if oper == "/":
        num = x / y
    if oper == "*":
        num = x * y
    print(f"{num}")

    arith = input("Give me an arithmetic equation: ").split()
    if arith[1] == "+":
        result = int(arith[0]) + int(arith[2])
    if arith[1] == "-":
        result = int(arith[0]) - int(arith[2])
    if arith[1] == "/":
        result = int(arith[0]) / int(arith[2])
    if arith[1] == "*":
        result = int(arith[0]) * int(arith[2])

    print(f"{float(result):.1f}")

main()