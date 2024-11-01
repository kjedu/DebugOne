def lone_sum(a, b, c):
    if a == b and a == c and b == c:
        return 0
    elif a >= b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    else:
        return a+b+c

print("lone_sum of 10, 10, 10 should be 0: " + str(lone_sum(10, 10, 10)))
print("lone_sum of 1, 2, 3 should be 6: " + str(lone_sum(1, 2, 3)))
print("lone_sum of 1, 2, 1 should be 2: " + str(lone_sum(1, 2, 1)))
print("lone_sum of 4, 5, 6 should be 15: " + str(lone_sum(4, 5, 6)))
