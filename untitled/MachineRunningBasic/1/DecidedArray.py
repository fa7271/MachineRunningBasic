import numpy as np
import numpy as ny

# np.zeros 정해진 형식의 n 차원 배열 생성
# 모든 원소들이 0으로된 배열을 생성

arr = np.zeros([2,2], dtype=int) # 인자는 shape
print(arr)


# np.ones
# 모든 원소들이 1로 만들어진 배열

arr1 = np.ones([2,2])
print(arr1)

# np.full
# 모든 원소들이 지정된 fillvalue

arr2 = np.full([2,2], 5) #인자는 5로
print(arr2)

# np.eye
# 행을 n 열을 m
#np.eye(n,m,k)
# 대각 원소가 1 그외 모두 0 대각  오른쪽 아래로만
# k = 대각원소의 발생지점을 어디에 나타낼지
arr3 = np.eye(3, 4, k = -1 )
print(arr3)


# 지정된 배열과 동일한 shape 배열 만들기
arr4 = np.array([[1,2,3],
                [5,6,7]])
copyarr4 = np.zeros_like(arr4)
print(copyarr4)

# 1로 카피하기
arr_0 = np.ones_like(arr4)
print(arr_0)

# full like
arr_f = np.full_like(arr4,3)
print(arr_f)


