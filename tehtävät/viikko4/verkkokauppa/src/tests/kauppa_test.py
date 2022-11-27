import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()
        self.nimi = "Henkilö Henkilö"
        self.tili = "26849"


        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 5
            if tuote_id == 3:
                return 0
                
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "omena", 6)
            if tuote_id == 3:
                return Tuote(3, "kurkku", 3)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu(self.nimi, self.tili)
        self.pankki_mock.tilisiirto.assert_called()

    def test_kutsutaan_pankin_metodia_tilisiirto_oikealla_asiakkaalla_tilinumeroilla_ja_summalla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu(self.nimi, self.tili)
        self.pankki_mock.tilisiirto.assert_called_with(self.nimi, ANY, self.tili, ANY, 5)
    
    def test_kutsutaan_pankin_metodia_tilisiirto_oikealla_asiakkaalla_tilinumeroilla_ja_summalla_kun_kaksi_eri_tuotetta(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu(self.nimi, self.tili)
        self.pankki_mock.tilisiirto.assert_called_with(self.nimi, ANY, self.tili, ANY, 11)

    def test_kutsutaan_pankin_metodia_tilisiirto_oikealla_asiakkaalla_tilinumeroilla_ja_summalla_kun_kaksi_samaa_tuotetta(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu(self.nimi, self.tili)
        self.pankki_mock.tilisiirto.assert_called_with(self.nimi, ANY, self.tili, ANY, 10)

    def test_kutsutaan_pankin_metodia_tilisiirto_oikealla_asiakkaalla_tilinumeroilla_ja_summalla_kun_kaksi_eri_tuotetta_joista_toinen_loppu(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu(self.nimi, self.tili)
        self.pankki_mock.tilisiirto.assert_called_with(self.nimi, ANY, self.tili, ANY, 11)

    def test_nollaa_edellisen_ostoksen_tiedot(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu(self.nimi, self.tili)
        self.pankki_mock.tilisiirto.assert_called_with(self.nimi, ANY, self.tili, ANY, 5)
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu(self.nimi, self.tili)
        self.pankki_mock.tilisiirto.assert_called_with(self.nimi, ANY, self.tili, ANY, 5)

    def test_kauppa_pyytaa_uuden_viitenumeron_jokaiselle_maksutapahtumalle(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu(self.nimi, self.tili)
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 1)
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu(self.nimi, self.tili)
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu(self.nimi, self.tili)
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 3)
    
    def test_poistaa_tuotteen_korista(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu(self.nimi, self.tili)
        self.pankki_mock.tilisiirto.assert_called_with(self.nimi, ANY, self.tili, ANY, 0)

    