"""
Ese neq esta bien? Lo visto en otras soluciones es que 
use aunque sea una estructura de datos como age1[posicion] o similar para unificar             
RES el neq es redudante y si o si tiene que unificar con una de las variables definidas de ages
lany(
membero( (var(),"abogado","Vicent"), ages ),
membero( (var(),"abogado","Sean"), ages )
),  neq( (var(),"abogado","Vicent"), (var(),"abogado","Sean") ),        
"""

from kanren import run,var,eq,membero,lall,lany
from logicpuzzles import *

#ages, professions, dates
age1 = (22, var(), var())
age2 = (23, var(), var())
age3 = (24, var(), var())
age4 = (25, var(), var())
ages = (age1, age2, age3, age4)

def restricciones(ages):
    return lall(
        #1. El abogado era Vicent o Sean      
        membero( (var(),"abogado","Sean"), ages ),

        #2. Nathan era un anio mas joven que el abogado
        left_of( ages, (var(),var(),"Nathan"), (var(),"abogado",var()) ),

        #3. El joven de 24 anios era el abogado
        eq( age3[1], "abogado" ),

        #4. Vicent era el bombero
        # Funcionaria? eq( (var(), "bombero",var()), (var(),var(),"Vicent") )
        #RES: No lo haria porque unifica nada con nada
        membero( (var(), "bombero", "Vicent"), ages ),

        #5. Sean era dos anios mayor que el boxeador
        right_of( ages, (var(),var(),"Sean"), (var(),"boxeador",var()), 2),

        #Dominios dates
        #Nathan, Vicent, Sean
        membero( (var(),var(),"Max"), ages ),

        #Dominios professions
        #abogado, bombero, boxeador
        membero( (var(),"banquero",var()), ages ),
        # Dominios dates
        membero((var(), var(), "Vicent"), ages),       
    )

resultado = run(0, ages, restricciones(ages))
print(resultado)
