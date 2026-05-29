# =========================================
#  Kiểm tra n có là bội số của 13 hoặc 19
# =========================================
#hàm lambda để kiểm tra n có phải là bội số của 13 hoặc 19 hay không
kiem_tra = lambda n: n % 13 == 0 or n % 19 == 0
# Nhập dữ liệu
n = int(input("Nhập n: "))
# Gọi hàm kiểm tra và in kết quả
if kiem_tra(n):
    print(n, "là bội số của 13 hoặc 19")
else:
    print(n, "không phải là bội số của 13 hoặc 19")
    
# =========================================
# Kiểm tra loại tam giác
# =========================================
#hàm lambda để xác định loại tam giác dựa trên độ dài ba cạnh a, b, c
tam_giac = lambda a, b, c: (
    "Tam giác đều" if a == b == c else
    "Tam giác cân" if a == b or b == c or a == c else
    "Tam giác vuông" if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a else
    "Tam giác thường"
)
#hàm lambda để kiểm tra tính hợp lệ của ba cạnh a, b, c có thể tạo thành một tam giác hay không
hop_le = lambda a, b, c: a + b > c and a + c > b and b + c > a
# Nhập dữ liệu
a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))
# Gọi hàm kiểm tra và in kết quả

if hop_le(a, b, c):
    print("Đây là", tam_giac(a, b, c))
else:
    print("Ba cạnh không tạo thành tam giác")
