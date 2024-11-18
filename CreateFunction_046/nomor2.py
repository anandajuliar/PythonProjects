import math

luas_lingkaran = lambda r : math.pi *r **2

radius = float(input("enter the radius:"))
area = luas_lingkaran(radius)
print(f"luas lingkaran dengan radius {radius}:{area}")