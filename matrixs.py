import numpy as np

def create_matrix(mc):
    print(f"\nArray {mc} elements :")
    array_1 = list(map(int, input().split()))
   
    print(f"\nArray {mc} row and column size:")
    row, column = map(int, input().split())

    if len(array_1) != (row * column):
        print("\nRow and column size do not match with total elements! Retry.")
        return create_matrix(mc)

    array_1 = np.array(array_1).reshape(row, column)
    print(f"\nArray {mc} is:")
    print(array_1)
    return array_1

arr1 = create_matrix(1)
arr2 = create_matrix(2)

if arr1.shape[1] == arr2.shape[0]:
    print("\nDot product result:")
    print(np.dot(arr1, arr2))
else:
    print("\nDot product not possible: column of first != row of second.") 