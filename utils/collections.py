def permutations(components):
    """
    Returns all the permutations of the provided components.
    Returns in a form of list of lists

    :param components: iterable components sequence
    :return: the list of permutations
    """
    if len(components) == 1:
        return [list(components)]
    insertion_component = components[0]
    result = []
    for permutation in permutations(components[1:]):
        for i in range(len(permutation) + 1):
            appendee = list(permutation)
            appendee.insert(i, insertion_component)
            result.append(appendee)
    return result