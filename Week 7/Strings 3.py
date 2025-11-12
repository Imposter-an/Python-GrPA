def most_occuring_first_letter(passage: str) -> str:
    '''
    Returns the letter which occurs most frequently 
    as the first letter of any word.(case insensitive)
    Args:
        passage (str): A multi-line string representing the passage.
    Returns:
        str: The most frequently occurring first letter in lowercase.
    '''
    # Dictionary to count first letters
    first_letter_count = {}
    
    # Split the passage into words
    words = passage.split()
    
    # Count first letters
    for word in words:
        if word:  # Check if word is not empty
            first_letter = word[0].lower()  # Get first letter in lowercase
            first_letter_count[first_letter] = first_letter_count.get(first_letter, 0) + 1
    
    # Find the letter with maximum count
    most_frequent_letter = max(first_letter_count, key=first_letter_count.get)
    
    return most_frequent_letter