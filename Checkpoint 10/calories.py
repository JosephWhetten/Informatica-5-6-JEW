calories = {
    "Milk": 73,
    "Chicken Breast": 101,
    "Greek Yogurt": 130,
    "Large Egg": 75,
    "Cream Cheese": 51,
    "Peanuts": 166,
    "Pinto Beans": 122,
    "Watermelon": 11,
    "Brocoli": 7,
    "Instant Oatmeal": 77
}

print(list(calories.keys()))
food = input("Enter in two foods in the above list, separated by a comma: ").split(", ")
while True:
    try:
        if (food[0] == "Milk" and food[1] == "Watermelon") or (food[0] == "Watermelon" and food[1] == "Milk"):
            raise ValueError("You can't mix Milk and Watermelon!")
        else:
            cal = calories[food[0]] + calories[food[1]]
            print(cal)
            break
    except KeyError:
        food = input("Invalid Input, try again: ").split(", ")