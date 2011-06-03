class RationalNumber(object):

    def __init__(self, numerator, denominator):
        self._numerator = numerator
        self._denominator = denominator
        self._simplify()

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    def _simplify(self):
        mdc = self._mdc(self._numerator, self._denominator)
        self._numerator /= mdc
        self._denominator /= mdc

    def _mdc(self, n1, n2):
        index = min(n1, n2)
        while index > 1:
            if n1 % index == 0 and n2 % index == 0:
                return index
            index -= 1
        return 1

    def _mmc(self, n1, n2):
        maxn = max(n1, n2)
        index = maxn
        while True:
            if index % n1 == 0 and index % n2 == 0:
                return index
            index += maxn

    def __eq__(self, other):
        return self.numerator == other.numerator and \
                self.denominator == other.denominator

    def __add__(self, other):
        mmc = self._mmc(self.denominator, other.denominator)
        return RationalNumber(mmc / self.denominator * self.numerator +
                               mmc / other.denominator * other.numerator, mmc)

    def __sub__(self, other):
        mmc = self._mmc(self.denominator, other.denominator)
        return RationalNumber(mmc / self.denominator * self.numerator -
                               mmc / other.denominator * other.numerator, mmc)

    def __mul__(self, other):
        return RationalNumber(self.numerator * other.numerator,
                               self.denominator * other.denominator)

    def __div__(self, other):
        return RationalNumber(self.numerator * other.denominator,
                               self.denominator * other.numerator)

    def __str__(self):
        return '%d/%d' % (self.numerator, self.denominator)

    def __repr__(self):
        return str(self)

