import math

def create_point(x, y):
    return (x, y)

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

x1 = float(input("Piste 1, x: "))
y1 = float(input("Piste 1, y: "))
p1 = create_point(x1, y1)

x2 = float(input("Piste 2, x: "))
y2 = float(input("Piste 2, y: "))
p2 = create_point(x2, y2)

d = distance(p1, p2)
print(f"Etäisyys: {d:.2f}")