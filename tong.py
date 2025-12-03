#tính tổng từ 0 đến một số nguyên n
s=0
with open("C:\\Users\\BACHDO\\Documents\\GitHub\\python\\input2.txt","r",encoding="utf-8") as sum:
    n=int(sum.read())
    for i in range(n+1):
        s+=i
sum.close()

with open("C:\\Users\\BACHDO\\Documents\\GitHub\\python\\output2.txt","w",encoding="utf-8") as sum1:
    sum1.write(f"Tổng từ 0 đến {n} là: {s}")