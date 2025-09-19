def main():

    choice = int(input("Option 1: Enter a list of numbers seperated by commas\nOption 2: Read numbers from a file\nOption choice = "))
    if choice == 1:
        numbers = input("Enter the numbers = ")
        write_numbers(numbers, "largest.txt")
        find_largest(numbers)
    if choice == 2:
        filename = input("Enter the file name = ")
        read_numbers()
        find_largest()

def write_numbers(num, name):
    file = open(name,"w")
    for i in list(num.replace(",", "").split()):     #Gets the list of the numbers the user put in, removes the commas, then splits it 
        file.write(f"{i}\n")                         #Writes into the file that was already created
    file.close()
    # with open(name, "w") as file:
    #     file.write(list(num.replace(",", "").split()))
    #print(list(num.replace(",","").split()))

def find_largest(num):
    print(max(list(num.replace(",", "").split())))

main()