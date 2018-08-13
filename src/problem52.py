'''
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

'''
from src.utils.digits import num2digits


def test(number, end=2):
    number_digits = set(num2digits(number))
    for x in range(2, end + 1):
        multiplied = number * x
        multiplied_digits = set(num2digits(multiplied))
        if not number_digits == multiplied_digits:
            return False
    return True


num = 1
while not test(num, 6):
    num += 1
print(num)

