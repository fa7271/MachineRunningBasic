import numpy as np

# 특정 시작점을 직접 설정 하게 되면 발생하게 된 난수 제어 >> 가능하게 하는 시드 존재

arr = np.random.rand(10) # 표본 10개
print("난수 발생 \n", arr)

arr = np.random.rand(10) # 표본 10개
print("난수 발생2 \n", arr)

# np seed로 고정 가능
np.random.seed(1) # 시작 1
arr1 = np.random.rand(10)
print("난수 발생1 \n", arr1)

np.random.seed(1) # 시작 1
arr2 = np.random.rand(10)
print("난수 발생2 \n", arr2)

# 시작점만 같은면 동일한 난수가 출력된다
# 시드는 코드값마다 지정해 줘야함





