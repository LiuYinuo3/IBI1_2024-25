a = 15
b = 75
c = a + b
d = 90
e = 5
f = d + e
if c > f:
    print("taking the bus is quicker")
elif c < f:
    print("driving the car is quicker")
else:
    print("driving the car and taking the bus take the same time")
# driving the car is quicker

X = True
Y = False
W = X and Y
print(W)
# truth table
# X     Y     W
# True  True  True
# True  False False
# False True  False
# False False False