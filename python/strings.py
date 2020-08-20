"""Everything to do with strings."""


def common_letters(str1, str2):
    """Return common letters between two strings."""
    dict_ = []
    if len(str1) > len(str2):
        str_ = str1
    else:
        str_ = str2
    for letter in str_:
        if letter in str2 and letter in str1 and letter not in dict_:
            dict_.append(letter)
    return dict_


"""Easy way to cast every element in stdin to a specific data type, e.g. int"""
input_items = list(map(int, input().rstrip().split()))
