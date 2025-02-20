total = 0 # khởi tạo biến tổng và cho giá trị của biến tổng bằng 0
for i in range(100): # khởi tạo vòng lặp for cho biến i, bắt đầu từ 0 đến một giá trị lớn sao cho để tổng khi cộng lại phải lớn hơn 50
		total += i # cập nhật biến tổng bằng tổng cộng với i
		if total > 50: # nếu tổng lớn hơn 50 thì dừng vòng lặp
			break # dừng vòng lặp
print("The result is: ", total) # in ra kết quả là tổng

# cách khác để không cần phải giới hạn giá trị vòng lập for bằng cách dùng itertools
# import itertools # khai báo thư viên itertools
# total = 0 
# for i in itertools.count(1): # khởi tạo vòng lặp for cho biến i, dùng itertools để đếm từ 1 đến vô cùng
#    if total > 50: 
#        break
# print("The result is: ", total)