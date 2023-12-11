def find_my_age(years, months, days):
    my_age = (years*365) + (months*30) + days
    return my_age
print(find_my_age(11, 3, 5))