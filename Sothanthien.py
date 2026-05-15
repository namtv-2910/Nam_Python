from math import gcd

def f(x):
    return int(str(x)[::-1])
def main():
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))
    cnt = 0
    for x in range(a, b ):
        if gcd(x, f(x)) == 1:
            cnt += 1
            print(x, f(x))
    print(cnt)
main()