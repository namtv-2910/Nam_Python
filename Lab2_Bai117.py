n = input("Nhập n: ")

S = 0

# Lấy tất cả số con
for i in range(len(n)):
    for j in range(i + 1, len(n) + 1):
        sub = n[i:j]      # cắt chuỗi
        so = int(sub)     # đổi thành số
        S += so ** 2      # cộng bình phương

print("Tổng S =", S)