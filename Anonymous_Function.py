from math import *
# n = int(input("Nhập một số nguyên: "))
# #cau a
# tinh_tuyet_doi = lambda x: abs(x)
# print("Giá trị tuyệt đối của", n, "là:", tinh_tuyet_doi(n))

# #cau b
# tinhb = lambda x: x + 15
# print("Kết quả của n + 15 là:", tinhb(n))

# #cau c
# tinh_tich = lambda x, y: x * y
# print("%d * %d = %d" % (2, 3, tinh_tich(2, 3)))

# #cau d
# def kt_boi_so(x):
#     if x % 13 == 0 or x % 19 == 0:
#         return True
# kiem_tra = lambda x: str(x) + " là bội số của 13 hoặc 19" if kt_boi_so(x) else str(x) + " không phải là bội số của 13 hoặc 19"
# print(kiem_tra(n))

# #cau e
# r = float(input("Nhập bán kính hình tròn: "))
# tinh_chu_vi = lambda r: 2 * pi * r
# tính_dien_tich = lambda r: pi * r ** 2
# print("Chu vi hình tròn là: %.2f" % tinh_chu_vi(r))
# print("Diện tích hình tròn là: %.2f" % tính_dien_tich(r))

# #cau f
# d = float(input("Nhập chiều dài hình chữ nhật: "))
# r = float(input("Nhập chiều rộng hình chữ nhật: "))
# tinh_dien_tich = lambda d, r: d * r
# print("Diện tích hình chữ nhật là: %.2f" % tinh_dien_tich(d, r))

# #cau g
# def chinh_phuong(n):
#     can = isqrt(n)
#     return can * can == n
# kiem_tra_chinh_phuong = lambda n: str(n) + " là số chính phương" if chinh_phuong(n) else str(n) + " không phải là số chính phương"
# print(kiem_tra_chinh_phuong(n))

# # cau h
# def so_nguyen_to(n):
#     if n < 2:
#         return False
#     for i in range(2, int(sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True
# kiem_tra_nguyen_to = lambda n: str(n) + " là số nguyên tố" if so_nguyen_to(n) else str(n) + " không phải là số nguyên tố"
# print(kiem_tra_nguyen_to(n))

#cau i
def tam_giac(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return True

def kiem_tra_tam_giac(a, b, c):
    if a == b == c:
        return "Tam giác đều"
    elif a == b or b == c or a == c:
        return "Tam giác cân"
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return "Tam giác vuông"
    else:
        return "Tam giác thường"
a = float(input("Nhập cạnh a của tam giác: "))
b = float(input("Nhập cạnh b của tam giác: "))
c = float(input("Nhập cạnh c của tam giác: "))
kiem_tra = lambda a, b, c: "Không phải là tam giác" if tam_giac(a, b, c) == False else kiem_tra_tam_giac(a, b, c)
print(kiem_tra(a, b, c))