def is_odd_indices_alpha_and_even_indices_digits(string: str) -> bool:
    '''
    Given a string, check if all the odd indices are alphabets and the even indices are digits.
    Note: indices starts from 0.
    Arguments:
    string: str - the input string
    Return:
    bool - True if all odd indices are alphabets and even indices are digits, else False
    '''
    for i in range(len(string)):
        if i % 2 == 0:  # Even index (0, 2, 4, ...)
            if not string[i].isdigit():
                return False
        else:  # Odd index (1, 3, 5, ...)
            if not string[i].isalpha():
                return False
    
    return True