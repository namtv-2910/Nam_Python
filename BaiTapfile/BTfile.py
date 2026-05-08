def compress_text(text: str) -> str:
    """Giảm dung lượng bằng mã hóa độ dài chạy (run-length encoding)."""
    if not text:
        return ""

    compressed_parts = []
    prev_char = text[0]
    count = 1

    for ch in text[1:]:
        if ch == prev_char:
            count += 1
        else:
            compressed_parts.append(f"{count}{prev_char}")
            prev_char = ch
            count = 1

    compressed_parts.append(f"{count}{prev_char}")
    return ''.join(compressed_parts)


def decompress_text(compressed: str) -> str:
    """Giải mã run-length encoding về chuỗi ban đầu."""
    if not compressed:
        return ""

    decompressed = []
    count_chars = []

    for ch in compressed:
        if ch.isdigit():
            count_chars.append(ch)
        else:
            count = int(''.join(count_chars)) if count_chars else 1
            decompressed.append(ch * count)
            count_chars = []

    return ''.join(decompressed)


def main():
    input_file = 'test.txt'
    compressed_file = 'textnen.txt'
    restored_file = 'text_restored.txt'

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            original_text = f.read()
    except FileNotFoundError:
        print(f"Không tìm thấy '{input_file}'. Hãy tạo file này trước khi chạy chương trình.")
        return

    compressed_text = compress_text(original_text)
    with open(compressed_file, 'w', encoding='utf-8') as f:
        f.write(compressed_text)

    restored_text = decompress_text(compressed_text)
    with open(restored_file, 'w', encoding='utf-8') as f:
        f.write(restored_text)

    print(f"Đã nén '{input_file}' thành '{compressed_file}'")
    print(f"Đã giải nén trở lại và lưu vào '{restored_file}'")
    print(f"Kích thước gốc: {len(original_text)} ký tự")
    print(f"Kích thước nén: {len(compressed_text)} ký tự")


if __name__ == '__main__':
    main()
