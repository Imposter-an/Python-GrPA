task = input()

# ---Write your code below this line ---


if task == "permutation":
    s = input().strip()
    n = len(s)
    for i in range(n):
        for j in range(n):
            if i != j:
                print(s[i] + s[j])


elif task == "sorted_permutation":
    s = input().strip()
    n = len(s)
    for i in range(n):
        for j in range(n):
            if i != j and s[i] < s[j]:  # first character before second alphabetically
                print(s[i] + s[j])

elif task == "repeat_the_repeat":
    n = int(input())
    line = "".join(str(i) for i in range(1, n + 1))
    for _ in range(n):
        print(line)


elif task == "repeat_incrementally":
    n = int(input())
    for i in range(1, n + 1):
        line = "".join(str(j) for j in range(1, i + 1))
        print(line)


elif task == "increment_and_decrement":
    n = int(input())
    for i in range(1, n + 1):
        inc = "".join(str(j) for j in range(1, i + 1))
        dec = "".join(str(j) for j in range(i - 1, 0, -1))
        print(inc + dec)

else:
    print("Invalid")