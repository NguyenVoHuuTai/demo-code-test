number = int(input("Nhap so co 3 chu so: ")) #nhập số có 3 chữ số
if number < 100 or number > 999: #kiểm tra số có 3 chữ số
    print("Nhap lai") #nếu không thỏa thì nhập lại
else:
    # print("So hang tram: ", number // 100) 
    # print("So hang chuc: ", (number // 10) % 10)
    # print("So hang don vi: ", number % 10)
    print("Hieu 3 chu so: ", (number // 100) - ((number // 10) % 10) - (number % 10)) 