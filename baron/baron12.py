from kanren import *
from logicpuzzles import *

telescopio1 = (4,var(),var())
telescopio2 = (6,var(),var())
telescopio3 = (8,var(),var())
telescopio4 = (10,var(),var())
telescopios = (telescopio1, telescopio2, telescopio3, telescopio4 )

"""
1. The scope with a tracking mount has an aperture smaller than the telescope with a Dobsonian mount.
2. The Omni scope, the scope with an alt-az mount and the telescope with 6 inches of aperture are all different telescopes.
3. The Sky-Watcher scope has an aperture 4 inches smaller than the telescope with an equatorial mount.
4. The telescope with a Dobsonian mount has an aperture of 6 inches.
5. The telescope with 4 inches of aperture is either the Omni scope or the Vixen telescope.
6. The telescope with 10 inches of aperture is a Meade.


The Pinecrest Astronomy Club has set up a row of telescopes on the hilltop for its monthly public viewing night, 
and club president Earl is explaining each instrument to the visitors. Determine the aperture of each telescope, 
its mount type, brand, and the member who brought it.
"""


def restricciones(telescopios):
    return lall(
        #
        somewhat_left_of( telescopios, (var(),"tracking",var()), (var(),"dobson",var()) ),
        
        #
        
        #
        left_of( telescopios, (var(),var(),"sky_watcher"),(var(),"ecuatorial",var()),2),
        #
        eq( telescopio2[1], "dobson" ),
        #
        lany(
            eq( telescopio1[2], "omni" ),
            eq( telescopio1[2], "vixen" )
        ),
        #
        eq( telescopio4[2], "meade" ),

        #
        membero( (var(),"alt-az",var()), telescopios ),
        membero( (var(),var(),"omni"), telescopios ),
        membero( (var(),var(),"meade"), telescopios ),
        membero( (var(),var(),"vixen"), telescopios ),
    )

resultados = run(0, telescopios, restricciones(telescopios),
             differents(telescopios, ( (6,),("alt-az",),("omni",) ) ) )
for resultado in resultados:
    print(resultado)
