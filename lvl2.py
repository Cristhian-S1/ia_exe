from kanren import membero, run, var

x = var()

result = run(1,x,membero(x, [1,2,3]))
print(result)