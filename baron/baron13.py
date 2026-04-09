from kanren import *
from logicpuzzles import *

train1 = ("march", var(),var())
train2 = ("april", var(),var())
train3 = ("may", var(), var())
train4 = ("june", var(), var())
trains = (train1, train2, train3, train4)

def restrictions(trains):
    return lall(
        #
        left_of(trains, (var(),"mcgruff",var()),(var(),"aries",var()), 2),

        #
        eq( train2[2], "ramsey" ),

        #
        membero( (var(),"aries","yates"), trains ),

        #
        membero( (var(),"jaws",var()), trains ),
        membero( (var(),"barca",var()), trains ),

        membero( (var(),var(),"ramsey"), trains ),
        membero( (var(),var(),"quinn"), trains ),
        membero( (var(),var(),"goodwin"), trains ),
    )

results = run(0, trains, restrictions(trains),
            differents(trains, ( ("may",), ("barca",), ("ramsey","quinn",) )    ))
for result in results:
    print(result)
