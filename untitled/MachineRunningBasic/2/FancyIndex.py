import numpy as np

# 특정 인덱스를 여러개 선택해서 탐색하는 방식
arr= np.array([5,10,15,20,25])
print(arr[[0, 2, 4]]) # 0,2,4 를 가져온다

# 2차원 배열 인덱싱

arr_2 = np.array([[5,10,15,20],
                  [25,30,35,40],
                  [45,50,55,60]])
print(arr_2[[0,2 ], 2:])
#0 행과 2행의 값중에서 2열 부터 끝까지 뽑아냄
# 15, 20    55, 60 출력