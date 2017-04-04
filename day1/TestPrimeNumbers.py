
import unittest
from GeneratePrimeNumbers import GeneratePrimeNumbers


class TestPrimeGenerator(unittest.TestCase):

    def test_prime_numbers(self):
        self.assertEqual(GeneratePrimeNumbers(20), [2, 3, 5, 7, 11, 13, 17, 19])


    def test_zero(self):
        self.assertEqual(GeneratePrimeNumbers(0), "Zero or One cannot be prime numbers.")

    def test_one(self):
        self.assertEqual(GeneratePrimeNumbers(1), "Zero or One cannot be prime numbers.")

    def test_two(self):
        self.assertEqual(GeneratePrimeNumbers("String"), "Only integers are allowed.")

    def test_only_positive(self):
        self.assertEqual(GeneratePrimeNumbers(-1), "Not possible to generate prime numbers for integers less than 2.")


if __name__ == "__main__":
       unittest.main()


       
