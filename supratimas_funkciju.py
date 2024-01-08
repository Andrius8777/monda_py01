
def imoku_ivedimas(pajamos, imoku_pav, suma_teigiama):
    if imoku_pav in pajamos:
        pajamos[imoku_pav] += suma_teigiama
    else:
        pajamos[imoku_pav] = suma_teigiama
    return pajamos[imoku_pav]

def islaidu_ivedimas(pajamos, islaidu_pav, suma_neigiama):
    if islaidu_pav in pajamos:
        pajamos[islaidu_pav] += suma_neigiama
    else:
        pajamos[islaidu_pav] = suma_neigiama
    return pajamos[islaidu_pav]

def ataskaita(pajamos):
    print("Jusu ataskaita imoku:")
    for index, (imoku_pav, suma_teigiama) in enumerate(pajamos.items()):
        print(f'{index}: {imoku_pav.upper():<10}: {suma_teigiama:^10.2f}')
   
def ataskaita(pajamos):
    print("Jusu ataskaita islaidu:")
    for index, (islaidu_pav, suma_neigiama) in enumerate(pajamos.items()):
        print(f'{index}: {islaidu_pav.upper():<10}: {suma_neigiama:^10.2f}')
          
def balansas_teigiamas(pajamos):
    balansas_teigiamas = 0
    for suma_teigiama, suma_neigiama in pajamos.values():
        balansas_teigiamas += suma_neigiama
    return balansas_teigiamas

def balansas_neigiamas(pajamos):
    balansas_neigiamas = 0
    for suma_neigiama in pajamos.values():
        balansas_neigiamas += suma_neigiama
    return balansas_neigiamas



pajamos = {}

while True:
    print(""" 
          === Biudzeto skaiciuokle \u20AC===
          MENU:
          0: "EXIT"
          1: "Imokos"
          2: "Islaidos"
          3: "Ataskaita"
          4: "Balansas"
        """)
    pasirinkimas = input('Pasirinkite Menu punkta: ')
    if pasirinkimas == '0':
        break
    elif pasirinkimas == '1':  #imokos
        while True:
            imoku_pav = input('Iveskite sio menesio gautu pajamu pavadinima: ')
            if imoku_pav.isnumeric():
                print('Klaida: "Prasau iveskite zodines reiksmes" ')
            else:
                break
        while True:
            sumos_ivedimas = input('Įveskite gauta pinigu sumą: ')
            try:
                suma_teigiama = float(sumos_ivedimas)
                break
            except ValueError:
                print('Įvesti duomenys netinka. Prašome įvesti skaičių.')
        imoku_ivedimas(pajamos, imoku_pav, suma_teigiama)
        print(f'====  {imoku_pav.upper()}:{suma_teigiama:>10.2f}  ====')
    elif pasirinkimas == '2':   #2 islaidos
        while True:
            islaidu_pav = input('Iveskite sio menesio isleistu pajamu pavadinima: ')
            if islaidu_pav.isnumeric():
                print('Klaida: "Prasau iveskite zodines reiksmes" ')
            else:
                break
        while True:
            sumos_ivedimas = input('Įveskite isleista pinigu sumą: ')
            try:
                suma_neigiama = float(sumos_ivedimas)
                break
            except ValueError:
                print('Įvesti duomenys netinka. Prašome įvesti skaičių.')
        islaidu_ivedimas(pajamos, islaidu_pav, suma_neigiama)
        print(f'====  {islaidu_pav.upper()}:{suma_neigiama:>10.2f}  ====')
    if pasirinkimas == '3':
        ataskaita(pajamos)
    elif pasirinkimas == '4':
        balansas = balansas_teigiamas(pajamos)
        balansas2 = balansas_neigiamas(pajamos)
        if balansas > 0:
            print(f'Jus esate "Bomzaras" Jusu saskaitoj: {balansas2}!')
        else:
            balansas2 < 0 
            print(f'Jusu balansas yra: {balansas}! Jus esate turtingas Mulkis!')


    


