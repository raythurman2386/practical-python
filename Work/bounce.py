# bounce.py
#
# Exercise 1.5
bounce = 1
height = 100

while bounce <= 10:
    height = height * (3/5)
    bounce += 1
    print(round(height, 4))
