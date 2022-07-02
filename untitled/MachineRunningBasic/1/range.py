import numpy as np
# 특정 범위의 값을 가지는 N차원 배열생성

# 순차적 값 생성 (이름순,번호순)

lst = list(range(5, 9, 2 ))
print(lst)

# === 시작,끝(미만),갭
arr = np.arange(5, 9, 2) # == arr = np.arrange(stop = 9, step = 2, start = 5)
print(arr)

# 시작 끝 넘 0 부터 100(포함)까지 11개 간격으로
arr1= np.linspace(0, 100, 10)
print(arr1)

#log space 지정된 범위에서 넘 갯수만큼 균등한 간격으로 데이터를 르고스페이스로 생성

#밑이 2인
arr2 = np.logspace(1, 10, 10, base=2)
print(arr2)

