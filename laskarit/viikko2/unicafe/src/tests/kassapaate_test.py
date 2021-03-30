import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(10)

    def test_luotu_kassa_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edulliset_maksut_alussa_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaat_maksut_alussa_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_kateinen_kun_on_raha(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250), 10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_maukas_kateinen_kun_on_raha(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(410), 10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_edullinen_lounaat_kateinen_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukas_lounaat_kateinen_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(410)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullinen_kateinen_kun_ei_on_raha(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(230), 230)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukas_kateinen_kun_ei_on_raha(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(4), 4)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullinen_lounaat_kateinen_ei_raha_ei_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(2)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukas_lounaat_kateinen_ei_raha_ei_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(40)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_kortti_kun_on_raha(self):
        self.maksukortti.lataa_rahaa(250)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_maukas_kortti_kun_on_raha(self):
        self.maksukortti.lataa_rahaa(400)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_edullinen_lounaat_kortti_kasvaa(self):
        self.maksukortti.lataa_rahaa(250)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukas_lounaat_kortti_kasvaa(self):
        self.maksukortti.lataa_rahaa(400)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullinen_kortti_kun_ei_on_raha(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)

    def test_maukas_kortti_kun_ei_on_raha(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)

    def test_edullinen_lounaat_kortti_ei_raha_ei_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukas_lounaat_kortti_ei_raha_ei_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortti_ei_kasvata_kassaa(self):
        self.maksukortti.lataa_rahaa(20000)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortti_lataus_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)
        self.assertEqual(str(self.maksukortti), "saldo: 2.1")

    def test_kortti_lataus_kasvattaa_kassaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100200)

    def test_kortti_lataus_negatiivinen_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -200)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_kortti_lataus_negatiivinen_ei_kasvattaa_kassaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)



