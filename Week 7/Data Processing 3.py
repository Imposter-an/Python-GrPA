# Take the input from standard input using input()
# and print the output according to the problem .

# Write your code here
def solve():
  """
  Main function to read input, process each sequence, and print the result.
  """
  try:
    # Read the total number of word sequences.
    num_sequences = int(input())
  except (ValueError, EOFError):
    # Handle cases where input is not a number or is empty.
    num_sequences = 0

  # Loop through each sequence.
  for _ in range(num_sequences):
    # Read the line containing the comma-separated words.
    sequence_str = input()

    # Split the string into a list of words and filter out any empty strings.
    # An empty string might occur if there are consecutive commas, e.g., "a,,b".
    words = [word for word in sequence_str.split(',') if word]

    # If there are no valid words after filtering, the longest subsequence is 0.
    if not words:
      print(0)
      continue

    # The minimum possible length is 1 (a single word).
    max_length = 1
    current_length = 1

    # Iterate through the list of words starting from the second word.
    for i in range(1, len(words)):
      # Get the previous and current words for comparison.
      prev_word = words[i-1]
      current_word = words[i]

      # Check for the antakshari property:
      # last letter of the previous word == first letter of the current word.
      if prev_word[-1] == current_word[0]:
        # If the property holds, extend the current chain.
        current_length += 1
      else:
        # If the chain is broken, reset the counter to 1 for the new word.
        current_length = 1

      # Update the maximum length found so far.
      if current_length > max_length:
        max_length = current_length

    # Print the final result for the current sequence.
    print(max_length)

# Run the solution
solve()