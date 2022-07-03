import numpy as np

#boolean T/F

array = np.array([1, 2, 3, 4 ])
print(array[[True, False, True, True]])
# True 만 가져오기   1, 3, 4

array_2 =np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])
print(array_2)
print(array_2[[True, False,False], True]) # 앞에는 행 뒤에는 열 True 값만 가져옴

