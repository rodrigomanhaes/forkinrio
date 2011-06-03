class Number(int):

    def is_odd(self):
        return not self.is_even()

    def is_even(self):
        return self % 2 == 0

    @property
    def roman(self):
        def convert(n, one, five, ten):
            if n == 0:
                return ''
            elif n <= 3:
                return one * n
            elif n == 4:
                return one + five
            elif n == 5:
                return five
            elif n <= 8:
                return five + (one * (n - 5))
            else: #9
                return one + ten
        return '%s%s%s%s' % (
            convert(self / 1000, 'M', '', ''),
            convert(self % 1000 / 100, 'C', 'D', 'M'),
            convert(self % 1000 % 100 / 10, 'X', 'L', 'C'),
            convert(self % 1000 % 100 % 10, 'I', 'V', 'X'))


    @property
    def fibonacci(self):
        if self in [1, 2]:
            return 1
        return Number(Number(self - 1).fibonacci + Number(self - 2).fibonacci)

    def looping_factorial(self):
        result = 1
        for n in range(1, self + 1):
            result *= n
        return result

    def recursive_factorial(self):
        if self == 0:
            return Number(1)
        return Number(self * Number(self - 1).recursive_factorial())

    def functional_factorial(self):
        return Number(reduce(lambda a, b: a * b, range(1, self + 1)))

