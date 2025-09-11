def main():
    list = [10,3,5,7,2,6,8,1,4,9]
    print("The length of the list is:",length(list))
    print("The mean of the list is:",mean(list))
    print("The range of the list is",range_of_list(list))
    new_list(list)
    print("The program has ended")

def length(list_len):
    return len(list_len)

def mean(list_mean):
    return (sum(list_mean)/len(list_mean))

def range_of_list(range):
    return (max(range)-min(range))

def new_list(new):
    num = int(input("Enter a new integer to add = "))
    while num != 0:
        new.append(num)
        print(new)
        print(sorted(new))
        num = int(input("Enter a new integer to add = "))

main()

