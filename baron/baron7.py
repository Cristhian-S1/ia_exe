from kanren import *
from logicpuzzles import *

expedition1 = ("january", var(), var())
expedition2 = ("february", var(), var())
expedition3 = ("march", var(), var())
expedition4 = ("april", var(), var())
expeditions = (expedition1,expedition2,expedition3,expedition4)

def restrictions(expeditions):
    return lall(
    
        #2. Connie's team will leave sometime after Noel's team.
        #2. El equipo de Connie saldrá en algún momento después del equipo de Noel.
        somewhat_right_of(expeditions, (var(),var(),"connie"), (var(),"noel",var())),

        #3. Connie's expedition will be either Horace's expedition or Noel's team.
        #3. La expedición de Connie será la expedición de Horace o el equipo de Noel.
        lany(
            membero( (var(),"horace","connie"), expeditions ),
            membero( (var(),"noel","connie"), expeditions )
        ),

        #4. The expedition leaving in February will be either Kay's expedition or Yolanda's team.
        #4. La expedición que sale en febrero será la expedición de Kay o el equipo de Yolanda.
        lany(
            eq( expedition2[2], "kay" ), 
            eq( expedition2[2], "yolanda" )
        ),

        #5. Darrell's team will include Yolanda. 
        #5. El equipo de Darrell incluirá a Yolanda.
        membero( (var(), "darrell", "yolanda"), expeditions ),

        #Dominios
        membero( (var(),var(),'kay'), expeditions ),
        membero( (var(),var(),'amelia'), expeditions ),

        membero( (var(),"horace",var()), expeditions ),
        membero( (var(),"zachary",var()), expeditions )
    )


#1. The four teams will be Zachary's expedition, Amelia's expedition, the expedition leaving in March and the expedition leaving in February.
#1. Los cuatro equipos serán: la expedición de Zachary, la expedición de Amelia, la expedición que sale en marzo y la expedición que sale en febrero.
results = run(0, expeditions, restrictions(expeditions),
            differents(expeditions, (("march","february",),("zachary",),("amelia",)) ))

for v in results:
    print(v)