from bisect import bisect_left

def in_list(coll, elem, lo=0, hi=None):
    """
    Returns True if the element is present in the input collection range, full by default.

    :param coll: input collection
    :param elem: element to be checked
    :param lo: lower collection boundary index
    :param hi: higher collection boundary index
    :return: True if element is in the collection, false otherwise
    """
    hi = hi or len(coll)
    idx = bisect_left(coll, elem)
    return idx < hi and coll[idx] == elem


def partition(coll, n, step=None, pad=None):
    """
    Returns a sequence of lists of n items each, at offsets step
    apart. If step is not supplied, defaults to n, i.e. the partitions
    do not overlap. If a pad collection is supplied, use its elements as
    necessary to complete last partition up to n items. In case there are
    not enough padding elements, return a partition with less than n items.

    :param coll: input list
    :param n: the size of partitions
    :param step: index step in partitions
    :param pad: additional element to fill
    :return: partitioned list
    """
    def item(idx):
        return coll[idx] if idx < len(coll) else pad

    step = step or n
    i = 0
    result = []

    while (pad and i < len(coll)) or i + n <= len(coll):
        items = tuple(item(idx) for idx in range(i, i + n))
        result.append(items)
        i += step

    return result