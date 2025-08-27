int = int(input("Enter an integer: "))
if int == 0:
    print("Dummy")
elif int == 3:
    print("Prime Fizz")
elif int == 5:
    print("Prime Buzz")
elif int % 3 == 0 and int % 5 == 0:
    print("FizzBuzz")
elif int % 3 == 0:
    print("Fizz")
elif int % 5 == 0:
    print("Buzz")
elif int == 2:
    print("Prime")
elif not (int%2==0 or int%3==0 or int%5==0):
    print("Prime")
else: print(f"{int}")