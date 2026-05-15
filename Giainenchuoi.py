def decode(cipher_text):
    result = []
    i = 0
    while i < len(cipher_text):
        if cipher_text[i] == '#':
            count = int(cipher_text[i + 1])   # chữ số tiếp theo
            char  = cipher_text[i + 2]         # ký tự cần lặp
            result.append(char * count)
            i += 3
        else:
            result.append(cipher_text[i])
            i += 1
    return ''.join(result)

# --- Kiểm tra ---
print(decode("XY#6Z1#4023"))   # → XYZZZZZZ1000023
print(decode("#39+1=1#30"))