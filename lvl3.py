from kanren import conde, var, run, eq
from kanren.constraints import neq

x = var()
result = run(0,x, neq(x,2), conde( [eq(x,1)], [eq(x,2)] ))
print(result)