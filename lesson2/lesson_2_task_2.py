def is_year_leap(year):
    if year % 4 == 0:
        answer = True
    else:
        answer = False
    return f'год {year}: {answer}'


print(is_year_leap(2024))
print(is_year_leap(2023))
