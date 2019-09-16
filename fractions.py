def hcf(a, b):
    hcf = 1
    for i in range(1, min(a,b)):
        if ((a % i == 0) & (b % i == 0)):
            hcf = i
    return hcf

class fraction:
    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return (str(self.numerator) + "/" + str(self.denominator))

    def __init__(self, a, b = None):
        if (b == None):
            self.numerator = a
            self.denominator = 1
        else:
            if (a*b < 0):
                a = -1*abs(a)
                b = abs(b)
            elif (a*b > 0):
                a = abs(a)
                b = abs(b)
            elif (b==0):
                return "Error: not a valid fraction."

            h = hcf(a, b)
            self.numerator = int(a/h)
            self.denominator = int(b/h)        

def sum(fraction1, fraction2):
    return fraction(fraction1.numerator * fraction2.denominator + fraction1.denominator * fraction2.numerator, fraction1.denominator * fraction2.denominator)

def diff(fraction1, fraction2):
    return fraction(fraction1.numerator * fraction2.denominator - fraction1.denominator * fraction2.numerator, fraction1.denominator * fraction2.denominator)

def equal(fraction1, fraction2):
    return fraction1.numerator == fraction2.numerator and fraction1.denominator == fraction2.denominator

def testSum(fraction1, fraction2, fractionSum):
    if equal(sum(fraction1, fraction2), fractionSum):
        print("pass")
    else:
        print("fail")

a = fraction(3, -4)
b = fraction(4, 3)
c = fraction(1, 2)
d = fraction(-2, 5)
e = fraction(6, 2)
f = fraction(1)
g = fraction(0)
h = fraction(3)

testSum(a, b, fraction(7, 12))
testSum(b, d, fraction(14, 15))
testSum(c, e, fraction(7, 2))
testSum(a, d, fraction(-23, 20))
testSum(f, g, f)
testSum(g, g, g)
testSum(h, f, fraction(4))