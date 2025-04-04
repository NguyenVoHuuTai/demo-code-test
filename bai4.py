number = int(input("Nhap so co 3 chu so: ")) #nhập số có 3 chữ số
if number < 100 or number > 999: #kiểm tra số có 3 chữ số
    print("Nhap lai") #nếu không thỏa thì nhập lại
else:
    a = number // 100 # tách từng số
    b = (number // 10) % 10 # tách từng số
    c = number % 10 # tách từng số
    if a < b: # so sánh 2 số
        so_trung_gian = a # dùng số trung gian để lưu số nhỏ hơn
        a = b # đổi số lớn lên phía trước
        b = so_trung_gian # đổi số nhỏ xuống phía sau
    if a < c: # so sánh 2 số
        so_trung_gian = a # dùng số trung gian để lưu số nhỏ hơn
        a = c # đổi số lớn lên phía trước
        c = so_trung_gian # đổi số nhỏ xuống phía sau
    if b < c: # so sánh 2 số
        so_trung_gian = b # dùng số trung gian để lưu số nhỏ hơn
        b = c # đổi số lớn lên phía trước
        c = so_trung_gian # đổi số nhỏ xuống phía sau
    print("Day giam dan:", a, b, c) #in ra dãy giảm dần