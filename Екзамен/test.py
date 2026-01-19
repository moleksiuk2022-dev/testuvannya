import unittest
from main import is_adult

class TestIsAdult(unittest.TestCase):

    def test_age_17(self):
        self.assertFalse(is_adult(17))

    def test_age_18(self):
        self.assertTrue(is_adult(18))

    def test_age_19(self):
        self.assertTrue(is_adult(19))


if __name__ == "__main__":
    unittest.main()
