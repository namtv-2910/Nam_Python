# n = int(input("Nhập n: "))
# c = 0
# l = 0
# while n > 0:
#     tmp = n % 10
#     if tmp % 2 == 0:
#         c += 1
#     else:
#         l += 1
#     n //= 10
# print("Số lượng chữ số chẵn:", c)
# print("Số lượng chữ số lẻ:", l)

# # bài 5
# n1 = int(input("Nhập n: "))
# s = 0
# tich = 1
# while n1:
#     tmp = n1 % 10
#     s += tmp
#     tich *= tmp
#     n1 //= 10
# print("Tổng các chữ số:", s)
# print("Tích các chữ số:", tich)

# # bai 6
# n2 = int(input("Nhập n: "))
# res = -1e9
# while n2:
#     tmp = n2 % 10
#     if tmp > res:
#         res = tmp
#     n2 //= 10
# print("Chữ số lớn nhất:", res)

#bai 7

for i in range(0, 3):
    n = int(input("Nhập số cần kt: "))
    kt = True   # giả sử đúng trước

    while n > 0:
        tmp = n % 10
        if tmp != 6 and tmp != 8:
            kt = False
            break
        n //= 10

    if kt:
        print("là số may mắn")
    else:
        print("không là số may mắn")
    