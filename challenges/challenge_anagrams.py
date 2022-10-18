def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    first = list(first_string.lower())
    second = list(second_string.lower())

    for index in first:
        if index not in second:
            return False
        else:
            second.remove(index)

    return True
