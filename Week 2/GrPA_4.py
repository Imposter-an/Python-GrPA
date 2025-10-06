import math

operation = input()

if operation == "odd_num_check":
    number = int(input())
    if number % 2 != 0:
        print("yes")
    else:
        print("no")

elif operation == "perfect_square_check":
    number = int(input())
    if int(math.sqrt(number)) ** 2 == number:
        print("yes")
    else:
        print("no")

elif operation == "vowel_check":
    text = input().lower()
    vowels = "aeiou"
    found = False
    for ch in text:
        if ch in vowels:
            found = True
            break
    if found:
        print("yes")
    else:
        print("no")

elif operation == "divisibility_check":
    number = int(input())
    div2 = (number % 2 == 0)
    div3 = (number % 3 == 0)
    if div2 and div3:
        print("divisible by 2 and 3")
    elif div2:
        print("divisible by 2")
    elif div3:
        print("divisible by 3")
    else:
        print("not divisible by 2 and 3")

elif operation == "palindrominator":
    text = input()
    if len(text) > 1:
        result = text + text[-2::-1]
    else:
        result = text
    print(result)

elif operation == "simple_interest":
    principal = int(input())
    years = int(input())
    if years < 10:
        rate = 5
    else:
        rate = 8
    si = (principal * rate * years) / 100
    print(round(si))

else:
    print("Invalid Operation")