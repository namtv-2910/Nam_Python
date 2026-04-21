#bài 6
s = input("Nhập một chuỗi: ")
tu = input("Nhập một từ: ")
print("Số từ {} trong chuỗi là: {}".format(tu, s.count(tu)))

#bài 13
s = """   Quê  hương
Quê  hương  là  chùm khế  ngọt .
   Cho  con trèo hái mỗi  ngày .
Quê  hương là   đường  đi học .
Con  về rợp  bướm vàng bay .
   Đỗ   Trung Quân   """

lines = s.split('\n')
result = []

for line in lines:
    line = line.strip()          # bỏ khoảng trắng đầu/cuối
    words = line.split()         # tách từ

    new_line = ""
    for word in words:
        if word == "." or word == ",":
            new_line = new_line.rstrip() + word   # dính dấu câu
        else:
            new_line += word + " "

    result.append(new_line.strip())

# in kết quả
for line in result:
    print(line)
