from abc import ABC, abstractmethod


#  SOYUT SINIF: Kaynak
class Kaynak(ABC):
    def __init__(self, baslik, kayitNo):
        self._baslik = baslik
        self._kayitNo = kayitNo

    @property
    def baslik(self):
        return self._baslik

    @baslik.setter
    def baslik(self, deger):
        self._baslik = deger

    @property
    def kayitNo(self):
        return self._kayitNo

    @kayitNo.setter
    def kayitNo(self, deger):
        self._kayitNo = deger

    @abstractmethod
    def bilgi_goster(self):
        pass


#  Kitap sınıfı → Kaynak'tan türetilir
class Kitap(Kaynak):
    def __init__(self, baslik, kayitNo, yazar, sayfa_sayisi):
        super().__init__(baslik, kayitNo)
        self._yazar = yazar
        self._sayfa_sayisi = sayfa_sayisi

    @property
    def yazar(self):
        return self._yazar

    @yazar.setter
    def yazar(self, deger):
        self._yazar = deger

    @property
    def sayfa_sayisi(self):
        return self._sayfa_sayisi

    @sayfa_sayisi.setter
    def sayfa_sayisi(self, deger):
        self._sayfa_sayisi = deger

    def bilgi_goster(self):
        print(f"  Baslik     : {self._baslik}")
        print(f"  Kayit No   : {self._kayitNo}")
        print(f"  Yazar      : {self._yazar}")
        print(f"  Sayfa Sayisi: {self._sayfa_sayisi}")

    def __str__(self):
        return (f"[Kitap] {self._baslik} | {self._kayitNo} | "
                f"{self._yazar} | {self._sayfa_sayisi} sayfa")


#  Dergi sınıfı → Kaynak'tan türetilir
class Dergi(Kaynak):
    def __init__(self, baslik, kayitNo, yayin_donemi, sayi_no):
        super().__init__(baslik, kayitNo)
        self._yayin_donemi = yayin_donemi   # aylik / haftalik
        self._sayi_no = sayi_no

    @property
    def yayin_donemi(self):
        return self._yayin_donemi

    @yayin_donemi.setter
    def yayin_donemi(self, deger):
        self._yayin_donemi = deger

    @property
    def sayi_no(self):
        return self._sayi_no

    @sayi_no.setter
    def sayi_no(self, deger):
        self._sayi_no = deger

    def bilgi_goster(self):
        print(f"  Baslik       : {self._baslik}")
        print(f"  Kayit No     : {self._kayitNo}")
        print(f"  Yayin Donemi : {self._yayin_donemi}")
        print(f"  Sayi No      : {self._sayi_no}")

    def __str__(self):
        return (f"[Dergi] {self._baslik} | {self._kayitNo} | "
                f"{self._yayin_donemi} | Sayi {self._sayi_no}")


#  SOYUT SINIF: Islem
class Islem(ABC):
    @abstractmethod
    def ekle(self):
        pass

    @abstractmethod
    def sil(self, kayitNo):
        pass

    @abstractmethod
    def guncelle(self, kayitNo):
        pass

    @abstractmethod
    def listele(self):
        pass


#  KitapIslem → Islem'den türetilir
class KitapIslem(Islem):
    def __init__(self):
        self._kitaplar = []

    def ekle(self):
        baslik = input("Kitabin basligini girin: ")
        kayitNo = input("Kitabin kayit numarasini girin: ")

        # Bonus: kayıt no tekrar kontrolü
        for k in self._kitaplar:
            if k.kayitNo == kayitNo:
                print("HATA: Bu kayit numarasi zaten mevcut!")
                return

        yazar = input("Kitabin yazarini girin: ")
        try:
            sayfa = int(input("Kitabin sayfa sayisini girin: "))
        except ValueError:
            print("HATA: Sayfa sayisi sayi olmalidir.")
            return

        yeni = Kitap(baslik, kayitNo, yazar, sayfa)
        self._kitaplar.append(yeni)
        print("Kitap basariyla eklendi.")
        print(f"Toplam Kitap Sayisi: {self.kitap_sayisi()}")

    def sil(self, kayitNo=None):
        if kayitNo is None:
            kayitNo = input("Silmek istediginiz kitabin kayit numarasini girin: ")
        for k in self._kitaplar:
            if k.kayitNo == kayitNo:
                self._kitaplar.remove(k)
                print(f"'{k.baslik}' adli kitap silindi.")
                return
        print("HATA: Belirtilen kayit numarasina sahip kitap bulunamadi.")

    def guncelle(self, kayitNo=None):
        if kayitNo is None:
            kayitNo = input("Guncellemek istediginiz kitabin kayit numarasini girin: ")
        for k in self._kitaplar:
            if k.kayitNo == kayitNo:
                print("Yeni bilgileri girin (bos birakirsaniz degismez):")
                yeni_baslik = input(f"Yeni baslik [{k.baslik}]: ")
                yeni_yazar  = input(f"Yeni yazar [{k.yazar}]: ")
                yeni_sayfa  = input(f"Yeni sayfa sayisi [{k.sayfa_sayisi}]: ")
                if yeni_baslik:
                    k.baslik = yeni_baslik
                if yeni_yazar:
                    k.yazar = yeni_yazar
                if yeni_sayfa:
                    try:
                        k.sayfa_sayisi = int(yeni_sayfa)
                    except ValueError:
                        print("Gecersiz sayfa sayisi, degistirilmedi.")
                print("Kitap guncellendi.")
                return
        print("HATA: Belirtilen kayit numarasina sahip kitap bulunamadi.")

    def listele(self):
        if not self._kitaplar:
            print("Kayit bulunamadi.")
            return
        print(f"\n--- Kitap Listesi (Toplam: {self.kitap_sayisi()}) ---")
        for i, k in enumerate(self._kitaplar, 1):
            print(f"{i}. {k}")
        print()

    def kitap_sayisi(self):
        return len(self._kitaplar)


#  DergiIslem → Islem'den türetilir
class DergiIslem(Islem):
    def __init__(self):
        self._dergiler = []

    def ekle(self):
        baslik  = input("Derginin basligini girin: ")
        kayitNo = input("Derginin kayit numarasini girin: ")

        for d in self._dergiler:
            if d.kayitNo == kayitNo:
                print("HATA: Bu kayit numarasi zaten mevcut!")
                return

        yayin_donemi = input("Yayin donemi (aylik/haftalik): ")
        try:
            sayi_no = int(input("Sayi numarasini girin: "))
        except ValueError:
            print("HATA: Sayi numarasi sayi olmalidir.")
            return

        yeni = Dergi(baslik, kayitNo, yayin_donemi, sayi_no)
        self._dergiler.append(yeni)
        print("Dergi basariyla eklendi.")
        print(f"Toplam Dergi Sayisi: {self.dergi_sayisi()}")

    def sil(self, kayitNo=None):
        if kayitNo is None:
            kayitNo = input("Silmek istediginiz derginin kayit numarasini girin: ")
        for d in self._dergiler:
            if d.kayitNo == kayitNo:
                self._dergiler.remove(d)
                print(f"'{d.baslik}' adli dergi silindi.")
                return
        print("HATA: Belirtilen kayit numarasina sahip dergi bulunamadi.")

    def guncelle(self, kayitNo=None):
        if kayitNo is None:
            kayitNo = input("Guncellemek istediginiz derginin kayit numarasini girin: ")
        for d in self._dergiler:
            if d.kayitNo == kayitNo:
                print("Yeni bilgileri girin (bos birakirsaniz degismez):")
                yeni_baslik  = input(f"Yeni baslik [{d.baslik}]: ")
                yeni_donem   = input(f"Yeni yayin donemi [{d.yayin_donemi}]: ")
                yeni_sayi    = input(f"Yeni sayi no [{d.sayi_no}]: ")
                if yeni_baslik:
                    d.baslik = yeni_baslik
                if yeni_donem:
                    d.yayin_donemi = yeni_donem
                if yeni_sayi:
                    try:
                        d.sayi_no = int(yeni_sayi)
                    except ValueError:
                        print("Gecersiz sayi no, degistirilmedi.")
                print("Dergi guncellendi.")
                return
        print("HATA: Belirtilen kayit numarasina sahip dergi bulunamadi.")

    def listele(self):
        if not self._dergiler:
            print("Kayit bulunamadi.")
            return
        print(f"\n--- Dergi Listesi (Toplam: {self.dergi_sayisi()}) ---")
        for i, d in enumerate(self._dergiler, 1):
            print(f"{i}. {d}")
        print()

    def dergi_sayisi(self):
        return len(self._dergiler)


#  Menu sınıfı
class Menu:
    def goster(self):
        print("\n" + "*"*40)
        print("   KUTUPHANE YONETIM SISTEMI")
        print("*"*40)
        print("1. Kitap Ekle")
        print("2. Kitap Sil")
        print("3. Kitap Guncelle")
        print("4. Kitaplari Listele")
        print("5. Dergi Ekle")
        print("6. Dergi Sil")
        print("7. Dergi Guncelle")
        print("8. Dergileri Listele")
        print("9. Cikis")
        print("*"*40)


#  ANA PROGRAM
def main():
    menu         = Menu()
    kitap_islem  = KitapIslem()
    dergi_islem  = DergiIslem()

    while True:
        menu.goster()
        secim = input("Yapmak istediginiz islemi secin (1-9): ").strip()

        if secim == "1":
            kitap_islem.ekle()
        elif secim == "2":
            kitap_islem.sil()
        elif secim == "3":
            kitap_islem.guncelle()
        elif secim == "4":
            kitap_islem.listele()
        elif secim == "5":
            dergi_islem.ekle()
        elif secim == "6":
            dergi_islem.sil()
        elif secim == "7":
            dergi_islem.guncelle()
        elif secim == "8":
            dergi_islem.listele()
        elif secim == "9":
            print("Programdan cikiliyor. Gorusuruz!")
            break
        else:
            print("Gecersiz secim! Lutfen 1-9 arasinda bir sayi girin.")


if __name__ == "__main__":
    main()
