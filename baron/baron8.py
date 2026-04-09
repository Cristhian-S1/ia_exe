from kanren import *
from logicpuzzles import *

# fecha, cliente, guia
buceo1 = (13, var(), var())
buceo2 = (14, var(), var())
buceo3 = (15, var(), var())
buceo4 = (16, var(), var())
buceos = (buceo1,buceo2,buceo3,buceo4)

def restricciones(buceos):
    return lall(

        #
        membero( (var(),"ayers","ted"), buceos ),

        #
        right_of(buceos, (var(),"blake",var()), (var(),"ferrell",var()),2),

        #
        lany(
            membero( (var(),"blake","zachary"), buceos),
            eq( buceo1[2], "zachary" )
        ), neq(buceo1, (13,"blake","zachary")),

        #
        eq( buceo1[2], "willard" ),

        #
        left_of( buceos, (var(),"blake",var()),(var(),"erickson",var()) ),

        #
        membero( (var(),var(),"muriel"), buceos ),
        membero( (var(),var(),"willard"), buceos ),
        membero( (var(),var(),"zachary"), buceos )
    )

resultados = run(0, buceos, restricciones(buceos))
for valor in resultados:
    print(valor)
