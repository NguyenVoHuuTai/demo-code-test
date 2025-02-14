import numpy as np
print("Nhap 1 neu la hinh tam giac.")
print("Nhap 2 neu la hinh vuong.")
print("Nhap 3 neu la hinh chu nhat.")
print("Nhap 4 neu la hinh tron.")
shape = int(input("Nhap hinh: "))
if shape == 1:
    canh_a = int(input("Nhap canh a: "))
    canh_b = int(input("Nhap canh b: "))
    canh_c = int(input("Nhap canh c: "))
    if canh_a < 0 or canh_b < 0 or canh_c < 0 or canh_a + canh_b <= canh_c or canh_a + canh_c <= canh_b or canh_b + canh_c <= canh_a:
        print("Khong phai tam giac, moi nhap lai.")
    else:
        nua_chu_vi_tam_giac = (canh_a + canh_b + canh_c) / 2
        dien_tich_tam_giac = np.sqrt((nua_chu_vi_tam_giac * (nua_chu_vi_tam_giac - canh_a) * (nua_chu_vi_tam_giac - canh_b) * (nua_chu_vi_tam_giac - canh_c)))
        print("Dien tich tam giac: ", round(dien_tich_tam_giac, 2))
if shape == 2:
    canh = int(input("Nhap canh: "))
    if canh < 0:
        print("Khong phai hinh vuong, moi nhap lai.")
    else:
        dien_tich_vuong = canh ** 2
        print("Dien tich hinh vuong: ", dien_tich_vuong)
if shape == 3:
    chieu_dai = int(input("Nhap chieu dai: "))
    chieu_rong = int(input("Nhap chieu rong: "))
    if chieu_dai < 0 or chieu_rong < 0:
        print("Khong phai hinh chu nhat, moi nhap lai.")
    else:
        dien_tich_chu_nhat = chieu_dai * chieu_rong
        print("Dien tich hinh chu nhat: ", dien_tich_chu_nhat)
if shape == 4:
    ban_kinh = int(input("Nhap ban kinh: "))
    if ban_kinh < 0:
        print("Khong phai hinh tron, moi nhap lai.")
    else:
        dien_tich_tron = np.pi * ban_kinh ** 2
        print("Dien tich hinh tron: ", dien_tich_tron, 2)
