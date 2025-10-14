# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
with open(__file__) as f:
    content = f.read().split("# <eoi>")[2]
if "while " in content:
    print("You should not use while loop or the word while anywhere in this exercise")

# your code should not use more than 7 for loops 
# assuming one for loop per problem
if content.count("for ")>7:
    print("You should not use more than 7 for loops")

# This is the first line of the exercise
task = input()
# <eoi>


# ---Write your code below this line ---


if task == 'factorial':  # Accumulation
    n = int(input())
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(result)

elif task == 'even_numbers':  # Just Iterating
    n = int(input())
    for i in range(0, n + 1, 2):   # include 0 and n if even
        print(i)

elif task == 'power_sequence':  # Mapping
    n = int(input())
    result = 1
    for i in range(n):
        print(result)
        result *= 2



elif task == 'sum_not_divisible':  # Filtered Accumulation
    n = int(input())
    total = 0
    for i in range(1, n):
        if i % 4 != 0 and i % 5 != 0:
            total += i
    print(total)

elif task == 'from_k':  # Filtering + Mapping
    n = int(input())
    k = int(input())
    count = 0
    for i in range(k, 0, -1):  # decreasing from k downwards
        if count == n:
            break
        if i % 2 == 1 and '5' not in str(i) and '9' not in str(i):
            print(str(i)[::-1])
            count += 1


elif task == 'string_iter':  # Iterable Mapping
    s = input().strip()
    prev = 1
    for ch in s:
        curr = int(ch)
        print(curr * prev)
        prev = curr

elif task == 'list_iter':  # Iterable Mapping (list)
    l = eval(input())  # read list like [1, 2.0, 'three', True]
    for item in l:
        print(f"{item} - type: {type(item)}")  # full class representation

else:
    print("Invalid")