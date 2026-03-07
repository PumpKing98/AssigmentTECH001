#Bài 1

numbers = []
while True:
    user_input = input("Nhập một số (nhấn Enter để kết thúc): ")
    if user_input == "":
        break
    numbers.append(float(user_input))
n = len(numbers)
for i in range(n):
    for j in range(i + 1, n):
        if numbers[i] < numbers[j]:
            temp = numbers[i]      
            numbers[i] = numbers[j] 
            numbers[j] = temp     
print("\n5 số lớn nhất theo thứ tự giảm dần là:")
for i in range(min(5, len(numbers))):
    print(numbers[i])
#Bài 2

seasons = ("Mùa xuân", "Mùa hè", "Mùa thu", "Mùa đông")
month = int(input("Nhập số tháng (1-12): "))
if month in (12, 1, 2):
    print(seasons[3])
elif 3 <= month <= 5:
    print(seasons[0])
elif 6 <= month <= 8:
    print(seasons[1])
elif 9 <= month <= 11:
    print(seasons[2])
#Bài 3

names = set()
while True:
    name = input("Nhập tên (nhấn Enter để dừng): ")
    if name == "":
        break
    
    if name in names:
        print("Existing name (Tên đã tồn tại)")
    else:
        print("New name (Tên mới)")
        names.add(name)

print("\nDanh sách các tên đã nhập:")
for n in names:
    print(n)
#Bài 4

def count_word_frequency(text):
    words = text.split()
    frequency = {}
    for word in words:
        word = word.lower().strip(".,!")
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

content = "Python là ngôn ngữ lập trình, Python rất dễ học."
print(count_word_frequency(content))
#Bài 5
def remove_odd_numbers(numbers_list):
    even_numbers = []
    for num in numbers_list:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers
input_list = []

print("Nhập các số nguyên (nhấn Enter để kết thúc):")
while True:
    user_input = input("Nhập số: ")
    if user_input == "":
        break
    num = int(user_input)
    input_list.append(num)
result_list = remove_odd_numbers(input_list)
print(f"Danh sách bạn đã nhập: {input_list}")
print(f"Danh sách sau khi lọc (chỉ còn số chẵn): {result_list}")