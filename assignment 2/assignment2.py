##task1
chieu_dai = float(input("Chiều dài cá (cm): "))
toi_thieu = 42
if chieu_dai < toi_thieu:
        thieu = toi_thieu - chieu_dai
        print("Cá không đạt kích thước tiêu chuẩn. Hãy thả cá lại hồ.")
        print(f"Cá ngắn hơn quy định {thieu:.1f} cm.")
else:
        print("Cá đạt kích thước cho phép.")
#task2 
cabin_class = input("Enter the cabin class (LUX, A, B, C): ").upper()

if cabin_class == "LUX":
        print("Upper-deck cabin with a balcony.")
elif cabin_class == "A":
        print("Above the car deck, equipped with a window.")
elif cabin_class == "B":
        print("Windowless cabin above the car deck.")
elif cabin_class == "C":
        print("Windowless cabin below the car deck.")
else:
        print("Invalid cabin class.")
#task 3
sex = input ("Enter biological sex(male/ female):")
hemoglobin = float(input("Enter Hemoglobin value(g/l):"))
if sex == "female" :
    if hemoglobin < 117 :
            print("Hemoglobin level is low.")
    elif hemoglobin < 155:
            print("Hemoglobin level is normal.")
    else:
            print("Hemoglobin level is high.")
elif sex == "male":
    if hemoglobin < 134:
            print("Hemoglobin level is low.")
    elif hemoglobin < 167:
            print("Hemoglobin level is normal.")
    else:
            print("Hemoglobin level is high.")
else:
            print("Invalid sex input.")
#task4

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
else:
        print(f"{year} is not a leap year.")
#task5
import math
def pizza_unit_price(d, p):
    r = (d / 2) / 100
    return p / (math.pi * r * r)

d1 = float(input("Pizza 1 diameter (cm): "))
p1 = float(input("Pizza 1 price (USD): "))
d2 = float(input("Pizza 2 diameter (cm): "))
p2 = float(input("Pizza 2 price (USD): "))

u1 = pizza_unit_price(d1, p1)
u2 = pizza_unit_price(d2, p2)

if u1 < u2:
    print("Pizza 1 is cheaper per square meter.")
elif u2 < u1:
    print("Pizza 2 is cheaper per square meter.")
else:
    print("Both pizzas have the same price.")
