class Fraction:
    def __init__(self):
        self.num = int(input("enter numerator:"))
        self.den = int(input("enter denominator:"))
        self.frac()
    def frac(self):
        if self.den == 0:
            print("denominator cannot be zero")
        else:
            x=self.num/self.den
            print(f'{x}')

fraction = Fraction()      # 1:20:00