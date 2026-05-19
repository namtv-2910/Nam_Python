"""
Bài 121
a. Phát sinh tất cả số strobogrammatic gồm n chữ số
b. Phát sinh tất cả số strobogrammatic mở rộng gồm n chữ số
"""


def strobogrammatic_num(n):

    return generate(n, n)

def generate(n, length):

    if n == 0:
        return [""]

    if n == 1:
        return ["0", "1", "8"]

    middles = generate(n - 2, length)

    result = []

    for middle in middles:

        if n != length:
            result.append("0" + middle + "0")

        result.append("1" + middle + "1")
        result.append("8" + middle + "8")
        result.append("6" + middle + "9")
        result.append("9" + middle + "6")

    return result


def strobogrammatic_extend(n):

    return generate_extend(n, n)

def generate_extend(n, length):

    if n == 0:
        return [""]

    if n == 1:
        return ["0", "1", "2", "5", "8"]

    middles = generate_extend(n - 2, length)

    result = []

    for middle in middles:

        # Không cho số bắt đầu bằng 0
        if n != length:
            result.append("0" + middle + "0")

        result.append("1" + middle + "1")
        result.append("2" + middle + "2")
        result.append("5" + middle + "5")
        result.append("8" + middle + "8")
        result.append("6" + middle + "9")
        result.append("9" + middle + "6")

    return result


# =====================================================
# CHƯƠNG TRÌNH CHÍNH
# =====================================================

# Nhập n
n = int(input("Nhập n (2 <= n <= 10): "))

# Kiểm tra điều kiện
if n < 2 or n > 10:

    print("n không hợp lệ!")

else:


    print("\n" + "=" * 60)
    print("a. Các số strobogrammatic gồm", n, "chữ số")
    print("=" * 60)
    result_a = strobogrammatic_num(n)
    print(result_a)
    print("Tổng:", len(result_a))


    print("\n" + "=" * 60)
    print("b. Các số strobogrammatic MỞ RỘNG gồm", n, "chữ số")
    print("=" * 60)
    result_b = strobogrammatic_extend(n)
    print(result_b)
    print("Tổng:", len(result_b))