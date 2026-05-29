#=======================================
#Số đồng nhất: các chữ số đều giống nhau
#=======================================
so_dong_nhat_all = lambda n: all(ch == str(n)[0] for ch in str(n))
so_dong_nhat_any = lambda n: not any(ch != str(n)[0] for ch in str(n))
print("\n Số đồng nhất :")
# In ra tất cả số đồng nhất nhỏ hơn 10000
print([i for i in range(1, 10001) if so_dong_nhat_any(i)])
print([i for i in range(1, 10001) if so_dong_nhat_all(i)])

#=======================================
#Số hoàn thiện: tổng ước số nguyên dương (không kể chính nó) bằng chính nó
#=======================================
so_hoan_thien = lambda n: n > 1 and sum(i for i in range(1, n // 2 + 1) if n % i == 0) == n
print("\nSố hoàn thiện:")
# In ra tất cả số hoàn thiện nhỏ hơn 10000
print([i for i in range(1, 10001) if so_hoan_thien(i)])