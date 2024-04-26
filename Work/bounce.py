# bounce.py
#
# Exercise 1.5
height = 100
loss = 3/5
bounce_count = 0

while bounce_count < 10:
    height = height * loss
    bounce_count = bounce_count + 1
    print(bounce_count, round(height, 4))