# ------------------------------Lecture1------------------------------
# Ctrl + / to disable or enable comment
# print("hello world")
# x = input()
# print(x)
# print("The first name")
# first_name = input()
# print("The first name is " + first_name) #concanitation
# print("The last name")
# last_name = input()
# print("The last name is" + last_name)
# print("Your name is " + last_name + " " + first_name)
# first_name = input("Your first name: ")
# last_name = input("Your last name: ")
# print("Your name is " + last_name + " " + first_name)
# CURRENT_YEAR = 2025
# year_born = int(input("Enter the year you were born: "))
# age = CURRENT_YEAR - year_born
# year_born = input("Enter the year you were born: ")
# year_born = int(year_born) #overwrite
# age = CURRENT_YEAR - int(year_born)
# print("You are " + str(age) + " years old")
# print("You are " + str(age) + " years old in " + str(CURRENT_YEAR))
# print("You are {0} years old in {1}".format(age, CURRENT_YEAR))
# x = "1.856963254488"
# x = float(x)
# x = round(x,5) #lam tron so
# print(x)
# temperature = int(input("Enter the temperature: "))
# if temperature < 15:
# 	print("It's cold")
# elif temperature >= 15 and temperature <= 25:
#    	print("It's good")
# else:
# 	print("It's hot")
# one tab = 4 spaces
# temperature = 14
# hot = False
# if temperature > 30:
# 	hot = True
# if not hot:
# 	print("It's not hot")
# if temperature < 15:
# 	print("It's cold")
# 	if temperature >=10 and temperature <= 12 or temperature == 14:
# 		print("It's very cold")
# else:
# 	print("It's good")
# gender_input = input("Are you male (yes or no): ")
# is_male = None

# if gender_input == "yes":
#     is_male = True
# elif gender_input == "no":
# 	is_male = False
# else:
#     is_male = None

# if is_male == True:
# 	print("You are male")
# elif is_male == False:
# 	print("You are female")
# elif is_male == None:
# 	print("Unknown")
# import numpy as np
# x = 4
# y = np.sqrt(x)
# print(y)
# if isinstance(y, int):
#     print(y)
# else:
#     print("Not an integer")
# ------------------------------Lecture2------------------------------
# for i in range(5):
# for i in range (0,5):
    # print(i)
#     print(2*i)
# for i in range(4):
#     print((2*i)+1)
# for i in range (0,6,2): # in range(a,b,c) a la gia tri dau, b la gia tri cuoi, c la buoc nhay
#     print(i)
# for i in range(0, 3):
#     print(i)
#     for j in range(3, 5):
#         print(j)
# i = 0
# for j in range(3, 5):
#     print(j)
#     print(i)
# i=1
# for j in range(3, 5):
#     print(j)
#     print(i)
# for i in range(0,2):
#     for j in range(3,5 ):
#         print(j)
#         print(i)
# for i in range(0,2):
#     for j in range(3,5 ):
#         print(j)
#     print(i)
# for i in range(10):
#     if i == 5:
#         continue
#     print(i)
# for i in range(10):
#     if i == 5:
#         break
#     print(i)
# i = 0
# while i < 5:
#     print(i)
#     i = i + 1
# while True:
#     print(i)
#     i += 1
# i = 0
# while i < 10:
#     i += 1
#     if i == 5:
#         continue
#     print(i)
#     i += 1
# while True:
#     gender_input = input("Are you male (yes/no): ")
#     if gender_input == "yes" or gender_input == "no":
#         break
# answers_list = ["yes", "no", "y", "n"]
# while True:
#     gender_input = input("Are you male (yes/no): ")
#     if gender_input in answers_list:
#         break
# def print_number():
#     print(1)
#     print(2)
#     print(3)

# def print_letter():
#     print("a")
#     print("b")
#     print("c")

# print_number()
# print_letter()

# def print_number(max_number):
#     for i in range(max_number):
#         print(i)
# number = 5
# print_number(number)
# number = 6
# print_number(number)

# def giai_thua(n):
#     if n == 0:
#         return 1
#     return n * giai_thua(n-1)
# print(giai_thua(5))

# def print_number(min_number, max_number, distance):
#     for i in range(min_number, max_number, distance):
#         print(i)

# print_number(2, 10, 2)

# def print_number(min, max):
#     for i in range(min, max):
#         print(i)

# print_number(2, 5)

# def add_one(number):
#     number = number + 1
#     return number

# x = 2
# x = add_one(x)
# print(x)
# y = 10
# y = add_one(y)
# print(y)

# a = [1, 2, 3, 4, 5]
# b = [1, 2, 3]

# result = a + b
# print(result)

# #Câu 1 - 24119189 - Nguyễn Võ Hữu Tài
# students = {}

# n = int(input("Nhập số lượng học sinh: "))

# for i in range(n):
#     print(f"\nNhập thông tin học sinh {i+1}:")
#     name = input("Tên: ")
#     age = int(input("Tuổi: "))
#     avg_score = float(input("Điểm trung bình: "))
    
#     students[name] = {"Tuổi": age, "Điểm trung bình": avg_score}

# print("\nDanh sách học sinh:")
# for name, info in students.items():
#     print(f"Tên: {name}, Tuổi: {info['Tuổi']}, Điểm trung bình: {info['Điểm trung bình']}")

# # Câu 2 - 24119189 - Nguyễn Võ Hữu Tài
# contacts = {}

# while True:
#     print("\nChọn chức năng:")
#     print("1. Thêm liên hệ mới")
#     print("2. Tìm số điện thoại theo tên")
#     print("3. Xóa liên hệ theo tên")
#     print("4. Thoát")
    
#     choice = input("Nhập lựa chọn (1-4): ")
    
#     if choice == "1":
#         name = input("Nhập tên: ")
#         phone = input("Nhập số điện thoại: ")
#         contacts[name] = phone
#         print(f"Đã thêm liên hệ: {name} - {phone}")
    
#     elif choice == "2":
#         name = input("Nhập tên cần tìm: ")
#         if name in contacts:
#             print(f"Số điện thoại của {name}: {contacts[name]}")
#         else:
#             print("Không tìm thấy liên hệ.")
    
#     elif choice == "3":
#         name = input("Nhập tên cần xóa: ")
#         if name in contacts:
#             del contacts[name]
#             print(f"Đã xóa liên hệ {name}.")
#         else:
#             print("Không tìm thấy liên hệ.")
    
#     elif choice == "4":
#         print("Thoát chương trình.")
#         break
    
#     else:
#         print("Lựa chọn không hợp lệ, vui lòng nhập lại.")

# # Câu 3 - 24119189 - Nguyễn Võ Hữu Tài
# students = {}

# n = int(input("Nhập số lượng sinh viên: "))

# for i in range(n):
#     print(f"\nNhập thông tin sinh viên {i+1}:")
#     name = input("Tên: ")
#     score = float(input("Điểm số: "))
    
#     students[name] = score

# if students:
#     avg_class_score = sum(students.values()) / len(students)
#     print(f"\nĐiểm trung bình của cả lớp: {avg_class_score:.2f}")
# else:
#     print("\nKhông có sinh viên nào trong danh sách.")

# def quan_ly_hoc_vien():
#     danh_sach_hoc_vien = set()  # 🟣 Khởi tạo tập hợp để lưu danh sách học viên

#     while True:
#         print("\n\033[95m Chọn chức năng:\033[0m")  # 💜 Màu tím
#         print("\033[94m1.\033[0m Nhập danh sách học viên")  
#         print("\033[94m2.\033[0m Xóa học viên")  
#         print("\033[94m3.\033[0m Hiển thị danh sách")  
#         print("\033[94m4.\033[0m Lưu danh sách vào file & Thoát")  
        
#         lua_chon = input("\033[96mLựa chọn: \033[0m")  # 💙 Màu cyan cho input

#         if lua_chon == "1":  
#             while True:
#                 ten = input("\033[92mNhập tên học viên (nhập stop để dừng): \033[0m")  # 💚 Màu xanh lá
#                 if ten.lower() == "stop":  
#                     break  
#                 if ten in danh_sach_hoc_vien:
#                     print("\033[91mHọc viên đã tồn tại trong danh sách!\033[0m")  # 🔴 Màu đỏ cho lỗi
#                 else:
#                     danh_sach_hoc_vien.add(ten)
#                     print("\033[93mĐã thêm học viên\033[0m")  # 🟠 Màu cam

#         elif lua_chon == "2":  
#             ten = input("\033[92mNhập tên học viên cần xóa: \033[0m")  
#             if ten in danh_sach_hoc_vien:
#                 danh_sach_hoc_vien.discard(ten)
#                 print(f"\033[93mĐã xóa học viên: {ten}\033[0m")  
#             else:
#                 print("\033[91mHọc viên không có trong danh sách!\033[0m")  

#         elif lua_chon == "3":  
#             if len(danh_sach_hoc_vien) != 0:  
#                 print("\033[96mDanh sách học viên:\033[0m", danh_sach_hoc_vien)  
#             else:
#                 print("\033[91mDanh sách học viên trống.\033[0m")  

#         elif lua_chon == "4":  
#             with open("students.txt", "w", encoding="utf-8") as f:  
#                 for ten in sorted(danh_sach_hoc_vien):  
#                     f.write(ten + "\n")  
#             print("\033[92mDanh sách đã được lưu vào file. Thoát chương trình!\033[0m")  
#             break  

#         else:
#             print("\033[91mLựa chọn không hợp lệ! Vui lòng nhập số từ 1 đến 4.\033[0m")  

# quan_ly_hoc_vien()

def dracula_demo():
    print("\033[95m--- DRACULA THEME DEMO ---\033[0m")  # 💜 Màu tím (Tiêu đề)
    print("\033[94m1. \033[92mXanh lá - Thành công!\033[0m")  # 🟢 Xanh lá
    print("\033[94m2. \033[91mĐỏ - Cảnh báo!\033[0m")  # 🔴 Đỏ
    print("\033[94m3. \033[93mVàng - Chú ý!\033[0m")  # 🟡 Vàng
    print("\033[94m4. \033[96mCyan - Thông tin!\033[0m")  # 🔵 Cyan
    print("\033[95m--- END DEMO ---\033[0m")  # 💜 Màu tím

dracula_demo()