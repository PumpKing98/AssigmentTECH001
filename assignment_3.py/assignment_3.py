#Task 1
i = 1
while i <= 1000:
    if i % 3 == 0:
        print(i, end=" ")
    i += 1
#Task 2
while True:
    inch = float(input("Nhập số inch (nhập số âm để dừng):\n "))
    cm = inch * 2.54

    if inch < 0:
        print("Kết thúc chương trình.")
        break

    print(f"{inch} inch = {cm:.1f} cm")
#Task 3

nhap_so = input( "Hãy nhập dãy số (dừng chương trình nhấp enter): ")
if nhap_so == "":
    print(" Chuong trinh da ket thuc")
chuyen_doi = nhap_so.split() 

so_lon_nhat = chuyen_doi[0]
so_be_nhat = chuyen_doi[0]
for things in chuyen_doi:
    if so_lon_nhat < things:
        so_lon_nhat = things
print("Số lớn nhất là",so_lon_nhat)
for things in chuyen_doi:
    if so_be_nhat > things:
        so_be_nhat = things
print("Số bé nhất là",so_be_nhat)
#task 4
import random
a = range(1,11)
b = random.choice(a)
while True:
    nhap_1 = float(input ("Đoán 1 số từ 1 -> 10 đi nào:"))
    if nhap_1 > b:
        print("Too high")
    elif nhap_1 < b:
        print("Too Low")
    else:
        break
print("Correct")
#task 5
password = 'rules'
user_name = 'python'
da_nhap = 5
while True:
    a = input("Nhập tên đăng nhập:")
    b = input("Nhập mật khẩu:")
    if a == user_name and b == password:
        print("Welcome!!!")
        break
    else:
        con_lai = da_nhap -1
        print ( "Số lần thử còn lại: ", con_lai)
        da_nhap -= 1
        if da_nhap == 0:
            print("Access denied")
            break
#Task 6
nhap_lieu = input("Nhập dãy kí tự( số, chữ, kí tự đặc biệt) bất kỳ:")
so_luong = len(nhap_lieu)
middle = so_luong // 2 
if so_luong % 2 != 0:
    ket_qua = nhap_lieu[middle]

else:
    ket_qua = nhap_lieu[middle - 1 : middle + 1]

print("Kết quả là:", ket_qua)     
#Task 7 
nhap_cum = input("Nhập cụm muốn viết tắt:")
tach_tu = nhap_cum.split()
tu_tat = ""
for love in tach_tu:
    tu_tat += love[0].upper()
print(tu_tat)
        
     
