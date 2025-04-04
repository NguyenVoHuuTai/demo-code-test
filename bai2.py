import numpy as np # thêm thư viện numpy để sử dụng hàm căn bậc 2
print("Nhap 1 neu la hinh tam giac.") # quy ước số 1 là hình tam giác
print("Nhap 2 neu la hinh vuong.") # quy ước số 2 là hình vuông
print("Nhap 3 neu la hinh chu nhat.") # quy ước số 3 là hình chữ nhật
print("Nhap 4 neu la hinh tron.") # quy ước số 4 là hình tròn
shape = int(input("Nhap hinh: ")) # nhập số tương ứng với hình
if shape == 1: # nếu là hình tam giác
    canh_a = int(input("Nhap canh a: ")) # nhập cạnh a
    canh_b = int(input("Nhap canh b: ")) # nhập cạnh b
    canh_c = int(input("Nhap canh c: ")) # nhập cạnh c
    if canh_a < 0 or canh_b < 0 or canh_c < 0 or canh_a == canh_b or canh_a == canh_c or canh_b == canh_c or canh_a + canh_b <= canh_c or canh_a + canh_c <= canh_b or canh_b + canh_c <= canh_a: # kiểm tra điều kiện tam giác
        print("Khong phai tam giac, moi nhap lai.") # nếu không thỏa thì không phải tam giác
    else:
        nua_chu_vi_tam_giac = (canh_a + canh_b + canh_c) / 2 # tính nửa chu vi tam giác
        dien_tich_tam_giac = np.sqrt((nua_chu_vi_tam_giac * (nua_chu_vi_tam_giac - canh_a) * (nua_chu_vi_tam_giac - canh_b) * (nua_chu_vi_tam_giac - canh_c))) # tính diện tích tam giác bằng heron
        print("Dien tich tam giac: ", round(dien_tich_tam_giac, 2)) # in diện tích tam giác
elif shape == 2: # nếu là hình vuông
    canh = int(input("Nhap canh: ")) # nhập cạnh
    if canh < 0: # kiểm tra điều kiện hình vuông
        print("Khong phai hinh vuong, moi nhap lai.") # nếu không thỏa thì không phải hình vuông
    else:
        dien_tich_vuong = canh ** 2 # tính diện tích hình vuông
        print("Dien tich hinh vuong: ", dien_tich_vuong) # in diện tích hình vuông
elif shape == 3: # nếu là hình chữ nhật
    chieu_dai = int(input("Nhap chieu dai: ")) # nhập chiều dài
    chieu_rong = int(input("Nhap chieu rong: ")) # nhập chiều rộng
    if chieu_dai < 0 or chieu_rong < 0: # kiểm tra điều kiện hình chữ nhật
        print("Khong phai hinh chu nhat, moi nhap lai.") # nếu không thỏa thì không phải hình chữ nhật
    else:
        dien_tich_chu_nhat = chieu_dai * chieu_rong # tính diện tích hình chữ nhật
        print("Dien tich hinh chu nhat: ", dien_tich_chu_nhat) # in diện tích hình chữ nhật
else: # nếu là hình tròn
    ban_kinh = int(input("Nhap ban kinh: ")) # nhập bán kính
    if ban_kinh < 0: # kiểm tra điều kiện hình tròn
        print("Khong phai hinh tron, moi nhap lai.") # nếu không thỏa thì không phải hình tròn
    else:
        dien_tich_tron = np.pi * ban_kinh ** 2 # tính diện tích hình tròn
        print("Dien tich hinh tron: ", round(dien_tich_tron, 2)) # im diện tích hình tròn
