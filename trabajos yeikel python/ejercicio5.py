a = float(input("Lado 1: "))
b = float(input("Lado 2: "))
c = float(input("Lado 3: "))

if a == b and b == c:
    print("Equilatero")
elif a == b or a == c or b == c:
    print("Isosceles")
else:
    print("Escaleno")