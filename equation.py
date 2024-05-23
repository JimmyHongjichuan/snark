import d

a = float(input("请输入二次项系数："))
b = float(input("请输入一次项系数："))
c = float(input("请输入常数项："))
d = b**2-4*a*c
if a == 0:
    x = -b/c
    print(x)
elif d >= 0:
    e = d**0.5
    x1 = (-b+e)/(2*a)
    x2 = (-b-e)/(2*a)
    print("方程的两根分别为：", x1, x2)
else:
    print("此方程无根")