def is_year_leap(year):
    if year % 4 == 0:
        result = f"год {year}: True"
    else:
        result = f"год {year}: False"
    print(result)


is_year_leap(2008)
