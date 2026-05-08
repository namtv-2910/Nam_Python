# Nhập chuỗi
S = input("Nhập chuỗi (S): ")

# Split thành các từ
words = S.split()

# Tập hợp để theo dõi các từ đã gặp
seen = set()

# Tìm từ đầu tiên lặp lại
first_repeated = None

for word in words:
    if word in seen:
        first_repeated = word
        break
    seen.add(word)

# In kết quả
print(first_repeated)
