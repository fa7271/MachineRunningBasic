import numpy as np


# 1차원
arr = np.array([1,2,3])
print(arr)

# 2 차원
arr2 = np.array([[1,2,3],
               [4,5,6]])
print(arr2)

print(type(arr)) # numpy ndarray임


#tpl

tpl = (4,5,6)
arrtpl = np.array(tpl)
print(arrtpl)

#lst
lst = [1,2,3]
arrlst = np.array(lst)

print(arrlst+arrlst)


#shape 배열의 형태

arr1 = np.array([1,2,3])
arr2 = np.array([[1,2,3], [4,5,6]])

print(arr1.shape, arr2.shape)
# 원소가 3개인 1차원배열  (3,)
# 원소가 2개인 2차원 배열 (2,3)      앞이 행 뒤가 열

# ndim 차원
print(arr1.ndim, arr2.ndim)
# >> 1 2

# size

print(arr1.size, arr2.size)
#  원소 3개 6개


