def main():

    matrix = [[1,2,3,4],[4,5,6,7],[7,8,9,9],[0,0,6,1]]
    for row in matrix:
        print(row)
    sum_row(matrix[int(input("Enter the row you want to sum = "))-1])

def sum_row(row):
    print(sum(row))

def sum_column(column):
    print(column)

main()