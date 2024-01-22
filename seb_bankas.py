from getpass import getpass


class Bankas:
    def __init__(self, likutis = 4000, pin_kodas = 1234, bandymu_skaicius = 3):
        self.__pin_kodas = pin_kodas
        self.__likutis = likutis
        self.bandymu_skaicius = bandymu_skaicius

    def pino_nuskaitymas(self, pin_kodas):
        if self.__pin_kodas == pin_kodas:
            print('Jusu ivestas Pin kodas teisingas!!')
            self.bandymu_skaicius = 3  # Reset attempts on successful login
        else:
            self.bandymu_skaicius -= 1 
            print(f"Ivestas neteisingas Pin kodas! Jums liko bandymai")
            if self.bandymu_skaicius == 0:
                print("Pasiektas maksimalus bandymų skaičius. Saskaita užblokuota.")
            

    def pin_kodo_keitimas(self, naujas_pin_kodas):
        self.__pin_kodas = naujas_pin_kodas
        return naujas_pin_kodas
    

    def saskaitos_likutis(self):
        print(f'Jusu saskaitos likutis: {self.__likutis}')

    
    def pinigu_isgryninimas(self, suma):
         self.__likutis -= suma
         if self.__likutis < suma:
             print(f'Nepakanka lesu saskaitoj!')



       
seb = Bankas() #funkciju iskvietimui

while True:    
    print( """ 
                  \nMenu:
                  1. Saskaitos likutis
                  2. Pinigu isemimas
                  3. Pinigu idejimas
                  4. Pin kodo keitimas
                  5. Iseiti          
                  """)
    try:
        pasirinkimas = int(input("Pasirinkite Menu punkta: "))
    except ValueError:
        print('Prasau iveskite tik skaicius rinkdamiesi Menu punktus!!')
        continue
    if pasirinkimas == 5:
        print('Aciu, kad naudojates SEB banko paslaugomis. Iki kito karto!')
        break
    elif pasirinkimas > 6 or pasirinkimas == 0:
        print("Pasirinkote neegzistuojanti Menu punkta, bandykite dar karta! ")
        continue
    elif pasirinkimas == 1:
        pin_kodas = getpass(prompt='Įveskite Pin kodą: ')
        seb.pino_nuskaitymas(pin_kodas)     


    elif pasirinkimas == 2:
        suma = int(input(f'Iveskite suma: '))
        seb.pinigu_isgryninimas(suma)
    elif pasirinkimas == 4:
        pin_kodas = int(input('Įveskite esama Pin kodą: '))
        naujas_pin_kodas = int(input('Įveskite nauja Pin kodą: '))
        naujas_pin_kodas2 = int(input('Pakartokite nauja Pin kodą: '))
        if naujas_pin_kodas != naujas_pin_kodas2:
            print("Pin kodai nesutampa, bandykite is naujo")
            break
        else:
            seb.pin_kodo_keitimas(naujas_pin_kodas)
            print('Pin kodas pakeistas sekmingai!')
       

        
        
       