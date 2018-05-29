import unittest
from src.utilities import get_validated_url

class TestUtilities(unittest.TestCase):
    def test_get_validated_url(self):
        self.assertEqual(get_validated_url("google.com"), "http://google.com")
        self.assertEqual(get_validated_url("https://google.com"), "https://google.com")
        self.assertEqual(get_validated_url("www.google.com"), "http://www.google.com")
        self.assertEqual(get_validated_url("http://google.com"), "http://google.com")


        self.assertEqual(get_validated_url("google.com"), "http://google.com")



if __name__ == "__main__":
    unittest.main()

