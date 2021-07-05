## to search for target in matrix, compare target with the last index of row
## if target is > than row[last index] then it means target might be in the next row
## if target is < than row[last index] then it means target might be in the in the previous columns

def search_matrix(matrix, target):
    row_index = 0
    col_index = len(matrix[row_index]) - 1
    while row_index < len(matrix) and col_index >= 0:
        if target == matrix[row_index][col_index]:
            print("target ", target, " is at (", row_index, ",", col_index, ")", sep='')
            return
        elif target > matrix[row_index][col_index]:
            row_index += 1
        else:
            col_index -= 1
    ## if reaches here, then it means target not found
    print("target", target, "not found")
    return -1

def main():
    square_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    target1 = 10
    target2 = 5
    target3 = 9
    search_matrix(square_matrix, target1)
    search_matrix(square_matrix, target2)
    search_matrix(square_matrix, target3)


main()