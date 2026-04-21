from datetime import datetime

now = datetime.now()

print("Năm hiện tại:", now.year)
print("Tháng hiện tại bằng chữ:", now.strftime("%B"))
print("Tuần hiện tại là tuần thứ mấy trong năm:", now.isocalendar()[1])
print("Tuần trong tháng:", (now.day - 1)//7 + 1)
print("Ngày trong năm:", now.timetuple().tm_yday)
print("Ngày:", now.day)
print("Thứ:", now.strftime("%A"))
print("Giờ:", now.strftime("%H:%M:%S"))
print("Giờ hiện tại bằng 12h:", now.strftime("%I:%M:%S %p"))