def num_to_word(num: int) -> str:
    '''
    Given an integer, generate a string with its digits as words separated by hyphens.

    Arguments:
    num: int - the input number

    Return:
    str - the string with digits as words separated by hyphens
    '''
    # A list to map digits (by index) to their English word.
    digit_words = [
        'zero', 'one', 'two', 'three', 'four', 
        'five', 'six', 'seven', 'eight', 'nine'
    ]
    
    # Convert the number to a string to easily iterate through its digits.
    s_num = str(num)
    
    # Create a list of words by looking up each digit in the digit_words list.
    # We convert each digit character back to an integer to use it as an index.
    words = [digit_words[int(digit)] for digit in s_num]
    
    # Join the list of words with a hyphen in between each word.
    return '-'.join(words)