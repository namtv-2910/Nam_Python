# Nhập số điện thoại
s = input("Nhập số điện thoại (S): ")

# Tập hợp tất cả các chữ số từ 0-9
all_digits = set('0123456789')

# Tập hợp các chữ số có trong số điện thoại
phone_digits = set(s)

# Tìm các chữ số không có trong số điện thoại
missing_digits = all_digits - phone_digits

# In kết quả
if missing_digits:
    print(f"Trong số điện thoại {s} không chứa các ký số: {sorted([int(d) for d in missing_digits])}")
else:
    print(f"Số điện thoại {s} chứa tất cả các chữ số từ 0-9")
