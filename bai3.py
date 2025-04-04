import numpy as np # thêm thư viện numpy để sử dụng hàm căn bậc 2
number = int(input("Nhap so: ")) # nhập số N
if number < 0: # kiểm tra số N
    print("Khong thoa mang: ")
else:
    so_lay_can = np.sqrt(number) # lấy căn bậc 2 của số N
    if so_lay_can % 1 == 0: # kiểm tra số nguyên
        print(str(number) + " " + "la so chinh phuong.") # in ra số chính phương
    else:
        print(str(number) + " " + "khong phai la so chinh phuong.") # in ra không phải số chính phương