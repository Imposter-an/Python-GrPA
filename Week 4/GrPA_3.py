min =  None

def find_min(items: list):
    """Find the minimum value in a list of integers."""
    if not items:
        return None
    minimum = items[0]
    for item in items:
        if item < minimum:
            minimum = item
    return minimum

def odd_increment_even_decrement_no_modify(items) -> list:
    """Increment odd numbers by 1, decrement even numbers by 1, without modifying original list."""
    result = []
    for item in items:
        if item % 2 == 0:  # even
            result.append(item - 1)
        else:  # odd
            result.append(item + 1)
    return result

def odd_square_even_double_modify(items: list) -> list:
    """Square odd numbers and double even numbers, modifying the list in place."""
    for i in range(len(items)):
        if items[i] % 2 == 0:  # even
            items[i] = items[i] * 2
        else:  # odd
            items[i] = items[i] * items[i]
    return items

def more_than_two_unique_vowels(sentence):
    """Return a set of words that have more than two unique vowels."""
    vowels = set('aeiouAEIOU')
    words = sentence.split(',')
    result = set()
    
    for word in words:
        word = word.strip()  # remove whitespace
        unique_vowels = set()
        for char in word:
            if char in vowels:
                unique_vowels.add(char.lower())
        if len(unique_vowels) > 2:
            result.add(word)
    
    return result

def sum_of_list_of_lists(lol):
    """Find the sum of all integers in all nested lists."""
    total = 0
    for sublist in lol:
        for item in sublist:
            total += item
    return total

def flatten(lol):
    """Flatten a list of lists into a single list."""
    result = []
    for sublist in lol:
        for item in sublist:
            result.append(item)
    return result

def all_common(strings):
    """Find common characters present in all strings, return as string in ascending order."""
    if not strings:
        return ""
    
    # Start with characters from the first string
    common_chars = set(strings[0])
    
    # Find intersection with each subsequent string
    for string in strings[1:]:
        common_chars = common_chars.intersection(set(string))
    
    # Convert to sorted string
    return ''.join(sorted(common_chars))

def vocabulary(sentences):
    """Find unique words from all sentences, return as set in lowercase."""
    words = set()
    for sentence in sentences:
        # Split sentence into words and convert to lowercase
        sentence_words = sentence.lower().split()
        for word in sentence_words:
            words.add(word)
    return words