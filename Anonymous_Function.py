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
#cau e
r = float(input("Nhập bán kính hình tròn: "))
tinh_chu_vi = lambda r: 2 * pi * r
tính_dien_tich = lambda r: pi * r ** 2
print("Chu vi hình tròn là: %.2f" % tinh_chu_vi(r))
print("Diện tích hình tròn là: %.2f" % tính_dien_tich(r))
