

def rotate(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return False

    n = len(matrix)

    for layer in range(n//2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):

            offset = i - first
            top = matrix[first][i]

            matrix[first][i] = matrix[last -offset][first]
            matrix[last -offset][first] = matrix[last][last -offset]
            matrix[last][last -offset] = matrix[i][last]

            matrix[i][last] = top


    return True

tmp = [[1,2,3],[4,5,6],[7,8,9]]
rotate(tmp)
print(tmp)