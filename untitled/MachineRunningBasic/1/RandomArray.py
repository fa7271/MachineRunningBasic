import numpy as np

# 시각화 하는 라이브러리
import matplotlib.pyplot as plt

# np.random.normal(평균, 표준편차, 사이즈) # 정규분포 확률분포에서 확률 뽑음
arr = np.random.normal(0, 1, (2, 3))
print(arr)

arr1 = np.random.normal(0, 1, 10000)
plt.hist(arr1, bins = 100 ) #bins = 난수를 몇개의 구간으로 구분해서 보여줄지
plt.show()

# rand  0~1 사이 값을 균등한 비율로 표본을 표출    인자 = 표본갯수

arr2 = np.random.rand(1000)
plt.hist(arr2, bins = 100)
plt.show()

# randn -1 부터 1사이 정규분포 표본 추출

arr3 = np.random.randn(1000) #표본의 갯수 1000개
plt.hist(arr3, bins=100)  # 구간 100개
plt.show()

# randint 랜덤한 정수만 출력  low 값 high 값 size
arr4 = np.random.randint(low = 1, high = 5, size = (3, 4))
plt.hist(arr4)

arr5 = np.random.randint(100, 200, 1000)
plt.hist(arr5, bins = 100)
plt.show()