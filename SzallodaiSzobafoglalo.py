from abc import ABC, abstractmethod  # Importáljuk az ABC és abstractmethod modulokat az absztrakt osztályok és metódusok létrehozásához
from datetime import datetime  # Importáljuk a datetime modult a dátumok kezeléséhez

class Szoba(ABC):  # Absztrakt osztály definíciója a Szoba osztály számára
    def __init__(self, ar, szobaszam):  # Konstruktor, ami inicializálja az árat és a szobaszámot
        self.ar = ar  # Szoba ára
        self.szobaszam = szobaszam  # Szoba száma
        self.foglalasok = {}  # Szoba foglalásainak tárolásához

    @abstractmethod  # Absztrakt metódus, amelyet a leszármazott osztályokban kell implementálni
    def get_tipus(self):  # Metódus deklarációja, ami Visszaadjuk a szoba típusát
        pass  # Absztrakt metódus törzse, amely nincs implementálva itt

class EgyagyasSzoba(Szoba):  # Leszármaztatott osztály az EgyágyasSzoba, amely a Szoba osztálytól örököl
    def __init__(self, ar, szobaszam):  # Konstruktor az EgyágyasSzoba számára
        super().__init__(ar, szobaszam)  # Meghívjuk a szülő osztály konstruktorát az ár és szobaszám továbbításával

    def get_tipus(self):  # Implementáljuk az absztrakt metódust, ami Visszaadjuk a szoba típusát
        return "Egyágyas"  # Visszaadjuk az "Egyágyas" sztringet, amely a szoba típusát jelöli

class KetagyasSzoba(Szoba):  # Leszármaztatott osztály a KétagyasSzoba számára
    def __init__(self, ar, szobaszam):  # Konstruktor a KétagyasSzoba számára
        super().__init__(ar, szobaszam)  # Meghívjuk a szülő osztály konstruktorát az ár és szobaszám továbbításával

    def get_tipus(self):  # Implementáljuk az absztrakt metódust, ami Visszaadjuk a szoba típusát
        return "Kétagyas"  # Visszaadjuk a "Kétagyas" sztringet, amely a szoba típusát jelöli

class Szalloda:  # Szálloda osztály definíciója a Szalloda számára
    def __init__(self, nev):  # Konstruktor a Szalloda számára
        self.nev = nev  # Szálloda neve
        self.szobak = []  # Lista, ami a szálloda szobáit tárolja

    def foglalas(self, szobaszam, datum):  # Metódus a szobák foglalására
        szoba = self.szoba_keres(szobaszam)  # Megkeressük a szobát a megadott szobaszámmal
        if szoba and datum not in szoba.foglalasok:  # Ellenőrizzük, hogy a szoba létezik-e és a dátum szabad-e
            szoba.foglalasok[datum] = szoba.ar  # Bejegyezzük a foglalást a szobához
            return szoba.ar  # Visszaadjuk a szoba árát
        return None  # Ha a szoba nem létezik, vagy a dátum már foglalt, akkor None értéket adunk vissza

    def lemondas(self, szobaszam, datum):  # Metódus a foglalások lemondására
        szoba = self.szoba_keres(szobaszam)  # Megkeressük a szobát a megadott szobaszámmal
        if szoba and datum in szoba.foglalasok:  # Ellenőrizzük, hogy a szoba létezik-e és a dátum foglalt-e
            del szoba.foglalasok[datum]  # Töröljük a foglalást a szobából
            return True  # Ha a lemondás sikeres, akkor a visszatérés True - Igaz
        return False  # Hamissal térünk vissza, ha a szoba nem létezik, vagy ha a dátum nem foglalt

    def szoba_keres(self, szobaszam):  # Metódus a szobák keresésére
        for szoba in self.szobak:  # Végigmegyünkünk a szálloda összes szobáján
            if szoba.szobaszam == szobaszam:  # Ha a szobaszám megegyezik a keresett szobaszámmal
                return szoba  # Akkor visszaadjuk a szobát
        return None  # Ha nem találjuk a szobát, akkor None értéket adunk vissza

    def teljes_listazas(self):  # Metódus a szálloda összes szobájának és foglalásának listázására
        print(f"Szálloda: {self.nev}")  # Kiírjuk a szálloda nevét
        for szoba in sorted(self.szobak, key=lambda x: x.szobaszam):  # Rendezetten Végigmegyünkünk a szobákon szobaszám alapján
            print(f"Szoba {szoba.szobaszam} ({szoba.get_tipus()}):")  # Kiírjuk a szoba számát és típusát
            for datum in sorted(szoba.foglalasok):  # Rendezetten Végigmegyünkünk a szoba foglalásain dátum alapján
                print(f"  {datum}: Foglalt")  # Kiírjuk a foglalás dátumát és azt, hogy foglalt-e

class Foglalas:  # Osztály definíciója a Foglalas kezelésére
    def __init__(self, szalloda):  # Konstruktor, ami inicializálja a szálloda referenciát
        self.szalloda = szalloda  # Szálloda objektum, amelyben a foglalások kezelése történik

    def foglalas_kezeles(self, szobaszam, datum):  # Metódus egy adott szoba foglalásának kezelésére
        ar = self.szalloda.foglalas(szobaszam, datum)  # Lekérjük a foglalás árát, ha a foglalás lehetséges
        if ar is not None:  # Ha az ár nem None, akkor a foglalás sikeres
            print(f"Foglalás sikeres: {datum}, Ár: {ar} Ft")  # Kiírjuk a foglalás sikerességét és az árat
        else:  # Ha az ár None, akkor a foglalás sikertelen
            print("Foglalás sikertelen.")  # Kiírjuk, hogy a foglalás sikertelen

    def lemondas_kezeles(self, szobaszam, datum):  # Metódus egy adott szoba foglalásának lemondására
        if self.szalloda.lemondas(szobaszam, datum):  # Ha a lemondás sikeres
            print(f"Lemondás sikeres: {datum}")  # Kiírjuk a lemondás sikerességét
        else:  # Ha a lemondás sikertelen
            print("Lemondás sikertelen.")  # Kiírjuk, hogy a lemondás sikertelen

def datum_validacio(datum):  # Függvény a dátum érvényességének ellenőrzésére
    try:  # Megpróbáljuk a dátumot konvertálni a megadott formátumra
        return datetime.strptime(datum, "%Y-%m-%d")  # Visszaadjuk a dátum objektumot, ha a formátum helyes
    except ValueError:  # Ha a dátum formátuma hibás
        return None  # None értékkel térünk vissza

def main():  # Főprogram, ami az alkalmazás logikáját tartalmazza
    hotel = Szalloda("Hotel Balaton")  # Létrehozzuk a szálloda objektumot a "Hotel Balaton" névvel
    hotel.szobak.append(EgyagyasSzoba(5000, 1))  # Hozzáadunkunk egy egyágyas szobát az 1-es szobaszámmal és 5000 Ft árral
    hotel.szobak.append(KetagyasSzoba(8000, 2))  # Hozzáadunk egy kétagyas szobát a 2-es szobaszámmal és 8000 Ft árral
    hotel.szobak.append(EgyagyasSzoba(5500, 3))  # Hozzáadunk egy másik egyágyas szobát a 3-as szobaszámmal és 5500 Ft árral

    foglalas_kezelo = Foglalas(hotel)  # Létrehozzuk a foglaláskezelő objektumot a szálloda referenciával

    hotel.foglalas(1, "2023-05-11")  # Foglalások létrehozása a 1-es szobához
    hotel.foglalas(1, "2023-05-12")  # További foglalás a 1-es szobához
    hotel.foglalas(2, "2023-05-11")  # Foglalás a 2-es szobához
    hotel.foglalas(3, "2023-05-13")  # Foglalás a 3-as szobához
    hotel.foglalas(3, "2023-05-14")  # További foglalás a 3-as szobához

    hotel.teljes_listazas()  # Listázza ki a szálloda összes foglalását

    while True:  # Végtelen ciklus a felhasználói interakciók kezelésére, amíg ki nem lép
        print("\n1 - Foglalás\n2 - Lemondás\n3 - Teljes listázás\n4 - Kilépés")  # Menü kiírása
        valasztas = input("Válassz egy opciót: ")  # Felhasználó választása
        if valasztas == "1":  # Ha a felhasználó a foglalást választja
            while True:  # Ciklus a foglalás adatainak megadására
                print("Elérhető szobák:")  # Kiírjuk az elérhető szobákat
                for szoba in hotel.szobak:  # Végigmegyünk a szálloda összes szobáján
                    print(f"Szobaszám: {szoba.szobaszam}, Típus: {szoba.get_tipus()}")  # Kiírjuk a szoba számát és típusát
                szobaszam = input("Adja meg a szobaszámot (vagy nyomjon entert a foglalás megszakításához): ")  # Bekérjük a szobaszámot
                if szobaszam == "":  # Ha üres inputot kapunk, akkor kilépünk a ciklusból
                    break
                try:  # Megpróbáljuk konvertálni a szobaszámot egész számmá
                    szobaszam = int(szobaszam)  # Szobaszám konvertálása
                    szoba = hotel.szoba_keres(szobaszam)  # Szoba keresése a megadott szám alapján
                    if not szoba:  # Ha a szoba nem létezik
                        print("Nem létező szobaszám!")  # Hibaüzenet
                        continue  # Folytatjuk a ciklust
                    print("Foglaltsági lista:")  # Kiírjuk a szoba foglaltsági listáját
                    for datum, ar in sorted(szoba.foglalasok.items()):  # Végigmegyünk a foglalásokon rendezett sorrendben
                        print(f"{datum}: Foglalt - {ar} Ft")  # Kiírjuk a foglalt dátumokat és az árat
                    while True:  # Ciklus a dátum megadásához
                        datum = input("Adja meg a dátumot (ÉÉÉÉ-HH-NN pl. 2032-05-10) vagy nyomjon entert a foglalás megszakításához: ")  # Dátum bekérése
                        if datum == "":  # Ha üres inputot kapunk, kilépünk a ciklusból
                            break
                        valid_datum = datum_validacio(datum)  # Dátum érvényességének ellenőrzése
                        if not valid_datum:  # Ha a dátum érvénytelen
                            print("Érvénytelen dátum formátum!")  # Hibaüzenet
                            continue  # Folytatjuk a ciklust
                        if valid_datum.date() <= datetime.today().date():  # Ha a dátum a múltban vagy a mai napon van
                            print("Szobát csak előre lehet foglalni, azaz csak a mai követő napokra lehetséges!")  # Hibaüzenet
                            continue  # Folytatjuk a ciklust
                        if datum in szoba.foglalasok:  # Ha a dátum már foglalt
                            print("Ez a dátum már foglalt!")  # Hibaüzenet
                            continue  # Folytatjuk a ciklust
                        foglalas_kezelo.foglalas_kezeles(szobaszam, datum)  # Foglalás kezelése
                        break  # Kilépünk a belső ciklusból
                    break  # Kilépünk a külső ciklusból
                except ValueError:  # Ha a szobaszám nem egész szám
                    print("Érvénytelen számformátum!")  # Hibaüzenet
        elif valasztas == "2":  # Ha a felhasználó a lemondást választja
            while True:
                print("Elérhető szobák a lemondáshoz:")
                for szoba in hotel.szobak:
                    print(f"Szobaszám: {szoba.szobaszam}, Típus: {szoba.get_tipus()}")
                szobaszam = input("Adja meg a szobaszámot (vagy nyomjon entert a lemondás megszakításához): ")
                if szobaszam == "":
                    break
                try:
                    szobaszam = int(szobaszam)
                    szoba = hotel.szoba_keres(szobaszam)
                    if not szoba:
                        print("Nem létező szobaszám!")
                        continue
                    if not szoba.foglalasok:
                        print("Nincsenek foglalások ebben a szobában.")
                        break
                    print("Foglaltsági lista:")  # Kiírjuk a szoba foglaltsági listáját
                    for datum, ar in sorted(szoba.foglalasok.items()):  # Végigmegyünk a foglalásokon rendezett sorrendben
                        print(f"{datum}: Foglalt - {ar} Ft")  # Kiírjuk a foglalt dátumokat és az árat
                    while True:  # Ciklus a dátum megadásához
                        datum = input("Adja meg a dátumot (ÉÉÉÉ-HH-NN pl. 2032-05-10) vagy nyomjon entert a foglalás megszakításához: ")  # Dátum bekérése
                        if datum == "":  # Ha üres inputot kapunk, kilépünk a ciklusból
                            break  # Kilépünk a belső ciklusból
                        valid_datum = datum_validacio(datum)  # Dátum érvényességének ellenőrzése
                        if not valid_datum:  # Ha a dátum érvénytelen
                            print("Érvénytelen dátum formátum!")  # Hibaüzenet
                            continue  # Folytatjuk a ciklust
                        if valid_datum.date() <= datetime.today().date():  # Ha a dátum a múltban vagy a mai napon van
                            print("Szobafoglalást lemondása csak a mai napot követő napokon történt foglalások esetén lehetséges!")  # Hibaüzenet
                            continue  # Folytatjuk a ciklust                        
                        if datum not in szoba.foglalasok:
                            print("Nincs ilyen foglalás ezen a dátumon!")  # Hibaüzenet
                            continue  # Folytatjuk a ciklust 
                        foglalas_kezelo.lemondas_kezeles(szobaszam, datum)  # Lemondás kezelése
                        break  # Kilépünk a belső ciklusból
                    break  # Kilépünk a külső ciklusból
                except ValueError:
                    print("Érvénytelen számformátum!")
        elif valasztas == "3":  # Ha a felhasználó a teljes listázást választja
            hotel.teljes_listazas()  # Listázzuk a szálloda összes foglalását
        elif valasztas == "4":  # Ha a felhasználó kilépést választja
            break  # Kilépünk a végtelen ciklusból
        else:  # Ha a felhasználó érvénytelen opciót ad meg
            print("Érvénytelen opció!")  # Hibaüzenet

main()  # A main függvény hívása, ami elindítja az alkalmazást
