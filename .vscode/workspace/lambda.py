def cube(x):
    return x*x*x
ls = [20,1,3,5,6]
l = list(map(lambda x: x*x*x, ls))
print(l)