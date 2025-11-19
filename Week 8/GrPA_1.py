def get_freq(filename):
    """
    Extract frequency information from the file

    Argument:
        filename: string, path to file
    Return:
        result: dictionary; keys are strings, values are integers
    """



    
    # Initialize an empty dictionary to store the frequency of each word.
    word_frequencies = {}

    # Use a 'with' statement to open the file. This ensures that the file
    # is automatically closed even if errors occur.
    with open(filename, 'r') as f:
        # Iterate through each line in the file.
        for line in f:
            # Remove any leading/trailing whitespace, including the newline
            # character, from the line to get the clean word.
            word = line.strip()

            # Check if the word is not an empty string after stripping.
            if word:
                # Use the .get() method to retrieve the current count of the word.
                # If the word is not yet in the dictionary, .get() returns the
                # default value of 0. We then add 1 to the count.
                word_frequencies[word] = word_frequencies.get(word, 0) + 1

    # Return the dictionary containing the words and their frequencies.
    return word_frequencies