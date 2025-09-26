birthdays = {
    "Alyssa": "June 20",
    "Gabriel T": "Dec 27",
    "Gabriel F": "July 28"
}


name = input("Enter a name: ").title()
while name != "":
    if name in birthdays:
        print(f"{name} was born on {birthdays[name]}")
    else:
        new_birthday = input(f"We can't find that name, what is the birthday of {name}? ").title()
        birthdays[name] = new_birthday
        print("The new birthday has been added")
    name = input("Enter a name: ").title()
print(birthdays)
with open("birthdays.txt", "w") as file:
    for day in birthdays:
        file.write(f"{day} born on {birthdays[day]}\n")