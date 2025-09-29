dictionary = {
    "color": "blue",
    "age": 17
}

# Values
print(dictionary.values())
for v in dictionary.values():
    print(v)

# Keys
print(dictionary.keys())
for k in dictionary.keys():
    print(k)

# Items
print(dictionary.items())
for i in dictionary.items():
    print(i)

# Print key and value using methods
# to do

# Get
picnic_items = {"apples": 5, "cups": 2}
print(f"I'm bringing {picnic_items.get("cups")} cups")

print(f"I'm bringing {picnic_items.get("eggs", 0)} eggs")       # Since there are no eggs, I set the fallback value to 0

# Setting Default Values
pet_info = {
    "name": "Arrow",
    "age": 3
}

pet_info.setdefault("color", "Brown and white")
pet_info["color"] = "Brown and orange"                          # Adds or modifies a key and value
pet_info.setdefault("color", "Black")                           # There is already a default so it doesn't change anything
print(pet_info)