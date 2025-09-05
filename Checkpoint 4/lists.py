independence_stages = ["Inicio","Organizacion","Resistencia","Consumacion"]
print(independence_stages[0])
print(independence_stages[1:3])
print(len(independence_stages))

# List Methos
leaders = []
leaders.append("Miguel Hidalgo")
leaders.append("Vicente Guerrero")
# leaders.extend(independence_stages)  |  Mix lists together
leaders.insert(1,"Jose Maria Morelos")
# leaders.remove("Vicente Guerrero")  | Remove the first match of a specific item
leaders.append("Agustin de Iturbide")
#leaders.pop(1)  | Remove certain indexes
#leaders.clear()  | Clears the list
print(leaders.index("Jose Maria Morelos"))  #Find which index the item is in
#print(leaders.count("Vicente Guerrero"))  | Count how many of the item is in the list
#leaders.sort()  | Sorts in alphabetical order
#leaders.reverse()  | Reverse the order of elements
new_leaders = leaders.copy()

print(new_leaders)
print(leaders)