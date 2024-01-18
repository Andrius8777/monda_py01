def programa(x, y):
    try:
       rez = x / y
       print(f'Atsakymas: {rez:.2f}')
    except ZeroDivisionError:
        print(f'Error: skaicius: {x} negali dalintis is 0')


while True:
    try:
        x = float(input(f'Iveskite pirma skaiciu: '))
        y = float(input(f'Iveskite antra skaiciu: '))
        programa(x, y)
        break
    except ValueError:
        print(f'ivesta zodine reiksme')
        break