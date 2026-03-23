#1
numbers = []
while True:
    user_input = input("Nhập một số (nhấn enter để dừng):")
    if user_input == "":
        break
    numbers.append(float(user_input))

numbers.sort(reverse=True)
top = numbers[:5]
print("5 số lớn nhất đã nhập là:", top)

#2
import math
n = int(input("Nhập một số nguyên tố: "))
prime = True

if n < 2:
    prime = False
else:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            prime = False
            break

if prime:
    print(n, "là số nguyên tố.")
else:
    print(n, "không phải là số nguyên tố.")

#3
cities = []
for i in range(5):
    city = input("Nhập tên thành phố: ")
    cities.append(city)

for city in cities:
    print(city)

#4
def tinh_tong(danh_sach):
    tong = 0
    for so in danh_sach:
        tong += float(so)
    return tong

nhap = input("Nhập dãy số :")
day = nhap.split()
ket_qua = tinh_tong(day)
print("Tổng của các số trong danh sách là:", ket_qua)

#5
def loc_so_chan(danh_sach):
    danh_sach_moi = []
    for n in danh_sach:
        if n % 2 == 0:
            danh_sach_moi.append(n)
    return danh_sach_moi

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ket_qua = loc_so_chan(numbers)
print("Các số chẵn trong danh sách là:", ket_qua)
