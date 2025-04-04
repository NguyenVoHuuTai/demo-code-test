import numpy as np
import matplotlib.pyplot as plt
# print(np.linspace(0, 1, 5))
# print(np.random.rand(3, 3))
# print(np.eye(4))
# print(np.random.randint(1, 100, (3, 3)))
# print(np.random.randn(3, 3))
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr[1, 2])
# print(arr[:,1])
# print(arr[0,:])
# arr = np.array([10, 20, 30, 40, 50])
# print(arr[1])
# print(arr[:3])
# print(arr[-2:])
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/2)
# print(np.dot(a,b))
# A = np.array([[1, 2], [3, 4]])
# B = np.array([[5, 6], [7, 8]])
# print(A @ B)
# print(np.dot(A, B))
# print(np.linalg.inv(A))
# print(np.linalg.det(A))
# arr = np.array([True, False, True, False])
# print(np.mean(arr))
# print(np.median(arr))
# print(np.var(arr)) # phương sai
# print(np.std(arr)) # độ lệch chuẩn
# print(np.sum(arr))
# print(np.max(arr))
# print(np.min(arr))
# arr = np.arange(1, 7)
# new_arr = arr.reshape(2, 3)
# print(new_arr)
# print(np.vstack((A, B)))
# print(np.hstack((A, B.T)))
# x = np.linspace(0, 10, 100)
# y = np.sin(x)
# plt.plot(x, y, label="sin(x)", color="b", linestyle="--", linewidth="2")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("biểu đồ hàm sin")
# plt.legend()
# plt.show()
# labels = ['A', 'B', 'C', 'D']
# values = [10, 20, 15, 25]
# plt.bar(labels, values, color=['red', 'blue', 'green', 'purple'], edgecolor='black')
# plt.xlabel('Class')
# plt.ylabel('Value')
# plt.title('Bar Chart')
# plt.show()
# labels = ['Apple', 'Samsung', 'Xiaomi', 'Oppo']
# sizes = [40, 30, 20, 10]
# colors = ['gold', 'lightblue', 'lightcoral', 'lightgreen']
# plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
# plt.title("Phone market")
# plt.show()
# x = np.random.rand(50)
# y = np.random.rand(50)
# plt.scatter(x, y, color="blue", marker="o", edgecolors='black')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Scatter chart')
# plt.show()
data = np.random.rand(1000)
plt.hist(data, bins=30, color="green", edgecolor="black")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# while True:
#     a = int(input("Nhập số a: "))
#     b = int(input("Nhập số b: "))
#     c = int(input("Nhập số c: "))
    
#     if a == 0:
#         print("a phải khác 0")
#         continue
    
#     delta = b**2 - 4*a*c
#     if delta < 0:
#         print("Phương trình vô nghiệm, mời nhập lại hệ số.")
#     else:
#         break

# x = np.linspace(-10, 10, 100)
# y = a*x**2 + b*x + c

# plt.plot(x, y, label=f"{a}x² + {b}x + {c} = 0", color="b", linestyle="--")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Đồ thị hàm bậc hai")
# plt.legend()
# plt.show()

# # Nguyễn Võ Hữu Tài - 24119189

