total = 0 # gọi biến tổng và cho biến tổng bằng 0
for i in range(3,100,2): # khỏi tạp vòng lập for cho biến i, bắt đầu với 3, kế thúc là 99, bước nhảy là 2
    total = total + 1/i**i # cập nhật biến tổng bằng tổng cộng với 1 chia cho i mũ i
one_over_the_total = 1/total # tính nghịc đảo của tổng
print("The result is: ",round(one_over_the_total, 2)) # in ra kết quả là nghịch đảo của tổng, làm tròn 2 chữ số thập phân

