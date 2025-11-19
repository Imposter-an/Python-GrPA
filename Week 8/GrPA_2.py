def relation(file1, file2):
    """
    Determine the relationship between two files

    Arguments:
        file1, file2: strings, paths to two files
    Return:
        string: 'Equal', 'Subset' or 'No Relation'
    """


    
    # Use 'with' statements to ensure both files are properly closed.
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        # Read all lines from both files into lists.
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    # Get the number of lines in each file.
    num_lines1 = len(lines1)
    num_lines2 = len(lines2)

    # Iterate through the lines of the first file and compare with the
    # corresponding lines of the second file.
    for i in range(num_lines1):
        # Strip whitespace (including newline characters) before comparing.
        if lines1[i].strip() != lines2[i].strip():
            # If any pair of corresponding lines do not match, there is no relation.
            return 'No Relation'

    # If the loop completes, it means all lines in file1 match the
    # corresponding lines in file2. Now, we check the lengths to determine
    # the exact relationship.

    # If the number of lines are equal, the files are 'Equal'.
    if num_lines1 == num_lines2:
        return 'Equal'
    # If file1 has fewer lines than file2, it is a 'Subset'.
    # The prompt guarantees that num_lines1 <= num_lines2.
    else:
        return 'Subset'