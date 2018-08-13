'''
It is possible to show that the square root of two can be expressed as an infinite continued F.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first
example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many Fs contain a numerator with more digits than denominator?
'''
from fractions import Fraction

F1 = Fraction(1)

num = F1
result = 0
for i in range(1000):
    num = F1 + F1 / (num + F1)
    if len(str(num.numerator)) > len(str(num.denominator)):
        result += 1
print(result)
