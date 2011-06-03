class ComplexNumber(object):

    def __init__(self, real, imaginary):
        self._real = real
        self._imaginary = imaginary

    @property
    def real(self):
        return self._real

    @property
    def imaginary(self):
        return self._imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        return ComplexNumber(real=self.real + other.real,
                              imaginary=self.imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(real=self.real - other.real,
                              imaginary=self.imaginary - other.imaginary)

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.imaginary * other.real + self.real * other.imaginary
        return ComplexNumber(real=real, imaginary=imaginary)

    def __div__(self, other):
        numerator = other.real * other.real + other.imaginary * other.imaginary * 1.
        real = (self.real * other.real + self.imaginary * other.imaginary) / numerator
        imaginary = (self.imaginary * other.real - self.real * other.imaginary) / numerator
        return ComplexNumber(real=real, imaginary=imaginary)

    def __str__(self):
        return '%d+%di' % (self.real, self.imaginary)

