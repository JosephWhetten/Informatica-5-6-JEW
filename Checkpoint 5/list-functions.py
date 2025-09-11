my_list = [5,2,3,1,4]
my_list2 = ["a","b","c"]

greatest = max(my_list)   #max() finds the greatest value
print("The greatest number of the list is:",greatest)

smallest = min(my_list)   #min() finds the smallest value
print("The smallest number of the list is:",smallest)

list_sum = sum(my_list)   #sum() finds the sum of the list
print("The sum of all the number in the list is:",list_sum)

list_length = len(my_list)   #len() finds the length of the list
print("This list has",list_length,"elements")

in_order = sorted(my_list)
print("The list in order is:",in_order)

def filter_price(price):
    if price < 400:
        return True
    else:
        return False

item_price = [230, 400, 450, 350, 370]
filtered_price = filter(filter_price, item_price)
print(list(filtered_price))