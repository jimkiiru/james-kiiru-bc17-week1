
import unittest
from GeneratePrimeNumbers import GeneratePrimeNumbers


class TestPrimeGenerator(unittest.TestCase):

    def TestCorrectness(self):
        #test whether the function generates correct prime numbers
        self.assertEqual(GeneratePrimeNumbers(20), [2, 3, 5, 7, 11, 13, 17, 19])


    def TestZero(self):
        self.assertEqual(GeneratePrimeNumbers(0), "Zero or One cannot be prime numbers.")

    def TestOne(self):
        self.assertEqual(GeneratePrimeNumbers(1), "Zero or One cannot be prime numbers.")

    def TestString(self):
        #makes sure that strings are not executed
        self.assertEqual(GeneratePrimeNumbers("String"), "Only integers are allowed.")

    def TestNegativeNumbers(self):
        #makes sure that only positive numbers are processed if the number is negative an error is displayed
        self.assertEqual(GeneratePrimeNumbers(-1), "Not possible to generate prime numbers for integers less than 2.")


if __name__ == "__main__":
       unittest.main()


       
