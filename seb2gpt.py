from getpass import getpass

class SaskaitosUzrakinta(Exception):
    pass

class Bankas:
    MAX_LOGIN_ATTEMPTS = 3

    def __init__(self, likutis=4000, pin_kodas=1234):
        self.__pin_kodas = pin_kodas
        self.__likutis = likutis
        self.login_attempts = self.MAX_LOGIN_ATTEMPTS

    def pino_nuskaitymas(self, pin_kodas):
        if self.__pin_kodas == pin_kodas:
            print('Jusu ivestas Pin kodas teisingas!!')
        else:
            self.login_attempts = self.MAX_LOGIN_ATTEMPTS
            self.login_attempts -= 1
            print(f"Ivestas neteisingas Pin kodas! Jums liko {self.login_attempts} bandymai")
            if self.login_attempts == 0:
                raise SaskaitosUzrakinta("Pasiektas maksimalus bandymų skaičius. Saskaita užblokuota.")

    # Other methods remain unchanged

# Rest of your code...

seb = Bankas()

while True:
    print("""
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
    try:
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
            pin_kodas = getpass(prompt='Įveskite esama Pin kodą: ')
            naujas_pin_kodas = getpass(prompt='Įveskite nauja Pin kodą: ')
            naujas_pin_kodas2 = getpass(prompt='Pakartokite nauja Pin kodą: ')
            if naujas_pin_kodas != naujas_pin_kodas2:
                print("Pin kodai nesutampa, bandykite is naujo")
                break
            else:
                print('Pin kodas sekmingai pakeistas')
        # Add other menu options as needed
    except SaskaitosUzrakinta as e:
        print(e)
        break
