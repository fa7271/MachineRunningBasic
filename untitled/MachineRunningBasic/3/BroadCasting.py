import numpy as np

# array 의 shape 을 안 맞춰도됨

arr1 = np.array([[0,0,0],
                 [1,1,1],
                 [2,2,2]])

arr2 = np.array([[1,2,3]])

print(arr1 + arr2)

arr3 = np.array([[1,1,1]])
arr4 = np.array([[1]])

print(arr3 + arr4)