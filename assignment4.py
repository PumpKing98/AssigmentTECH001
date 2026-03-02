#B1
def check_course_code(s):
    if len(s) != 6:
        return False
    
    for i in range(6):
        char = s[i]
        if i < 3:
            if not ('A' <= char <= 'Z'):
                return False
        else:
            if not ('0' <= char <= '9'):
                return False
                
    return True
while True:
     ma_nhap_vao = input("Nhập mã khóa học: ")
     ket_qua = check_course_code(ma_nhap_vao)
     if ket_qua == True :
          print("Hợp lệ")
          break
     else: 
          print("Nhập lại mã đi")
          
#b2
def is_valid_hex(color):
   if len(color) != 7 or color[0] != '#':
        return False
   a = "0123456789abcdefABCDEF"
   for i in color[1:]:
        if i not in a:
            return False
   return True
while True:
    thap_luc_phan = input("Nhập mã thập lục phân: ")
    ket_qua2 = is_valid_hex(thap_luc_phan)

    if ket_qua2:
        print("Hợp lệ")
        break
    else:
        print("Không hợp lệ, nhập lại đi")
#b3
def dem_so(bi):
    tong = 0
    current_num = ""
    for char in bi:
        if '0' <= char <= '9': 
            current_num += char 
        else:
            if current_num: 
                tong += int(current_num)
                current_num = "" 
    
    if current_num:
        tong += int(current_num)
        
    return tong
input_text = input("Nhập nội dung bất kỳ để tính tổng các số")
ketqua3 = (dem_so(input_text)) 
print (ketqua3)
#b4
def redact_phones(text):
    result = ""
    i = 0
    n = len(text)
    
    while i < n:
        if text[i:i+3] == "+84":
            result += "[REDACTED]"
            i += 3
            while i < n and '0' <= text[i] <= '9':
                i += 1
            continue
        muoi_so = True
        if i + 10 <= n:
            for j in range(i, i + 10):
                if not ('0' <= text[j] <= '9'):
                    muoi_so = False
                    break
            
            if muoi_so == True:
                result += "[REDACTED]"
                i += 10
                continue
        result += text[i]
        i += 1
        
    return result
doc = input()
print(redact_phones(doc))
