from unittest import TestCase

from periodic_table import PeriodicTable


class TestPeriodicTable(TestCase):

    def setUp(self) -> None:
        self.table = PeriodicTable()

    def test_search_name(self):
        s = self.table.search_number(16)
        self.assertFalse(s is None)
        names = ('sulfur', 'Sulfur', 'Sulphur')
        for n in names:
            self.assertTrue(s.is_named(n))
            found = self.table.search_name(n)
            self.assertTrue(found is s)

        self.assertIsNone(self.table.search_name("Gerardominium"))

    def test_search_symbol(self):
        fe = self.table.search_number(26)
        for sm in ('Fe','fe'):
            found = self.table.search_symbol(sm)
            self.assertTrue(found is fe)
        self.assertIsNone(self.table.search_symbol('peace sign'))


    def test_search_number(self):
        for i in range(1,115):
            e = self.table.search_number(i)
            self.assertEqual(i,e.atomic)



