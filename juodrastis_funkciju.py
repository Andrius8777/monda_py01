def kvadratu(skaicius_x):
    return skaicius_x ** 2

def saknis_kvadratu(skaicius_x):
    return skaicius_x ** (1/2)

a = {}

while True:
    print(""" ====== MINI SKAICIUOTUVAS =======
          0. ISEITI IS PROGRAMOS
          1. Kelimas kvadratu
          2. Kvadratines saknies istraukimas """)
    ivestis = int(input('Iveskite Menu punkta: '))
    if ivestis == 0:
        print(f'Iki kito karto!!!')
        break
    elif ivestis == 1:
        skaicius_x = float(input('Iveskite skaiciu kvadrato kelimui: '))
        atsakymas = kvadratu(skaicius_x)
        print(f'Ivestas skaicius "{skaicius_x}" \nATSAKYMAS = {atsakymas:.2f}')
        if atsakymas > 1000:
            print(f'Jus gavote dideli skaiciu: {atsakymas:.2f}')
        else:
            print(f'Jusu pasirinktas skaicius galejo buti ir didesnis!')
    elif ivestis == 2:
        skaicius_x = float(input('Iveskite skaiciu saknies traukimui: '))
        atsakymas = saknis_kvadratu(skaicius_x)
        print(f'{atsakymas}')
    elif ivestis == 3:
        print(f'Prasau iveskite tinkama Menu punkta!')
    
 
