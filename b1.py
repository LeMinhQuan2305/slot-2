import math
#problem 1
array = list(map(int, input("Nhập các phần tử của mảng cách nhau bởi dấu cách: ").split()))
# Tạo tbc

avg = float(sum(array)/ len(array))
diffmin = 0
pos = 0
for i in range(len(array)):
    if abs(array[i]- avg <= diffmin):
        diff = array[i]
        pos = i
print(pos)
#problem 2
a = float(input("Nhập điểm: "))
if 8.5 <= a <= 10:
    print("Điểm chữ: A - Điểm hệ 4 : 4")
elif 7.0 <= a <= 8.4:
    print("Điểm chữ: B - Điểm hệ 4 : 3")
elif 5.5 <= a <= 6.9:
    print("Điểm chữ: C - Điểm hệ 4 : 2")
elif 4.0 <= a <= 5.4:
    print("Điểm chữ: D - Điểm hệ 4 : 1")
else:
    print("Điểm chữ: F - Điểm hệ 4 : 0")
#problem 3:
array = list(map(float, input("Nhập các phần tử của mảng cách nhau bởi dấu cách: ").split()))
array0laplaiso = list(set(array))
print(array0laplaiso)

    