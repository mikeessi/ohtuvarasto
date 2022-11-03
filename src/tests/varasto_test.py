import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.neg_varasto = Varasto(-5,-1)
        self.varasto_full = Varasto(5,10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_tilavuus_uudella_varastolla(self):
        self.assertAlmostEqual(self.neg_varasto.tilavuus, 0)

    def test_negatiivinen_alkusaldo_uudella_varastolla(self):
        self.assertAlmostEqual(self.neg_varasto.saldo, 0)

    def test_ylitaysi_varasto_oikea_saldo(self):
        self.assertAlmostEqual(self.varasto_full.saldo, 5)

    def test_negatiivinen_lisays_ei_tee_mitaan(self):
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_liika_lisays_antaa_oikean_saldon(self):
        self.varasto.lisaa_varastoon(11)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_negatiivinen_otto_ei_anna_mitaan(self):
        otto = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(otto, 0)

    def test_oikea_otto_kun_yritetaan_ottaa_liikaa(self):
        self.varasto.lisaa_varastoon(5)
        otto = self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(otto, 5)

    def test_oikea_saldo_liikaoton_jalkeen(self):
        self.varasto.lisaa_varastoon(5)
        otto = self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_oikea_merkkijono(self):
        self.assertAlmostEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
