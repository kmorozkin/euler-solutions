def num2digits(num: int) -> list:
    '''
    Produces a list of the digits that form the input number.

    :param num: the input integer to be split to digits
    :return: the list of integers, the eldest is the first
    '''
    digits = []
    current = num
    while current:
        digit = current % 10
        digits.append(digit)
        current //= 10
    digits.reverse()
    return digits


def digits2num(digits: list) -> int:
    '''
    Unites the digits list into the number.
    The function assumes that the first element of the list
    has the largest rank.
    This function has a reverse effect of num2digits

    :param digits: the list of integers
    :return: the number that consists of these digits
    '''
    multiplier = 1
    result = 0
    for num in reversed(digits):
        result += num * multiplier
        multiplier *= 10
    return result