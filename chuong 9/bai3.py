# viết chương trình chỉ số BMI
def tinh_bmi(can_nang,chieu_cao):
    bmi = can_nang/(chieu_cao*chieu_cao)
    if bmi < 18.5:
        return "Gầy"
    if bmi > 18.5 and  bmi < 24.99:
        return "bình thường"
    if bmi >= 25:
        return "Thừa cân"
    
n = eval(input("Nhập cân nặng (kg):"))
m = eval(input("Nhập chiều cao (m):"))
print(tinh_bmi(n,m))