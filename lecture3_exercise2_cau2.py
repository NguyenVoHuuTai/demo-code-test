m = int(input("Enter the number: ")) # khai báo số nguyên m
n = int(input("Enter the number: ")) # khai báo số nguyên n

if m > n: # nếu m lớn hơn n
    for i in range(1, n + 1): # khởi tạo vòng lặp for cho biến i, bắt đầu từ 1, vì nếu khỏi tạo kết thúc là n thì vòng lập chỉ chạy đến giá trị n - 1 nên khởi tạo kết thúc là n + 1 để vòng lập chạy đến n, bước nhảy là 1
        if m % i == 0 and n % i == 0: # nếu số mà cả m và n cùng chia hết thì đó là ước chung của m và n
            gcd = i # gáng giá trị đó cho biến gcd và tiếp tục gáng cho đến khi giá trị ước chung lớn nhất
    print("The greatest common divisor of", m, "and", n, "is", gcd) # in ra ước chung lớn nhất của m và n
if n > m: # n lớn hơn m thì làm tương tự như trên
    for i in range(1, m + 1): # lưu ý cho vòng lập chạy từ 1 đến số nhỏ hơn (ở đây là m)
        if m % i == 0 and n % i == 0: # nếu số mà cả m và n cùng chia hết thì đó là ước chung của m và n
            gcd = i # gáng giá trị đó cho biến gcd và tiếp tục gáng cho đến khi giá trị ước chung lớn nhất
    print("The greatest common divisor of", m, "and", n, "is", gcd) # in ra ước chung lớn nhất của m và n

# Cách khác:
# for i in range(1, min(m, n) + 1): # khởi tạo vòng lặp for cho biến i, bắt đầu từ 1, kết thúc là số nhỏ hơn trong 2 số m và n và cộng thêm 1, bước nhảy là 1
#     if m % i == 0 and n % i == 0:
#             gcd = i 
# print("The greatest common divisor of", m, "and", n, "is", gcd) 

# Cách khác:
# import math
# gcd_value = math.gcd(a, b)  # hàm dùng để tìm ước chung nhỏ nhất