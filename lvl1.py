from kanren import *

def regla(value):
    return eq(value,5), eq(value,2)

x=var()
print( run(1,x,regla(x)) )


"""
Entonces, ¿para qué sirve run?
run es quien hace realidad la declaración:

# Declaras las "reglas"
eq(x, 5)           # "x es 5"
eq(y, x)           # "y es x"  
membero(z, [1,2,3]) # "z está en [1,2,3]"

# run busca soluciones que CUMPLAN todas las declaraciones
run(1, x, eq(x, 5))        # Encuentra: x debe ser 5
run(1, y, eq(y, x), eq(x, 5))  # Encuentra: y debe ser 5
run(3, z, membero(z, [1,2,3]))  # Encuentra: z puede ser 1,2,3
"""