def tinh_can(nam):
    can = nam % 10
    if can == 0:
        return " canh "
    elif can == 1:
        return "Tân"
    elif can == 2:
        return "Nhâm"
    elif can == 3:
        return "Quý"
    elif can == 4:
        return "Giáp"
    elif can == 5:
        return "Ất"
    elif can == 6:
        return "Bính"
    elif can == 7:
        return "Đinh"
    elif can == 8:
        return "Mậu"
    elif can == 9:
        return "kỷ"
    
def tinh_chi(nam):
    chi = nam % 12
    if chi == 0:
        return "Thân"
    elif chi == 1:
        return " Dậu"
    elif chi == 2:
        return "Tuất"
    elif chi == 3:
        return "Hợi"
    elif chi == 4:
        return "Tý"
    elif chi == 5:
        return "Sửu"
    elif chi == 6:
        return "Dần"
    elif chi == 7:
        return "Mão"
    elif chi == 8:
        return "Thìn"
    elif chi == 9:
        return "Tỵ"
    elif chi == 10:
        return "Ngọ"
    elif chi == 11:
        return "Mùi"

can_nam = tinh_can(2017)
chi_nam = tinh_chi(2017)

print("Năm 2017 âm lịch là năm " + can_nam + chi_nam)
    
    

