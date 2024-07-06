def bank(x, y):
    rate = 0.1
    profit = round(x * (1 + rate) ** y)
    return profit


print(bank(300000, 5))


# вариант 2
def bank2(x2, y2):
    for i in range(1, y2 + 1):
        profit_in_period = x2 + (x2 * 0.1)
        x2 = profit_in_period
    return print(round(profit_in_period))


bank2(300000, 5)
