import unittest
from calcularArea import calcularArea
class TestArea(unittest.TestCase):
	def setUp(self):
		self.calc=calcularArea()

	def test_cuadrado_4x4_16(self):
		self.assertEquals(self.calc.cuadrado(4),16)

if __name__ == '__main__':
	unittest.main()