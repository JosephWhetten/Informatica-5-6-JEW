# names = ["Bob", "Alex", "Kevin"]                                          # List with strings
# names.append("Joseph")
# for name in sorted(names):
#     print(name)

# measurements = [-2.5, 1.1, 7.5]
# mean = sum(measurements) / len(measurements)                              # List with floats
# print("The mean is:",mean)


super_list = [[5,2,3],[4,1],[2,2,5,1]]
print(super_list[1][0])

grades = [["Shakira",8,"D"],["Melissa",0,"C"],["Shensi",10,"A"]]            # List within lists
for student in grades:
    name = student[0]
    grade = student[1]
    group = student[2]
    print(f"{name} from group {group} got a {grade}")

# Matrices
matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Print rows
for row in matrix:
    print(row)
for column in matrix:
    print(column[0],end=" ")
print("")
for column in matrix:
    print(column[1],end=" ")
print("")
for column in matrix:
    print(column[2],end=" ")
print("")