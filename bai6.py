quang_duong = int(input("Nhap quang duong: ")) # nhập quãng đường
if quang_duong < 0: # kiểm tra quãng đường
    print("Nhap lai") # nếu không thỏa thì nhập lại
if quang_duong == 1: # nếu quãng đường bằng 1
    print("Gia tien: 13000 VND") # in giá tiền
elif quang_duong > 1 and quang_duong <= 35: # nếu quãng đường lớn hơn 1 và nhỏ hơn hoặc bằng 35
    print("Gia tien:", 13000 + (quang_duong - 1) * 12000, "VND") # in giá tiền
elif quang_duong > 35: # nếu quãng đường lớn hơn 35
    print("Gia tien:", 13000 + 34 * 12000 + (quang_duong - 35) * 11000, "VND") # in giá tiền