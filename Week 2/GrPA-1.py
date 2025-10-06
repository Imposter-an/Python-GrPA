x1 = input()
x2 = input()
y1 = input()
y2 = input()
y3 = input()
z = input()

# swap the values of `x1` and `x2`
x1 , x2 = x2 , x1
# do a circular swap of `y1`, `y2` and `y3`  like y1 = y2, y2 = y3, y3 = y1 
y1, y2, y3 = y2, y3, y1
# create a new variable `a` with the value of `z`
a = z
# delete the variable `z`
del z
print(x1)
print(x2)
print(y1)
print(y2)
print(y3)
print(a)