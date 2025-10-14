# this is to ensure that you cannot use the built in any, all and min function for this exercise but you can use it in the OPPEs.
any = None 
all = None
min = None 

task = input()

# ---Write your code below this line ---


if task == 'factorial':
    n = int(input())
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(result)

elif task == 'even_numbers':
    n = int(input())
    for i in range(0, n + 1, 2):
        print(i)

elif task == 'power_sequence':
    n = int(input())
    val = 1
    for _ in range(n):
        print(val)
        val *= 2

elif task == 'sum_not_divisible':
    n = int(input())
    total = 0
    for i in range(1, n):
        if i % 4 != 0 and i % 5 != 0:
            total += i
    print(total)

elif task == 'from_k':
    n = int(input())
    k = int(input())
    count = 0
    for i in range(k, 0, -1):
        if count == n:
            break
        if i % 2 == 1 and '5' not in str(i) and '9' not in str(i):
            print(str(i)[::-1])
            count += 1


elif task == 'string_iter':
    s = input().strip()
    prev = 1
    for ch in s:
        curr = int(ch)
        print(curr * prev)
        prev = curr

elif task == 'list_iter':
    l = eval(input())
    for item in l:
        print(f"{item} - type: {type(item)}")


elif task == 'permutation':
    s = input().strip()
    n = len(s)
    for i in range(n):
        for j in range(n):
            if i != j:
                print(s[i] + s[j])

elif task == 'sorted_permutation':
    s = input().strip()
    n = len(s)
    for i in range(n):
        for j in range(n):
            if i != j and s[i] < s[j]:
                print(s[i] + s[j])

elif task == 'repeat_the_repeat':
    n = int(input())
    line = [str(i) for i in range(1, n + 1)]
    for _ in range(n):
        for num in line:
            print(num)

elif task == 'repeat_incrementally':
    n = int(input())
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j)

elif task == 'increment_and_decrement':
    n = int(input())
    for i in range(1, n + 1):
        # increment
        for j in range(1, i + 1):
            print(j)
        # decrement
        for j in range(i - 1, 0, -1):
            print(j)


elif task == "factors":
    n = int(input())
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

elif task == "find_min":
    n = int(input())
    numbers = []
    for _ in range(n):
        numbers.append(int(input()))
    smallest = numbers[0]
    for num in numbers[1:]:
        if num < smallest:
            smallest = num
    print(smallest)

elif task == "prime_check":
    n = int(input())
    if n <= 1:
        print("False")
    else:
        is_prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        print("True" if is_prime else "False")

elif task == "is_sorted":
    s = input().strip()
    sorted_flag = True
    for i in range(1, len(s)):
        if s[i] < s[i - 1]:
            sorted_flag = False
            break
    print("True" if sorted_flag else "False")

elif task == "any_true":
    n = int(input())
    divisible = False
    for _ in range(n):
        num = int(input())
        if num % 3 == 0:
            divisible = True
    print("True" if divisible else "False")

elif task == "manhattan":
    x, y = 0, 0
    while True:
        direction = input().strip()
        if direction == "STOP":
            break
        if direction == "UP":
            y += 1
        elif direction == "DOWN":
            y -= 1
        elif direction == "LEFT":
            x -= 1
        elif direction == "RIGHT":
            x += 1
    print(abs(x) + abs(y))

else:
    print("Invalid")