def bank(a, years):
    for i in range(years):
        a += a * 10 / 100
    return a


print(bank(1000, 5))
