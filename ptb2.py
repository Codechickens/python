# Giải phương trình bậc 2: Ax^2 + Bx + C = 0
# Đọc hệ số từ file input.txt

try:
    # Đọc input từ file
    with open("C:\\Users\\BACHDO\\Documents\\GitHub\\python\\input.txt", "r", encoding="utf-8") as input_file:
        lines = input_file.readlines()
        A = float(lines[0].strip())
        B = float(lines[1].strip())
        C = float(lines[2].strip())
    
    # Tính delta (biệt thức)
    D = B**2 - 4*A*C
    
    # Giải và chuẩn bị kết quả
    results = []
    results.append(f"Chương trình giải phương trình bậc 2: Ax^2 + Bx + C = 0")
    results.append(f"Hệ số: A={A}, B={B}, C={C}")
    results.append(f"Delta (Δ) = {D}\n")
    if A <= 0:
        results.append("Lỗi: Hệ số A phải khác 0 để là phương trình bậc 2.")
    else:
        if D < 0:
            results.append("Kết quả: Phương trình vô nghiệm (Δ < 0)")
        elif D == 0:
            x = -B / (2*A)
            results.append(f"Kết quả: Phương trình có nghiệm kép")
            results.append(f"x1 = x2 = {x}")
        else:
            x1 = (-B + D**0.5) / (2*A)
            x2 = (-B - D**0.5) / (2*A)
            results.append(f"Kết quả: Phương trình có hai nghiệm phân biệt")
            results.append(f"x1 = {x1}")
            results.append(f"x2 = {x2}")
        
    # Ghi kết quả vào file output
    with open("C:\\Users\\BACHDO\\Documents\\GitHub\\python\\output.txt", "w", encoding="utf-8") as output_file:
        output_file.write("\n".join(results))
    
    # Cũng in ra console
    print("\n".join(results))
    print("\n✓ Kết quả đã được lưu vào output.txt")
    
except FileNotFoundError:
    print("Lỗi: Không tìm thấy file input.txt!")
    print("Vui lòng tạo file input.txt với ba dòng chứa hệ số A, B, C")
    print("\nVí dụ input.txt:")
    print("1")
    print("2")
    print("1")
except ValueError:
    print("Lỗi: Dữ liệu không hợp lệ! Vui lòng nhập đúng số")
except Exception as e:
    print(f"Lỗi: {e}")