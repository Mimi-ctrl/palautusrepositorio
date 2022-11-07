import unittest
from statistics import Statistics
from player import Player
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_palauttaa_oikean_pelaajan(self):
        pelaaja = self.statistics.search("Semenko")
        self.assertEqual(pelaaja.name, "Semenko")

    def test_palauttaa_tyhjan_jos_ei_pelaajaa(self):
        pelaaja = self.statistics.search("Peltonen")
        self.assertEqual(pelaaja, None)

    def test_palauttaa_oikeat_pelaajat(self):
        pelaajat = self.statistics.team("EDM")
        pelaaja_nimet = [pelaaja.name for pelaaja in pelaajat]
        self.assertListEqual(pelaaja_nimet, ["Semenko", "Kurri", "Gretzky"])

    def test_palauttaa_oikeassa_jarjestyksessa_pisteet(self):
        pelaajat = self.statistics.top(3, SortBy.POINTS)
        top3 = ["Gretzky", "Lemieux", "Yzerman"]
        self.assertEqual(pelaajat[0].name, top3[0])
        self.assertEqual(pelaajat[1].name, top3[1])
        self.assertEqual(pelaajat[2].name, top3[2])
        