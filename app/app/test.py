from django.test import SimpleTestCase
from app import calc
class CalculateTests(SimpleTestCase):

    def test_add_number(self):
        res=calc.add(8,4)
        self.assertEqual(res,12)
    def test_mult_number(self):
        res=calc.mult(8,4)
        self.assertEqual(res,32)