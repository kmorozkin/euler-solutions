'''
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576
 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as
the concatenated product of an integer with (1,2, ... , n) where n > 1?

'''
from utils.digits import num2digits, digits2num


def pandigital(num, digitsNumber = 9):
    digits = []
    multiplier = 1
    while len(digits) < digitsNumber:
        multiplied = num * multiplier
        digits.extend(num2digits(multiplied))
        multiplier += 1
    return digits

def isPandigital(digits, digitsNumber = 9):
    legals = set(range(1, digitsNumber + 1))
    length = len(digits)
    return length == digitsNumber \
           and legals.issuperset(digits) \
           and length == len(set(digits))

def generateSeeds():
    seeds = [9]
    def permute(seed):
        seedDigits = num2digits(seed)
        legalDigits = list(set(range(1, 10)).difference(seedDigits))
        legalDigits.sort(reverse=True)
        for i in legalDigits:
            yield seed * 10 + i
    for seed in seeds:
        yield seed
        seeds.extend(permute(seed))

gen = generateSeeds()
max = maxSeed = iteration = -1
for i in range(4000):
    nextSeed = next(gen)
    pandigitalDigits = pandigital(nextSeed)
    if isPandigital(pandigitalDigits):
        number = digits2num(pandigitalDigits)
        if number > max:
            max, maxSeed, iteration = number, nextSeed, i
print('{}, seed: {} on iteration {}'.format(max, maxSeed, iteration))
