x = int(input("a:"))
y = int(input("b:"))
z = int(input("c:"))

delta = y ** 2 - 4 * x *z

x1 = (-y - delta ** 0.5 ) / (2 * x)
x2 = (-y + delta ** 0.5 ) / (2 * x)

print("Birinci Kök: {}\nİkinci Kök: {}\n".format(x1,x2))

