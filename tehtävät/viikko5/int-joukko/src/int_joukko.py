class IntJoukko:
    def __init__(self):
        self.sum = 5
        self.lukujono = [0] * 5
        self.alkioiden_lukumaara = 0

    def kuuluuko(self, luku):
        if luku in self.lukujono:
            return True
        return False

    def lisaa(self, luku): 
        if self.alkioiden_lukumaara == 0:
            self.lukujono[0] = luku
            self.alkioiden_lukumaara = self.alkioiden_lukumaara + 1
            return True
        if self.kuuluuko(luku):
            return False
        self.lukujono[self.alkioiden_lukumaara] = luku
        self.alkioiden_lukumaara = self.alkioiden_lukumaara + 1
        if self.alkioiden_lukumaara % len(self.lukujono) == 0:
            vanha_taulu = self.lukujono
            self.kopioi_taulukko(self.lukujono, vanha_taulu)
            self.lukujono = [0] * (self.alkioiden_lukumaara + self.sum)
            self.kopioi_taulukko(vanha_taulu, self.lukujono)

        return True

    def poista(self, luku):
        if not self.kuuluuko(luku):
            return False
        i = self.lukujono.index(luku)
        self.lukujono[i] = 0
        for x in range(i, self.alkioiden_lukumaara - 1):
            apu = self.lukujono[x]
            self.lukujono[x] = self.luvut[x+1]
            self.lukujono[x+1] = apu
        self.alkioiden_lukumaara = self.alkioiden_lukumaara - 1
        return True

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lukumaara

    def to_int_list(self):
        return [luku for luku in self.lukujono if luku > 0]

    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            yhdiste.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            yhdiste.lisaa(b_taulu[i])

        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    leikkaus.lisaa(b_taulu[j])

        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            erotus.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            erotus.poista(b_taulu[i])

        return erotus

    def __str__(self):
            tuotos = "{"
            for i in range(0, self.alkioiden_lukumaara - 1):
                tuotos = tuotos + str(self.lukujono[i])+ ", "
            tuotos = tuotos + str(self.lukujono[self.alkioiden_lukumaara - 1]) + "}"
            return tuotos
