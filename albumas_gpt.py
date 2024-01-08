class Albumas:
    def __init__(self, atlikejas, pavadinimas):
        self.atlikejas = atlikejas
        self.pavadinimas = pavadinimas
        self.takeliai = []

    def uzpildyti_informacija(self):
        self.atlikejas = input("Įveskite atlikėją: ")
        self.pavadinimas = input("Įveskite albumo pavadinimą: ")

    def prideti_takeli(self, eiles_numeris, pavadinimas, trukme):
        takelis = {'eiles_numeris': eiles_numeris, 'pavadinimas': pavadinimas, 'trukme': trukme}
        self.takeliai.append(takelis)

    def istrinti_takeli(self, eiles_numeris):
        self.takeliai = [takelis for takelis in self.takeliai if takelis['eiles_numeris'] != eiles_numeris]

    def perziureti_albuma(self):
        print(f"Atlikėjas: {self.atlikejas}")
        print(f"Albumo pavadinimas: {self.pavadinimas}")
        print(f"Takelių kiekis: {len(self.takeliai)}")
        trukme_sekundemis = sum([takelis['trukme'] for takelis in self.takeliai])
        trukme_minutes, trukme_sekundes = divmod(trukme_sekundemis, 60)
        print(f"Bendra takelių trukmė: {trukme_minutes} min {trukme_sekundes} sek")

    def perziureti_dainas(self):
        print("Dainų sąrašas:")
        for takelis in sorted(self.takeliai, key=lambda x: x['eiles_numeris']):
            trukme_minutes, trukme_sekundes = divmod(takelis['trukme'], 60)
            print(f"Eil. Nr.: {takelis['eiles_numeris']} | Pavadinimas: {takelis['pavadinimas']} | Trukmė: {trukme_minutes} min {trukme_sekundes} sek")


# Pavyzdys, kaip naudoti klasę Albumas:
if __name__ == "__main__":
    albumas = Albumas(atlikejas="", pavadinimas="")
    albumas.uzpildyti_informacija()

    albumas.prideti_takeli(1, "Daina1", 180)
    albumas.prideti_takeli(2, "Daina2", 210)

    albumas.perziureti_albuma()
    albumas.perziureti_dainas()