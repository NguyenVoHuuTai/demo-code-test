number = int(input("Nhap so co 3 chu so: ")) #nhập số có 3 chữ số
if number < 100 or number > 999: #kiểm tra số có 3 chữ số
    print("Nhap lai") #nếu không thỏa thì nhập lại
else:
    so_hang_tram = number // 100 # tìm số hàng trăm
    so_hang_chuc = (number // 10) % 10 # tìm số hàng chục
    so_hang_don_vi = number % 10 # tìm số hàng đơn vị
    print("Hieu 3 chu so: ", so_hang_tram - so_hang_chuc - so_hang_don_vi) #in ra hiệu 3 chữ số