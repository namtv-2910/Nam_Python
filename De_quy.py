#bai 1
def SumDigit(n):
    if n == 0:
        return 0
    else:
        return n % 10 + SumDigit(n // 10)
n = int(input("Nhập một số nguyên dương: "))
print("Tổng các chữ số của", n, "là:", SumDigit(n))

#bai 2
def Gt(n):
    if n == 0:
        return 1
    else:
        return n * Gt(n - 1)
n = int(input("Nhập một số nguyên dương: "))
print("Giai thừa của", n, "là:", Gt(n))

#bai 3
def luy_thua(x, n):
    if n == 0:
        return 1
    else:
        return x * luy_thua(x, n - 1)
a = int(input("Nhập cơ số: "))
b = int(input("Nhập số mũ: "))
print(a, "^", b, "=", luy_thua(a, b))

#bai 4
def gcd(a, b):
    if b == 0:
        return a
    else: 
        return gcd(b, a%b)
a = int(input("Nhập số nguyên dương thứ nhất: "))
b = int(input("Nhập số nguyên dương thứ hai: "))
print("Ước chung lớn nhất của", a, "và", b, "là:", gcd(a, b))

#bai 5
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("Nhập một số nguyên dương: "))
print("Số Fibonacci thứ", n, "là:", fibonacci(n))