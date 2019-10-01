def hcf(a, b):
    hcf = 1
    for i in range(1, 1 + min(abs(a),abs(b))):
        if ((a % i == 0) & (b % i == 0)):
            hcf = i
    return hcf

class fraction:
    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return (str(self.numerator) + "/" + str(self.denominator))

    def __init__(self, a, b = None, c = None):
        
        if c is not None:
            temp = fraction(a * c + b, c)
            self.numerator = temp.numerator
            self.denominator = temp.denominator
        elif (b == None or a == 0):
            self.numerator = a
            self.denominator = 1
        else:
            if (b == 0):
                print("Error: not a valid fraction!")
                return
            
            second = abs(b)
            first = int(a*b/second)
            h = hcf(first, second)
            self.numerator = int(first/h)
            self.denominator = int(second/h)        

def AddFractions(fraction1, fraction2):
    return fraction(fraction1.numerator * fraction2.denominator + fraction1.denominator * fraction2.numerator, fraction1.denominator * fraction2.denominator)

def SubtractFractions(fraction1, fraction2):
    return fraction(fraction1.numerator * fraction2.denominator - fraction1.denominator * fraction2.numerator, fraction1.denominator * fraction2.denominator)

def MultiplyFractions(fraction1, fraction2):
    return fraction(fraction1.numerator * fraction2.numerator, fraction1.denominator * fraction2.denominator)

def AreFractionsEqual(fraction1, fraction2):
    return fraction1.numerator == fraction2.numerator and fraction1.denominator == fraction2.denominator