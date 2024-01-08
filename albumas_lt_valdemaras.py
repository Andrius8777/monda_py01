""" Komandinio/individualaus darbo užduotis
===[ Muzikos Albumas ]===

Reikalavimai:

* Žodynas albumas turi turėti atlikėją ir pavadinimą, gali turėti ir kitų atributų
* Albumo žodyne sukurkite takelių (dainų) sąrašą, kur kiekvienas takelis yra žodynas, talpinantis eilės numerį, pavadinimą ir trukmę sekundėmis. 
** Bonus: trukmės įvedimas "minutės:sekundės" formatu (žmogui suprantamu).
* Programa turi leisti vartotojui užpildyti/pakeisti albumo informaciją (pavadinimą, atlikėją, ...)
* Programa turi leisti vartotojui sukurti/ištrinti takelį, užpildant takelio informaciją (pavadinimą, trukmę)
* Galimybė peržiūrėti albumą, išspausdinant takelių kiekį ir bendrą jų trukmę šalia kitų atributų.
* Peržiūrėti albumo dainas. Bonus: išrūšiuotas pagal eilės numerį. Takelio trukmė turi būti pateikta žmogui suprantama laiko išraiška.

Pastabos:
* Stenkitės nekartoti kodo - funkcionalumui, kuriam kodas kartotųsi, parašykite atskiras funkcijas ir jas panaudokite kelis kartus kur reikia.
"""


albumas = {}
albumas = [{'Artist': 'Dj Tiesto', 'Song name': 'Space' , 'Duration(s)': 230}, {'Artist': 'Dj Mouse', 'Song name': 'Lost' , 'Duration(s)': 430}]


while True:
    print('====== CD ALBUMAS =======')
    print('0: EXIT')
    print('1: Song list')
    print('2: Edit list')
    print('3: Delete list')
    print('4: Check total lenght Album')
    menu = input('Pasirinkite viena is punktu: ')
    if menu == 0:
        break
    elif menu == 1:
        menu = albumas.keys()






print('Copyrated By CodeAcademy Xackers')

def add_song(album, name=str, audio_long=float)
    for album