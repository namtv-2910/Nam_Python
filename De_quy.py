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

