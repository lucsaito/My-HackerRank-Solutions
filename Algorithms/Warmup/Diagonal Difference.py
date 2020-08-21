# Returns the difference between the primary diagonal and the secondary of a nxn matrix.

def diagonalDifference(arr):
    primDiag = 0
    secDiag = 0
    for i in range(len(arr)):
        primDiag += arr[i][i]
        secDiag += arr[i][-(i+1)]
    return abs(primDiag - secDiag)

# ex:  [[1, 2, 3, 4], [6, 7, 8, 9], [11, 12, 13, 14], [16, 17, 18, 19]]
print(diagonalDifference([[1, 2, 3, 4], [6, 7, 8, 9], [11, 12, 13, 14], [16, 17, 18, 19]]))