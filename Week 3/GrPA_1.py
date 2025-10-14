# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
with open(__file__) as f:
    content = f.read().split("# <eoi>")[2]
if "for " in content:
    print("You should not use for loop or the word for anywhere in this exercise")

# This is the first line of the exercise
task = input()
# <eoi>

# ---Write your code below this line ---


if task == "sum_until_0":
    total = 0
    n = int(input())
    while n != 0:  # terminal condition
        total += n
        n = int(input())
    print(total)

elif task == "total_price":
    total_price = 0
    while True:  # indefinite loop
        line = input()
        if line == "END":  # terminal condition
            break
        quantity, price = line.split()
        quantity, price = int(quantity), int(price)
        total_price += quantity * price
    print(total_price)

elif task == "only_ed_or_ing":
    words = []
    while True:
        s = input()
        if s.lower() == "stop":  # terminal condition
            break
        if s.lower().endswith("ed") or s.lower().endswith("ing"):
            words.append(s)
    print("\n".join(words))

elif task == "reverse_sum_palindrome":
    def is_palindrome(num):
        s = str(num)
        return s == s[::-1]

    nums = []
    while True:
        a = input()
        if a == "-1":
            break
        n = int(a)
        rev = int(str(n)[::-1])
        if is_palindrome(n + rev):
            nums.append(str(n))
    print("\n".join(nums))

elif task == "double_string":
    lines = []
    while True:
        s = input()
        if s == "":
            break
        lines.append(s * 2)
    print("\n".join(lines))

elif task == "odd_char":
    result = []
    while True:
        s = input()
        if s.endswith("."):
            # include last string
            odd_chars = ""
            i = 0
            while i < len(s):
                if (i + 1) % 2 != 0:
                    odd_chars += s[i]
                i += 1
            result.append(odd_chars)
            break
        odd_chars = ""
        i = 0
        while i < len(s):
            if (i + 1) % 2 != 0:
                odd_chars += s[i]
            i += 1
        result.append(odd_chars)
    print(" ".join(result))

elif task == "only_even_squares":
    squares = []
    while True:
        s = input()
        if s == "NAN":
            break
        n = int(s)
        if n % 2 == 0:
            squares.append(str(n ** 2))
    print("\n".join(squares))

elif task == "only_odd_lines":
    lines = []
    count = 1
    while True:
        s = input()
        if s == "END":
            break
        if count % 2 != 0:
            lines.insert(0, s)  # prepend to make reverse order
        count += 1
    print("\n".join(lines))