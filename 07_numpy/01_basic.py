"""
    Numpy (넘파이)

    다차원 배열을 다룰 수 있는 기능을 제공하는 라이브러리
    넘파이 배열 : ndarray
"""
import numpy as np

# 파이썬 리스트에는 다양한 타입의 데이터를 담을 수 있음.
data_list = [1, "이", 3.0, [4]]
print(f"data_list : {data_list}")
print(f" 각 요소 별 타입 : {[type(x).__name__ for x in data_list]}")

"""
data_list2  = [10,20,30,40]

for d1, d2 in zip(data_list, data_list2):
    print(f"{d1} + {d2} + = {d1 + d2}")
print('-'*60)
"""
# 데이터구분않고 담을수있는 장점, 다른리스트와 연산할때는 문제 될수있음

arr = np.array([1,2,3,4])
print(f"arr : {arr}")
print(f"배열 타입 : {arr.dtype}")

arr2 = np.array([5,6,7,8])
print(f"arr2 : {arr2}")

"""
for d1, d2 in zip(arr, arr2):
    print(f"{d1} + {d2} + {d1 + d2}")
    """

print(f"arr +arr2 = {arr +arr2}")

print("=" * 60)

arr_0d = np.array(42)
print(f"0차원 배열 : {arr_0d}, 차원: {arr_0d.ndim}, 형태: {arr_0d.shape}")

arr_1d = np.array([1,2,3])
print(f"1차원 배열: {arr_1d}, 차원: {arr_1d.ndim}, 형태: {arr_1d.shape}")

arr_2d = np.array([[1,2,3], [4,5,6]])
print(f"2차원 배열: {arr_2d}, 차원: {arr_2d.ndim}, 형태: {arr_2d.shape}")

print("=" * 60)

n = 100_000
print(f"n : {n}")

list_10m = list(range(n))
arr_10m = np.arange(n)

print(f"list_10m : {list_10m[:5]} ... {list_10m[-5:]}")
print(f"arr_10m : {arr_10m[:5]} ... {arr_10m[-5:]}")

import sys 

list_container = sys.getsizeof(list_10m)
int_obj = sys.getsizeof(list_10m[0])
list_bytes = list_container + ( int_obj * n)

arr_bytes = arr_10m.nbytes

print(f" 데이터 {n:,}개 기준")
print(f" - 리스트 : {list_bytes / 1024 / 1024:6.2f} MB")
print(f" - 배열 : {arr_bytes / 1024 / 1024:6.2f}MB")