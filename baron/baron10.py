from kanren import *
from logicpuzzles import *

estreno1 = (2,var(),var())
estreno2 = (5,var(),var())
estreno3 = (8,var(),var())
estreno4 = (11,var(),var())
estrenos = (estreno1,estreno2,estreno3,estreno4)

def restricciones(estrenos):
    return lall(
        #
        right_of(estrenos, (var(),"let_me_out",var()), (var(),var(),"kenneth_key")),
        #
        lany(
            eq( estreno3[2], "jim_johnson" ),
            eq( estreno3[1], "tippecanoe" )
        ), neq( estreno3, (8,"tippecanoe","jim_johnson") ),
        #
        somewhat_left_of( estrenos, (var(),var(),"micah_moreno"), (var(),var(),"kenneth_key") ),
        #
        membero( (var(),"easy_to_love","kenneth_key"), estrenos ),
        #
        eq( estreno1[1], "tippecanoe" ),

        #
        membero( (var(),"fast_and_dead",var()), estrenos ),
        membero( (var(),"tippecanoe",var()), estrenos ),
        membero( (var(),var(),"jim_johnson"), estrenos ),
        membero( (var(),var(),"nan_norman"), estrenos )
    )

resultados = run(0, estrenos, restricciones(estrenos))
for valor in resultados:
    print(valor)
