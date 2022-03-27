liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
kwadraty = [lambda x=x: x**2 for x in liczby]
for kwadrat in kwadraty:
    print(kwadrat())
szesciany = [lambda x=x: x**3 for x in liczby]
for szescian in szesciany:
    print(szescian())