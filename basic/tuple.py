# tuple(タプル): 変更できないリスト []ではなく()を使う

date_of_birth = (1990, 2, 3)
# date_of_birth = [1990, 2, 3]
# date_of_birth[0] = 1999
print(date_of_birth)

year, month, date = date_of_birth
print(year)
print(month)
print(date)