import numpy as np

# index 의 접근하기

# 1차원 배열

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
 #arr = np.arange(10)
print(arr)

print(arr[0]) # index 3번째 값
print(arr[-1]) # 뒤로감 0 이전이므로 -9

# 1차원 배열에서 탐색
print(arr[3:8])



# 2차원 배열

arr_2 = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])
print(arr_2, arr_2.shape, arr_2.ndim)   # 배열 (3,4)행렬 2차원

print(arr_2[0][3])  # ==  print(arr_2[0, 3])
print(arr_2[0, :])  # 0번째 행 모든 원소 출력
print(arr_2[:, [1]]) # 특정 모든 열 출력


