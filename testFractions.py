import unittest
from fractions import *
from testcases import *

class TestFractionArithmetic(unittest.TestCase):
    def __init__(self, testName, fraction1, fraction2, result):
        unittest.TestCase.__init__(self, methodName=testName)
        self.fraction1 = fraction1
        self.fraction2 = fraction2
        self.result = result

    def test_Sum(self):
        self.assertTrue(AreFractionsEqual(AddFractions(self.fraction1, self.fraction2), self.result))

    def test_Product(self):
        self.assertTrue(AreFractionsEqual(MultiplyFractions(self.fraction1, self.fraction2), self.result))

def GetTestCases():
    for x in SumTestCases():
        yield ("test_Sum", x[0], x[1], x[2])
    
    for x in ProductTestCases():
        yield ("test_Product", x[0], x[1], x[2])

if __name__=='__main__':
    testRunner = unittest.TextTestRunner()
    testSuite = unittest.TestSuite([TestFractionArithmetic(n[0], n[1], n[2], n[3]) for n in GetTestCases()])
    testRunner.run(testSuite)