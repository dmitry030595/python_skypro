def bank(x, y):
    for i in range(y):
        x *= 1.1
    print(round(x))


bank(1000, 10)
