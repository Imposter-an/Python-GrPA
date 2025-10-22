def sum_of_squares(numbers):
    """Find the sum of squares of numbers in a list"""
    return sum([x**2 for x in numbers])

def total_cost(cart):
    """Given quantity and price of each item as a list of tuples, find the total cost"""
    return sum([quantity * price for quantity, price in cart])

def abbreviation(sentence):
    """Form an abbreviation by taking the first letter of each word in caps"""
    return '.'.join([word[0].upper() for word in sentence.split()]) + '.'

def palindromes(words):
    """Create a new list with only palindromes"""
    return [word for word in words if word == word[::-1]]

def all_chars_from_big_words(sentence):
    """Find all unique characters (lowercase) from words with size > 5"""
    return set([char.lower() for word in sentence.split() for char in word if len(word) > 5])

def flatten(lol):
    """Flatten a nested list"""
    return [item for sublist in lol for item in sublist]

def unflatten(items, n_rows):
    """Create a matrix with n_rows from a flat list"""
    n_cols = len(items) // n_rows
    return [[items[i * n_cols + j] for j in range(n_cols)] for i in range(n_rows)]

def make_identity_matrix(m):
    """Make an identity matrix of size m x m"""
    return [[1 if i == j else 0 for j in range(m)] for i in range(m)]

def make_lower_triangular_matrix(m):
    """Create a lower triangular matrix with the specified pattern"""
    return [[(j + 1) * (j <= i) for j in range(m)] for i in range(m)]