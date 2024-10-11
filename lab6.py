import math

def f(x):
    return x * math.sin(x) + math.exp(x)

a = float(input("Введіть початок інтервалу a: "))
b = float(input("Введіть кінець інтервалу b: "))
h = float(input("Введіть крок h: "))

#1
print("\n")

print("Табулювання за допомогою циклу for:")
x_values = []
for x in range(int((b - a) / h) + 1):
    x_curr = a + x * h
    x_values.append(f(x_curr))
    print(f"f({x_curr:.2f}) = {f(x_curr):.5f}")

#2
print("\n")

print("Табулювання за допомогою циклу while:")
x_values_while = []
x_curr = a
while x_curr <= b:
    x_values_while.append(f(x_curr))
    print(f"f({x_curr:.2f}) = {f(x_curr):.5f}")
    x_curr += h

#3
print("\n")

print("Значення функції у списку:")
print(x_values)

print("\n")

print("Відсортований список:")
x_values.sort()
print(x_values)
