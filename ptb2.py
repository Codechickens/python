#phương trình bậc 2 Ax^2 + Bx + C = 0
A= float(input("Nhập hệ số A: "))
B= float(input("Nhập hệ số B: "))
C= float(input("Nhập hệ số C: "))
D= B**2 - 4*A*C
if D < 0:
    print("Phương trình vô nghiệm")
elif D == 0:
    x= -B/(2*A)
    print("Phương trình có nghiệm kép x1 = x2 =", x)
else:
    x1= (-B + D**0.5)/(2*A)
    x2= (-B - D**0.5)/(2*A)
    print("Phương trình có hai nghiệm phân biệt:")
    print("x1 =", x1)
    print("x2 =", x2)