import numpy as np


# 모든 넘파이 array는 고유한 타입을 가짐
# 데이터 타입을 다로 명시하지 않으면 적절한 넘파이 배열을 자동으로 인식하여 적용함
# 코더가 적용할 수 있음


# 데이터 형
# bool, int, float 등

arr = np.array([1.2,2.3,3.4], dtype=np.bool)
print(arr, arr.dtype)

# 변형 as타입

arr1 = np.array([0, 1, 2, 3])
print(arr1, arr.dtype)

arr1 = arr1.astype(np.float32) # 변경하는법
print(arr1, arr.dtype)

#주의할점
# 파이썬 리스트일 경우 여러가지 타입을 넣을 수 있음
# 넘파이에서는 단일 데이터만 가능

# 데이터 타입이 혼재하는 경우

arr3 = np.array([1,2,3.4])
print(arr3, arr3.dtype)
# float 형에 맞춰 바뀜

arr4 = np.array([1,2,"64"])
print(arr4, arr4.dtype)
# 문자열에 맞춰 바뀜 uni코드 형식으로 바뀜



# 섞어서
arr5 = np.array([1,2,"64, 문자열"], dtype=int)
print(arr5, arr5.dtype)
# 섞였기 때문에 에러