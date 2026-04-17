from kanren import *
from logicpuzzles import *

camara1 = (1930,var(),var())
camara2 = (1940,var(),var())
camara3 = (1950,var(),var())
camara4 = (1960,var(),var())
camaras = (camara1,camara2,camara3,camara4)

def restricciones(camaras):
    return lall(
        #
        lany(
            eq( camara3[2], 28 ),
            eq( camara3[1], "rolleiflex" )
         ), neq( camara3, (1950,"rolleiflex",28) ),
        #
        eq( camara2[1], "pentax" ),

        #
        left_of(camaras, (var(),var(),70),(var(),var(),9.5)),

        #
        membero( (var(),"canon",28), camaras ),

        #
        left_of(camaras, (var(),"rolleiflex",var()), (var(),"pentax",var())),

        #
        membero( (var(),var(),35), camaras ),
        membero( (var(),"nikon",var()), camaras )
    )

resultados = run(0, camaras, restricciones(camaras))
for valor in resultados:
    print(valor)
