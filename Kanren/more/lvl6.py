from kanren import run,var,eq,lany,lall,membero
from kanren.constraints import neq

# amigo(nombre, bebida)
#Alberto, Berta, Carlos
amigos = [ 
    ["Alberto", var()], 
    ["Berta", var()], 
    ["Carlos", var()] 
]


def dominio(amigos):
    # 1. Cada uno de ellos pide te o cafe
    return lall(
        membero( amigos[0][1], ["te","cafe"] ),
        membero( amigos[1][1], ["te","cafe"] ),
        membero( amigos[2][1], ["te","cafe"] )
    )

def restricciones1(amigos):
    # 2. Si Alberto pide cafe, entonces Berta pide lo mismo que Carlos  
    return lany( neq(amigos[0][1],"cafe"), eq(amigos[1][1], amigos[2][1]) )

def restricciones2(amigos):
    # 3. Si Berta pide cafe, entonces Alberto pide la bebida que no pide Carlos
    return lany(neq(amigos[1][1],"cafe"), neq(amigos[0][1], amigos[2][1]))

def restricciones3(amigos):
    # 4. Si Carlos pide te, entonces Alberto pide la misma bebida que Berta
    return lany(neq(amigos[2][1],"te"), eq(amigos[0][1],amigos[1][1]))

def restricciones(amigos):
    return lall(restricciones1(amigos),restricciones2(amigos),restricciones3(amigos)) 

# Todas las soluciones (mundos) posibles
result = run(0, amigos, dominio(amigos), restricciones(amigos))
print(result)

# Quien siempre pide la misma bebida (en todos los mundos posibles)
# Estrategia: Se crea un conjunto (a) para cada uno de los estados posibles de cada amigo (i) 
# en cada solucion encontrada (s).
# Se verifica que todos los estados sean el mismo: len(set(a)) == 1