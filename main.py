import math


class Figure:
    def __init__(self):
        self.S = 0
        self.name = 'None'

    def square_out(self):
        if self.S > 0:
            print('The area of the ' + self.name + ' equals ' + f'{self.S:0.2f}')
        else:
            print('The shape with the specified parameters does not exist')

    @staticmethod
    def input_check(txt: str):
        x = input(txt)
        if not x.isdigit():
            while not x.isdigit():
                print('ERROR! INPUT VALUE IS INCORRECT!\n')
                x = input(txt)
            return float(x)
        else:
            return float(x)


class Circle (Figure):
    def __init__(self):
        Figure.__init__(self)
        self.name = 'circle'
        self.r = 0

    def square(self):
        self.S = math.pi * self.r ** 2

    def input(self):
        self.r = self.input_check('Set radius: ')

    def run(self):
        self.input()
        self.square()
        self.square_out()


class Triangle(Figure):
    def __init__(self):
        Figure.__init__(self)
        self.name = 'triangle'
        self.a = 0
        self.b = 0
        self.c = 0

    def square(self):
        if self.a + self.b < self.c or self.c + self.a < self.b or self.b + self.c < self.a:
            self.S = 0
        else:
            p = self.a + self.b + self.c
            half_p = p / 2
            self.S = math.sqrt(half_p * (half_p - self.a) * (half_p - self.b) * (half_p - self.c))

    def input(self):
        self.a = self.input_check('Set side a: ')
        self.b = self.input_check('Set side b: ')
        self.c = self.input_check('Set side c: ')

    def is_rect(self):
        hypot = max(self.a, self.b, self.c)
        if hypot**2 == self.a**2 + self.b**2 + self.c**2 - hypot**2:
            print('Triangle is rectangular')
        else:
            print('Triangle is not rectangular')

    def run(self):
        self.input()
        self.square()
        self.square_out()
        self.is_rect()



print('\n------------------CIRCLE------------------\n')

circle = Circle()
circle.run()

print('\n-----------------TRIANGLE-----------------\n')

triangle = Triangle()
triangle.run()

