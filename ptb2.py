#tính phương trình bậc 2 Ax^2 + Bx + C = 0

with open("C:\\Users\\BACHDO\\Documents\\GitHub\\python\\input.txt","r",encoding="utf-8") as ptb2:
    a=float(ptb2.readline())
    b=float(ptb2.readline())
    c=float(ptb2.readline())
    d=b**2 - 4*a*c
    res=[]
    if a<=0:
        res.append("Đây không phải phương trình bậc 2")
    else:
        if d<0:
            res.append("Phương trình vô nghiệm")
        elif d==0:
            x=-b/(2*a)
            res.append(f"Phương trình có nghiệm kép x1=x2={x}")
        else:
            x1=(-b + d**0.5)/(2*a)
            x2=(-b - d**0.5)/(2*a)
            res.append(f"Phương trình có 2 nghiệm phân biệt x1={x1} và x2={x2}")

ptb2.close()

with open("C:\\Users\\BACHDO\\Documents\\GitHub\\python\\output.txt","w",encoding="utf-8") as ptb2_out:
    for line in res:
        ptb2_out.write(line)

