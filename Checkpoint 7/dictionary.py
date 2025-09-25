capitals = {
    "Mexico": "Mexico City",
    "Canada": "Dttawa",                 # KEY : VALUE
    "Brazil": "Brasilia",
    # "Canada": "Montreal"    You have to use unique keys
}

capitals["Italy"] = "Rome"          # Appends a new key and value
del capitals["Brazil"]              # Deletes a new key and value
capitals.pop("Canada")              # Does the same thing
# capitals.clear()                  # Clears the list
print(capitals["Mexico"])

# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin"
# }

# for key in students:
#     print(f"{key}: {students[key]}")      Prints the student then the key or the house

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]
for element in students:
    print(f"{element["name"]} of {element["house"]} with {element["patronus"]}")