import numpy as np

arr = np.array([[1,2,3],
                [0, 1, 4]])

# 최소 min
print(np.min(arr))
# axix 값 지정

print(arr.min(axis=1))
# 최대 max
print(np.max(arr))
print(arr.max(axis=1))

# 합
print(np.sum(arr))
print(arr.sum(axis = 0))

#평균
print(np.mean(arr))
print(arr.mean(axis = 0))

#표준편차
print(np.std(arr))
print(arr.std(axis = 1))

#중앙값 median 짝수 개면 가운데 있는 2개 사이값
print(np.median(arr))

# comsum 누적값 계산
print(np.cumsum(arr))
print(arr.cumsum(axis = 1))


# 중앙값
print(np.median(arr, axis = 1))

