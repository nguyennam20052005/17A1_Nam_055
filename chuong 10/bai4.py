# Sử dụng hàm pow
# Yêu cầu : viết lại bài tính A = (x^2 + x + 1)*n  + (x^2 - x + 1)^nbằng cách sử dụng hàm thư viện 
import math
x = eval(input("Nhập số x:"))
n = eval(input("Nhập số n:"))
A= (pow(x,2)+x+1)*n + (pow(x,2)-x+1)*n
print("bài tính a = (x^2 +x+1 là):", A)
print("bài tính a = (x^2 -x+1 là):", A)
