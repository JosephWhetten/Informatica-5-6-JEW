#try:
while True:
    try:
        gas = input("Enter your remaining gas in fraction (x/y): ").split("/")
        gas[0] = int(gas[0])
        gas[1] = int(gas[1])
    except ValueError:
        print("ValueError")
    elif gas[0] > gas[1]:
       print("Invalid input, try again")

if gas[0]/gas[1]*100 < 1:
    print("E")
    break
elif gas[0]/gas[1]*100 > 99:
    print("F")
    


print(f"{(int(gas[0]) / int(gas[1]) * 100):.0f}%")