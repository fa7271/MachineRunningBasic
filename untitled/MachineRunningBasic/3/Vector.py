import numpy as np
import time


# Benefit
array = np.arange(99999999)
array2 = np.arange(99999999)
# for
sum = 0
before = time.time()
for i in array:
    sum += i
after = time.time()
print(sum)
print(sum, after - before , " 초1 ") # 연산에 걸린 총 시간


# vector

before = time.time()
sum = np.sum(array)
after = time.time()
print(sum, after - before, " 초2 ")


# 포문
before = time.time()
sum = 0
for i, j in zip(array,array2):
    sum += i * j
after = time.time()
print(sum,after - before, "초3")


# vector
before = time.time()
sum = np.dot(array,array2)
after = time.time()
print(sum, after - before, "초4")





