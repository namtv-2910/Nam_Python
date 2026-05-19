"""
Bài 119 - Số Strobogrammatic
Dùng TWO POINTER (2 con trỏ)
"""

LIMIT = 1_000_000



def is_prime(n):

    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:
            return False

    return True



strob_map = { '0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

strob_map_ext = {'0': '0', '1': '1', '2': '2', '5': '5', '6': '9', '8': '8', '9': '6' }

# KIỂM TRA STROBOGRAMMATIC
def is_strobogrammatic(n, extended=False): # extended=False để chọn bảng xoay chuẩn hoặc mở rộng

    s = str(n)

    if extended:
        mp = strob_map_ext
    else:
        mp = strob_map

    left = 0
    right = len(s) - 1

    while left <= right:

        
        if s[left] not in mp:
            return False
        # xoay ký tự bên trái
        rotated = mp[s[left]]

        if rotated != s[right]:
            return False

        left += 1
        right -= 1

    return True



# LẤY SỐ SAU KHI XOAY 180 ĐỘ
def rotate_number(n, extended=False):

    s = str(n)

    # chọn bảng xoay
    if extended:
        mp = strob_map_ext
    else:
        mp = strob_map

    left = 0
    right = len(s) - 1

    result = [''] * len(s)

    while left <= right:

        # nếu ký tự không xoay được
        if s[left] not in mp:
            return None

        # xoay ký tự bên trái
        result[right] = mp[s[left]]

        # xử lý ký tự bên phải
        if s[right] not in mp:
            return None

        result[left] = mp[s[right]]

        left += 1
        right -= 1

    return int(''.join(result))


# =====================================================
# a. STROBOGRAMMATIC CHUẨN
# =====================================================
print("=" * 60)
print("a. Các số strobogrammatic chuẩn")
print("=" * 60)

result_a = []

for n in range(1, LIMIT):

    if is_strobogrammatic(n):
        result_a.append(n)

print(result_a)
print("Tổng:", len(result_a))


# =====================================================
# b. NGUYÊN TỐ STROBOGRAMMATIC CHUẨN
# =====================================================
print("\n" + "=" * 60)
print("b. Các số nguyên tố strobogrammatic chuẩn")
print("=" * 60)

result_b = []

for n in result_a:

    if is_prime(n):
        result_b.append(n)

print(result_b)
print("Tổng:", len(result_b))


# =====================================================
# c. STROBOGRAMMATIC MỞ RỘNG
# =====================================================
print("\n" + "=" * 60)
print("c. Các số strobogrammatic mở rộng")
print("=" * 60)

result_c = []

for n in range(1, LIMIT):

    if is_strobogrammatic(n, extended=True):
        result_c.append(n)

print(result_c)
print("Tổng:", len(result_c))


# =====================================================
# d. NGUYÊN TỐ STROBOGRAMMATIC MỞ RỘNG
# =====================================================
print("\n" + "=" * 60)
print("d. Các số nguyên tố strobogrammatic mở rộng")
print("=" * 60)

result_d = []

for n in result_c:

    if is_prime(n):
        result_d.append(n)

print(result_d)
print("Tổng:", len(result_d))


# =====================================================
# e. KHÔNG PHẢI STROBOGRAMMATIC
#    KHÔNG PHẢI NGUYÊN TỐ
#    NHƯNG SỐ XOAY LÀ NGUYÊN TỐ
# =====================================================
print("\n" + "=" * 60)
print("e. Không phải strobogrammatic,")
print("   không phải nguyên tố,")
print("   nhưng số xoay lại là nguyên tố")
print("=" * 60)

result_e = []

for n in range(2, LIMIT):

    # bỏ qua nếu là strobogrammatic
    if is_strobogrammatic(n):
        continue

    # bỏ qua nếu là nguyên tố
    if is_prime(n):
        continue

    # lấy số sau khi xoay
    rotated = rotate_number(n)

    # nếu xoay được
    if rotated is not None:

        # khác chính nó
        if rotated != n:

            # số xoay là nguyên tố
            if is_prime(rotated):

                result_e.append(n)

print(result_e)
print("Tổng:", len(result_e))