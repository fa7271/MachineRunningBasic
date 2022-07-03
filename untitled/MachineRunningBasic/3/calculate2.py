import numpy as np

array = np.array([1,2,3])
array2 = np.array([4,6,7])

print(np.dot(array,array2))

arr_1 = np.array([[1,2],
                  [3,4]])
arr_2 = np.array([[5,6],
                  [7,8]])

print(np.dot(arr_1, arr_2))

# 절댓값

arr_3 = np.array([[1,2],
                  [-2,-5]])
print(np.abs(arr_3))


arr_4 = np.array([[1,2.643],
                  [3,-4]])
print(np.ceil(arr_4))
print(np.floor(arr_4)) # 내림
print(np.round(arr_4))
print(np.trunc(arr_4))

