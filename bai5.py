diem_chuyen_can = int(input("NHap diem chuyen can: ")) # nhập điểm chuyên cần
diem_bai_tap_tren_lop = int(input("Nhap diem bai tap tren lop: ")) # nhập điểm bài tập trên lớp
diem_bai_tap_ve_nha = int(input("Nhap diem bai tap ve nha: ")) # nhập điểm bài tập về nhà
diem_giua_ky = int(input("Nhap diem giua ky: ")) # nhập điểm giữa kỳ
diem_cuoi_ky = int(input("Nhap diem cuoi ky: ")) # nhập điểm cuối kỳ
diem_trung_binh = diem_chuyen_can * 0.1 + diem_bai_tap_tren_lop * 0.1 + diem_bai_tap_ve_nha * 0.1 + diem_giua_ky * 0.2 + diem_cuoi_ky * 0.5 #tính điểm trung bình
if diem_trung_binh >= 9: # kiểm tra điểm trung bình để xếp loại
    print("Loai A") # in loại A
elif diem_trung_binh < 9 and diem_trung_binh >= 7: # kiểm tra điểm trung bình để xếp loại
    print("Loai B") # in loại B
elif diem_trung_binh < 7 and diem_trung_binh >= 5: # kiểm tra điểm trung bình để xếp loại
    print("Loai C") # in loại C
elif diem_trung_binh < 5: # kiểm tra điểm trung bình để xếp loại
    print("Loai D") # in loại D