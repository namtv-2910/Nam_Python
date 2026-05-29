

# Hàm tính diện tích đáy
def dien_tich_day(dai, rong):
    return dai * rong


# Hàm tính thể tích
def the_tich(dai, rong, cao):
    return dai * rong * cao


# Nhập dữ liệu
dai = float(input("Nhập chiều dài đáy hình khối chữ nhật (cm): "))
rong = float(input("Nhập chiều rộng đáy hình khối chữ nhật (cm): "))
cao = float(input("Nhập chiều cao hình khối chữ nhật (cm): "))

# số lượng số lẻ cần hiển thị sau dấu phẩy
so_le = int(input("Số lượng số lẻ cần hiển thị: "))

# Tính toán
dt_day = dien_tich_day(dai, rong)
tt = the_tich(dai, rong, cao)

# In kết quả với định dạng số lẻ đã nhập
print(f"Diện tích đáy hình chữ nhật = {dt_day:.{so_le}f} cm\u00b2")
print(f"Thể tích hình khối = {tt:.{so_le}f} cm\u00b3")