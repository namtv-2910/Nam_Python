import math

# Nhap n
print("Nhap mot so nguyen duong n: ")
n = int(input())

# a) So than thien: GCD cua n va đao nguoc n bang 1
so_than_thien = lambda n: math.gcd(n, int(str(n)[::-1])) == 1
print("So than thien:")
print([i for i in range(1, n + 1) if so_than_thien(i)])

# b) S0 chinh phuong
so_chinh_phuong = lambda n: int(math.sqrt(n)) ** 2 == n
print("\nb) So chinh phuong:")
print([i for i in range(1, n + 1) if so_chinh_phuong(i)])

# c) So đong nhat: cac chu so đeu giong nhau
so_dong_nhat_all = lambda n: all(ch == str(n)[0] for ch in str(n))
so_dong_nhat_any = lambda n: not any(ch != str(n)[0] for ch in str(n))
print("\nc) So dong nhat:")
print([i for i in range(1, n + 1) if so_dong_nhat_any(i)])
print([i for i in range(1, n + 1) if so_dong_nhat_all(i)])

# d) So hoan thien: tong uoc khong ke chinh no bang n
so_hoan_thien = lambda n: n > 1 and sum(i for i in range(1, n // 2 + 1) if n % i == 0) == n
print("\nSo hoan thien:")
print([i for i in range(1, n + 1) if so_hoan_thien(i)])

# e) So phong phu: tong uoc khong ke chinh no lon hon n
so_phong_phu = lambda n: n > 1 and sum(i for i in range(1, n // 2 + 1) if n % i == 0) > n
print("\n So phong phu:")
print([i for i in range(1, n + 1) if so_phong_phu(i)])

# f) So tang dan: chu so tu trai sang phai khong giam
so_tang_dan = lambda n: (
    (lambda s: all(s[i] <= s[i + 1] for i in range(len(s) - 1)))(str(n))
)
print("\n So tang dan:")
print([i for i in range(1, n + 1) if so_tang_dan(i)])

# g) So Armstrong
so_armstrong = lambda n: sum(int(ch) ** len(str(n)) for ch in str(n)) == n
print("\n So Armstrong:")
print([i for i in range(1, n + 1) if so_armstrong(i)])

# h) So nguyen to
so_nguyen_to = lambda n: n > 1 and not any(n % i == 0 for i in range(2, int(math.sqrt(n)) + 1))
print("\n So nguyen to:")
print([i for i in range(1, n + 1) if so_nguyen_to(i)])

# i) So Palindrome
so_palindrome = lambda n: str(n) == str(n)[::-1]
print("\n So Palindrome:")
print([i for i in range(1, n + 1) if so_palindrome(i)])

# j) So nguyen to Palindrome
so_nguyen_to_palindrome = lambda n: so_nguyen_to(n) and so_palindrome(n)
print("\n So nguyen to Palindrome:")
print([i for i in range(1, n + 1) if so_nguyen_to_palindrome(i)])

# k) So loc phat: chi chua so 6 hoac 8
so_loc_phat_all = lambda n: all(ch in "68" for ch in str(n))
so_loc_phat_dem = lambda n: str(n).count("6") + str(n).count("8") == len(str(n))
print("\n So loc phat:")
print([i for i in range(1, n + 1) if so_loc_phat_all(i)])

# l) So loc phat Palindrome
so_loc_phat_palindrome = lambda n: so_loc_phat_all(n) and so_palindrome(n)
print("\n So loc phat Palindrome:")
print([i for i in range(1, n + 1) if so_loc_phat_palindrome(i)])