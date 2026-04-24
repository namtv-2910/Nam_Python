#bai 1
def SumDigit(n):
    if n == 0:
        return 0
    else:
        return n % 10 + SumDigit(n // 10)
n = int(input("Nhập một số nguyên dương: "))
print("Tổng các chữ số của", n, "là:", SumDigit(n))


