"""Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti. Jokaisella julkaisulla on
nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös
tarvittavat alustajat. Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot. Luo
pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla."""


# Luokka Jukaisu
class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    # Tulostaa luokan tiedot
    def tulosta_tiedot(self):
        print(f"Julkaisun nimi: {self.nimi}")


# Luokka Kirja
class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivujen_maara):
        self.kirjoittaja = kirjoittaja
        self.sivujen_maara = sivujen_maara
        super().__init__(nimi)

    # Tulostaa luokan tiedot
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjan kirjailija: {self.kirjoittaja} ja sivujen määrä on {self.sivujen_maara}.")


# Luokka Lehti
class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)

    # Tulostaa luokan tiedot
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Lehden päätoimittaja on {self.paatoimittaja}.")


# Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
# Pääohjelma
julkaisut = []
julkaisut.append(Kirja("Hytti n:o 6", "Rosa Liksom", 200))
julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))

for j in julkaisut:
    j.tulosta_tiedot()