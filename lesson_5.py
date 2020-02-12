import math


class Complex(object):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real,
                       self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real,
                       self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real*other.real - self.imag*other.imag,
                       self.imag*other.real + self.real*other.imag)

    def __abs__(self):
        return sqrt(self.real**2 + self.imag**2)


number_1 = input("enter first complex namber ")
number_2 = input("enter second complex namber ")

my_list_1 = []
my_list_2 = []

def splitter(a, list_of_numbers):
    splited_number = a.split(' ')
    for i in splited_number:
        list_of_numbers.append(int(i))
    return list_of_numbers

splitter(number_1, my_list_1)
splitter(number_2, my_list_2)

complex_number_1 = complex(my_list_1[0], my_list_1[1])
complex_number_2 = complex(my_list_2[0], my_list_2[1])

print(complex_number_1 + complex_number_2)
print(complex_number_1 * complex_number_2)
