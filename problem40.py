'''

An irrational decimal fraction is created by concatenating the positive integers:

0.12345678910_1_112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

'''
from utils.digits import num2digits


def digit_gen():
    current = 1
    while True:
        for digit in num2digits(current):
            yield digit
        current += 1

saved = ['stub']
gen = digit_gen()
for i in range(1000000):
    saved.append(next(gen))

result = 1
for i in [1, 10, 100, 1000, 10000, 100000, 1000000]:
    result *= saved[i]
print(result)