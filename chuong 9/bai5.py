# xây dựng phương thức tinh A(n, x): với n và x là tham số truyền vào 
# phương thức có giá trị trả về là A = (x^2+x+1)^n+(x^2-x+1)^n
def tinhA(n, x):
     a = (x**2 + x + 1)**n + (x**2 - x + 1)**n
     return a
a = eval(input("nhập giá trị n:"))
b = eval(input("nhập giá trị x:"))
print(tinhA(a, b))
