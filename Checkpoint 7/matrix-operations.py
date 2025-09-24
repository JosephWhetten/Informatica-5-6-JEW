def main():

    matrix = [[1,2,3,4],[4,5,6,7],[7,8,9,9],[0,0,6,1]]
    for row in matrix:
        print(row)
    sum_row(matrix[int(input("Enter the row you want to sum = "))-1])
    sum_column(int(input("Enter the column you want to sum = "))-1,matrix)
    change(input("What element do you want to change? (x,y) = "),matrix)

def sum_row(row):
    print(sum(row))

def sum_column(column,matrix):
    column_sum = 0
    for row in matrix:
        column_sum += row[column]
    print(column_sum)

def change(element,matrix):
    for row in matrix(list(element.replace(",","").split())[0]):
        print(row)

main()