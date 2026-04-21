#bai2
from datetime import datetime

d1 = datetime.strptime(input("Nhập ngày 1 (dd/mm/yyyy): "), "%d/%m/%Y")
d2 = datetime.strptime(input("Nhập ngày 2 (dd/mm/yyyy): "), "%d/%m/%Y")

print("Số ngày:", abs((d2 - d1).days))