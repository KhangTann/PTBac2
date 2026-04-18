import math

def giai_phuong_trinh_bac_2(a, b, c):
    # Kiểm tra nếu a = 0 thì phương trình trở thành bậc nhất bx + c = 0
    if a == 0:
        if b == 0:
            if c == 0:
                return "Phương trình có vô số nghiệm."
            else:
                return "Phương trình vô nghiệm."
        else:
            return f"Phương trình có một nghiệm duy nhất: x = {-c / b}"

    # Tính delta
    delta = b**2 - 4*a*c
    print(f"Delta (Δ) = {delta}")

    # Biện luận nghiệm dựa trên delta
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"Phương trình có 2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}"
    elif delta == 0:
        x = -b / (2 * a)
        return f"Phương trình có nghiệm kép: x1 = x2 = {x}"
    else:
        return "Phương trình vô nghiệm (trên tập số thực)."

# Nhập dữ liệu từ người dùng
try:
    print("--- Giải phương trình bậc 2: ax^2 + bx + c = 0 ---")
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    c = float(input("Nhập c: "))

    ket_qua = giai_phuong_trinh_bac_2(a, b, c)
    print(ket_qua)
except ValueError:
    print("Vui lòng nhập số hợp lệ!")