# cd = float(input(u'Nhập chiều dài đáy hình chữ nhật: '))
# cr = float(input(u'Nhập chiều rộng đáyhình chữ nhật: '))
# ch = float(input(u'Nhập chiều cao hình khối chữ nhật: '))
# a = int(input(u'Nhập số lượng số lẻ cần hiển thị : '))
# sdt = cd * cr
# stp = 2 * (cd * ch + cr * ch) + sdt
# v = sdt * ch

# print(u'Diện tích đáy hình chữ nhật là: {:.{a}f}cm\u00b2'.format(sdt, a=a))
# print(u'Thể tích hình khối chữ nhật là: {:.{a}f}cm\u00b3 '.format(v, a=a))

# # BÀI 2

# a = int(input(u'Nhập số nguyên a : '))
# b = int(input(u'Nhập số nguyên b : '))
# c = int(input(u'Nhập số nguyên c : '))

# so_lon_nhat = max(a, b, c)
# so_nho_nhat = min(a, b, c)
# print(u'3 số tăng dần là: {}, {}, {}'.format(so_nho_nhat, (a + b + c) - (so_lon_nhat + so_nho_nhat), so_lon_nhat))

# bài 3
a = int(input(u'Nhập số nguyên a : '))
print('{x} + {y} + {z} = {s}'.format(x=a, y=a*11, z=a*111, s=a + a*11 + a*111))