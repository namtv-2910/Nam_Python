# =========================
# In bảng cửu chương
# =========================

def bang_cuu_chuong(a, b):
    # Xác định khoảng từ a đến b
    if a < b:
        start = a
        end = b
    else:
        start = b
        end = a
    # In bảng cửu chương từ start đến end
    for i in range(start, end + 1):
        print(f"\n===== Bảng cửu chương {i} =====")
        for j in range(1, 11):
            print(f"{i} x {j} = {i*j}")


# Nhập dữ liệu
a, b = map(int, input("Nhập a,b (cách nhau bởi dấu phẩy): ").split(","))
# Gọi hàm in bang_cuu_chuong
bang_cuu_chuong(a, b)


#import math dùng để tính căn bậc hai của n trong hàm so_nguyen_to()
import math


# =========================
# Liệt kê số nguyên tố < n
# =========================
# Hàm kiểm tra số nguyên tố
def so_nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

# Hàm liệt kê số nguyên tố nhỏ hơn n
def liet_ke_snt(n):
    print("Các số nguyên tố nhỏ hơn", n, "là:")

    for i in range(2, n):
        if so_nguyen_to(i):
            print(i, end=" ")


# Nhập dữ liệu
n = int(input("\nNhập n: "))
# Gọi hàm liet_ke_snt
liet_ke_snt(n)

# =========================
# Liệt kê các ước số nguyên tố của n
# =========================
def uoc_so_nguyen_to(n):
    print("Các số vừa là ước số của", n, "vừa là số nguyên tố:")
    # Kiểm tra từng số từ 1 đến n xem có phải là ước số của n và là số nguyên tố hay không
    for i in range(1, n + 1):
        if n % i == 0 and so_nguyen_to(i):
            print(i, end=" ")


# Nhập dữ liệu
n = int(input("\nNhập n: "))
# Gọi hàm uoc_so_nguyen_to
uoc_so_nguyen_to(n)