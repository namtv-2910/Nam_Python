from datetime import datetime

s = input("Nhập (vd: Sep 18 2019 2:43PM): ")
d = datetime.strptime(s, "%b %d %Y %I:%M%p")

print(d)