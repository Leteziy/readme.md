def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


print(is_year_leap(2025))


year1 = 2020
result = is_year_leap(year1)
print(f"Год {year1}: {result}")
