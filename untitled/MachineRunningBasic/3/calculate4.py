import numpy as np

#  비교 연산 삼각 함수

# 같으면 true 틀리면 false
arr1 = np.array([[1,2,3,],
                 [4,5,6]])

arr2 = np.array([[1,0,-1],
                 [5,-2,7]])

print(arr1 == arr2)
# 전체 동일여부
print(np.array_equal(arr1,arr2))


# 삼각 함수
arr3 = arr1 = np.array([[1,2,3,],
                        [4,5,6]])
# sin함수
print(np.sin(arr3))
print(np.cos(arr3))
print(np.tan(arr3))
print(np.pi)