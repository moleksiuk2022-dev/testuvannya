import unittest
from random import choice, randint
from app import Figure  

class TestFigure(unittest.TestCase):

    def setUp(self) -> None:
        self.figure_type = choice(Figure.FIGURES)
        self.length = randint(1, 10)
        self.obj = Figure(self.figure_type, self.length)
        return super().setUp()

    def tearDown(self) -> None:
        del self.obj
        return super().tearDown()

    def test_figure_type(self):
        self.assertEqual(self.obj.type, self.figure_type,
                         f"Expected {self.figure_type}, got {self.obj.type}")

    def test_figure_length(self):
        self.assertEqual(self.obj.length, self.length,
                         f"Expected {self.length}, got {self.obj.length}")

    def test_invalid_object(self):
        with self.assertRaises(AssertionError):
            Figure("circle", 1) 

if __name__ == '__main__':
    unittest.main()
