import unittest

from dd_mod import MetricConvert

switch = MetricConvert()

class MetTest(unittest.TestCase):
    '''
    Tests the metric converter.
    '''
    def test_cels100(self):
        boil = switch.old_to_si(212)
        self.assertEqual(boil, 100.0)

    def test_fahr212(self):
        sealevel = switch.si_to_old(100)
        self.assertEqual(sealevel, 212.0)


if __name__ == '__main__':
    unittest.main()