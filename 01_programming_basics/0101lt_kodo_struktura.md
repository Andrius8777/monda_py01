# Python programavimo principai

Python yra programavimo kalba, kuri remiasi tam tikrais principais ir taisyklėmis.

## Kodo ir blokų struktūra

Python kodo struktūra yra labai svarbi, nes ji nusako, kaip kodo eilutės turi būti struktūrizuotos ir kiek reikia naudoti įtraukas (indentation). Python nenaudoja skliaustų ar kabliatūros, kad atskirtų blokus. Vietoj to, Python naudoja įtraukas, kurios turi būti tuo pačiu atstumu nuo kairės eilutės.

Pavyzdžiui, šis kodas yra teisingai struktūrizuotas:

```Python
if x > 0:
    print("x yra teigiamas")
else:
    print("x yra neigiamas arba lygus nuliui")
```

Tačiau šis kodas yra neteisingai struktūrizuotas:

```Python
if x > 0:
print("x yra teigiamas")
else:
   print("x yra neigiamas arba lygus nuliui")
```

## Sakinio struktūra

Python sakinių struktūra yra paprasta. Kiekvienas sakinys gali būti užbaigtas kabliataškiu (;), tačiau Python nereikalauja to daryti, ir praktikoje netaikoma. Taigi, sakinius galite užbaigti taip, kaip norite.

Elementaraus sakinio pavyzdys:

```Python
print("Sveiki, pasauli!")
```

## PEP8 taisyklės

PEP8 yra Python kodo rašymo taisyklių rinkinys, kuris padeda standartizuoti Python kodo formatavimą. Šios taisyklės yra naudingos, nes jos padeda kitiems programuotojams lengviau suprasti jūsų kodą. Kai kurios iš PEP8 taisyklių:

```Text
❗ Nenaudokite tabuliavimo simbolių kaip įtraukos. Vietoj to naudokite tarpus.

❗ Kiekvienas eilutėje neturėtų viršyti 79 simbolių ilgio.

❗ Naudojant kelis argumentus, atskirkite juos kableliais ir po kiekvieno argumento padėkite po vieną tarpą.

❗ Naudokite paaiškinamuosius kintamųjų pavadinimus. Kintamųjų pavadinimai turi kuo tiksliau reprezentuoti jų turinį.

❗ Klasės pavadinimai turėtų naudojant CapWords notaciją (pavyzdžiui, ManoKlasė).

❗ Funkcijų, klasės metodų ir kintamųjų pavadinimuose naudokite mažąsias raides ir atskirkite žodžius apatiniais brūkšniais (pavyzdžiui, mano_funkcija, gimimo_data).

❗ Nesupaprastinkite trumpųjų pavadinimų (pvz., nenaudokite gd vietoj gimimo_data).

❗ Naudojant palyginimo operatorius, naudokite išsamias formas (pavyzdžiui, != vietoj <>).

❗ Naudokite vienodą skiriamųjų simbolių vietą. Pavyzdžiui, jeigu funkcijos argumentai netelpa vienoje eilutėje, ir argumentus išvardinote po vieną naujose eilutėse atitraukus nuo kairės per vieną įtrauką, tai funkcijos deklaracijos argumentų skliaustelis uždaromas irgi naujoje eilutėje, bet neatitraukus.
```

💡 Šios taisyklės nėra būtinos, tačiau jų laikymasis padės padidinti jūsų kodo skaitomumą ir suprantamumą, ypač jei jūs dirbate komandoje su kitais programuotojais arba dalyvaujate atviro kodo projektuose.

## Komentarai

Kodas yra skirtas ne tik kompiuteriams, bet ir žmonėms. Komentarai yra svarbūs, kad kiti programuotojai galėtų lengviau suprasti, ką reiškia tam tikri kodo blokai, ką norite pasiekti su savo kodu. Komentarai taip pat gali padėti jums patiems, jei vėliau turėsite peržiūrėti savo kodą ir suprasti, ką jūs bandėte padaryti.

Komentarai yra rašomi po simbolio `#`, o kai yra paleidžiamas kodas, viskas, kas yra tarp `#` ir eilutės pabaigos, yra ignoruojama. Komentarai taip pat gali būti naudojami kaip laikinas kodas, kurio nenorite paleisti, bet kurį norite laikyti savo faile.

```Python
# Čia mes apibrėžiame kintamuosius, kuriuos naudosime toliau
skaicius1 = 5
skaicius2 = 10

# Ši eilutė sudeda du skaičius
suma = skaicius1 + skaicius2

# Ši eilutė išveda sumą į ekraną
print("Suma yra:", suma)
```

```Python
# Ši eilutė nuskaito vartotojo įvestus skaičius
skaicius1 = int(input("Įveskite pirmą skaičių: "))
skaicius2 = int(input("Įveskite antrą skaičių: "))

# Ši eilutė sudeda du skaičius
suma = skaicius1 + skaicius2

# Ši eilutė išveda sumą į ekraną
print("Suma yra:", suma)
```

```Python
# Ši funkcija patikrina, ar skaičius yra lyginis
def ar_lyginis(skaicius):
    if skaicius % 2 == 0:
        return True
    else:
        return False

# Čia mes patikriname, ar 4 yra lyginis skaičius
if ar_lyginis(4):
    print("4 yra lyginis skaičius")
else:
    print("4 nėra lyginis skaičius")
```

## Klaviatūros sutrumpinimai VS Code aplinkoje

Klaviatūros sutrumpinimai (angl. keyboard shortcuts) yra efektyvus būdas darbui su programavimo redaktoriais, nes jie leidžia programuotojams greičiau ir efektyviau rašyti kodą. VS Code yra labai galinga kūrimo aplinka, kuri turi daugybę klaviatūros sutrumpinimų, kurie palengvina programavimo procesą. Šie klaviatūros sutrumpinimai gali būti naudojami tiek Linux, tiek Windows, tiek macOS sistemose.

```Text
👉 `Ctrl + Shift + P` (`Cmd + Shift + P` macOS sistemoje) - Atidaryti komandų paleidimo langą

👉 `Ctrl + P` (`Cmd + P` macOS sistemoje) - Atidaryti greitąjį meniu

👉 `Ctrl + Shift + E` (`Cmd + Shift + E` macOS sistemoje) - Atidaryti naršyklę

👉 `Ctrl + Shift + F` (`Cmd + Shift + F` macOS sistemoje) - Atidaryti paieškos langą

👉 `Ctrl + Shift + K` (`Cmd + Shift + K` macOS sistemoje) - Ištrinti eilutę

👉 `Ctrl + /` (`Cmd + /` macOS sistemoje) - Sukurti / išjungti komentarą
```

💡 Šie pavyzdžiai yra tik keli iš daugybės klaviatūros sutrumpinimų, kuriuos galite naudoti su VS Code.

Galite rasti visus oficialius VS Code klaviatūros sutrumpinimus [dokumentacijoje](https://code.visualstudio.com/docs/getstarted/keybindings#_keyboard-shortcuts-reference). Pasirinkite aktualią operacinę sistemą (Windows/Mac/Linux)

### Per VS Code programą

Pasirinkite meniu Help (Pagalba) -> Keyboard Shortcuts Reference (Klaviatūros sutrumpinimų sąrašas) arba naudokite greitąją klavišų kombinaciją `Ctrl + K`, `Ctrl + R` (`Cmd + K`, `Cmd + R` macOS sistemoje).
