import numpy as np

# 사칙연산


array =np.array([[1, 2, 3],
                 [5, 6, 7],
                 [9, 10, 11]])
array_2 = np.array([[2,2,2],
                    [2,2,2],
                    [2,2,2]])
print(array_2)
print(array)

# 덧
print(array+array_2)
print(np.add(array,array_2))

# 빼
print(array-array_2)
print(np.subtract(array,array_2))

# 곱 행렬간의 내적연산이 아님
print(array * array_2)
print(np.multiply(array,array_2))

# 나
print(array/array_2)
print(np.divide(array,array_2))

#제곱
print(array ** 2)
print(np.square(array))

#제곱근
print(np.sqrt(array))

# 몫
print(array//2)

# 나머지
print(array % 2)



