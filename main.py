a = int(input("Enter side A: "))
b = int(input("Enter side B: "))
c = int(input("Enter side C: "))
d = int(input("Enter side D: "))
e = int(input("Enter side E: "))


areaOne = 1.0 * a * b
areaTwo = (a-c) * (d-e-b)
areaThree = 0.5 * (a-c) * e

print()
print("Room Area: " + str(areaOne + areaTwo +areaThree))
