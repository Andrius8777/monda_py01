print("Easy\ncalculator created by \nAndriusS \U0001F604" )
skaicius1 = float(input('Iveskite pirma skaiciu:'))
skaicius2 = float(input('Iveskite antra skaiciu:'))
rezultatas = skaicius1 + skaicius2
print(f'Atsakymas: {skaicius1} + {skaicius2} = {rezultatas}')
if rezultatas < 0:
    print(f'Jusu rezultatas: {rezultatas} yra neigiamas')
else:
    print(f'Jusu rezultas: {rezultatas} yra teigiamas')                  
