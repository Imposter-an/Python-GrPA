def get_goals(filename, country):
    """
    Get the count of players and their cumulative goals for this country

    Arguments:
        filename: string
        country: string
    Return: 
        result: tuple, (integer, integer)
        
    """

    
    import csv
    # Initialize variables to store the count of players and total goals.
    num_players = 0
    num_goals = 0
    country_found = False

    # Use a 'with' statement to open the CSV file. This ensures the file
    # is automatically closed.
    with open(filename, 'r', newline='') as csvfile:
        # Create a CSV reader object to iterate over the rows.
        reader = csv.reader(csvfile)

        # Skip the header row.
        next(reader, None)

        # Iterate through each row in the CSV file.
        for row in reader:
            # Check if the row is not empty and has the expected number of columns.
            if row and len(row) == 3:
                # The country is in the second column (index 1).
                # The goals are in the third column (index 2).
                player_country = row[1].strip()
                player_goals = int(row[2].strip())

                # If the player's country matches the target country.
                if player_country == country:
                    country_found = True
                    num_players += 1
                    num_goals += player_goals

    # After checking all rows, if the country was found, return the results.
    if country_found:
        return (num_players, num_goals)
    # Otherwise, if the country was not present in the file, return (-1, -1).
    else:
        return (-1, -1)