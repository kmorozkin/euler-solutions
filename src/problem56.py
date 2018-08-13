'''
A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large:
one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
'''
from src.utils.digits import num2digits

max_sum = -1
for i in reversed(range(100)):
    if i % 10 == 0:
        continue
    for j in reversed(range(100)):
        digits_sum = sum(map(int, num2digits(i ** j)))
        if digits_sum > max_sum:
            max_sum = digits_sum
print(max_sum)