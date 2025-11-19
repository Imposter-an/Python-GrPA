def num_to_words(mat):
    """
    Convert matrix to file

    Argument: 
        mat: list of lists
    Return:
        None
    """


    # A mapping from single-digit integers to their English word form.
    digit_map = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
    }

    # A list to hold the lines of text that will be written to the file.
    lines_to_write = []

    # Iterate through each row of the input matrix.
    for row in mat:
        # For each number in the current row, find its corresponding word
        # from the digit_map and create a new list of words.
        word_row = [digit_map[num] for num in row]
        
        # Join the words in the word_row with a comma to create a single
        # string representing the line for the CSV file.
        line = ','.join(word_row)
        
        # Add the newly created line to our list of lines.
        lines_to_write.append(line)

    # Open the file 'words.csv' in write mode ('w'). This will create the
    # file if it doesn't exist or overwrite it if it does.
    with open('words.csv', 'w') as f:
        # Join all the lines in our list with a newline character.
        # This method ensures that a newline is placed between lines but
        # not at the very end of the file, satisfying the requirement.
        output_string = '\n'.join(lines_to_write)
        f.write(output_string)