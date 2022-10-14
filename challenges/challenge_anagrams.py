def is_anagram(first_string, second_string):
    if (first_string  == "" or second_string == ""):
        return False
    
    first = list(first_string.lower())
    second = list(second_string.lower())

    for index in first:
        if (first.count(index) != second.count(index)):
            return False

    return True

    
