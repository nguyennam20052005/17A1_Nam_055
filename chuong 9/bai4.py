# xây dựng phương thức tinh_S(n, x): với n và x là tham số truyền vào 
# phương thức có giá trị trả về là S = (x^2 +1)^n
def tinh_S(n, x):
    s = (x**2 + 1)**n
    return s

a = eval(input("nhập giá trị n:"))
b = eval(input("nhập giá trị x:"))
print(tinh_S(a, b))
