from kanren import run,var,eq,membero, conde

x = var()

def restriction(value):
    return eq(value, 3)

def domain(value):
    return conde([membero(x, [1,2,3,4,5,6,7,8,9]), restriction(x)])

result = run(0, x, domain(x))
print(result)