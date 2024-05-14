import matplotlib.pyplot as plt

print("введите x1")
x1 = int(input())
print("введите y1")
y1 = int(input())
print("введите x2")
x2 = int(input())
print("введите y1")
y2 = int(input())
print("введите x3")
x3 = int(input())
print("введите y3")
y3 = int(input())
ya = [y1, y2, y3]
xa = [x1, x2, x3]
plt.plot(xa, ya)
plt.show()
