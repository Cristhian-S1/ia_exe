from kanren import *
from logicpuzzles import *

preparation1 = (4.50, var(), var())
preparation2 = (5.50, var(), var())
preparation3 = (6.50, var(), var())
preparation4 = (7.50, var(), var())
preparations = (preparation1, preparation2, preparation3, preparation4)

"""
1. The variety that requires 190 degree water costs 1 dollar less than the variety that requires 195 degree water.
2. The Pouchong costs 1 dollar less than the Red Robe.
3. The Pouchong needs 195 degree water.
4. The four teas are the Ali Shan, the variety that costs $6.50, the variety that requires 
200 degree water and the tea that requires 190 degree water.

 Jarvis is teaching a small group of friends how to properly brew several different types of tea. 
 Using only the clues that follow, determine the ideal temperature and steep time for each tea, as well 
 as its price per pound.
"""

def restrictions(preparations):
    return lall(
        #
        left_of( preparations, (var(),190,var()), (var(),195,var()) ),

        #
        left_of( preparations, (var(),var(),"pouchong"),(var(),var(),"red_robe") ),

        #
        membero( (var(),195,"pouchong"), preparations ),

        #
        membero( (var(),200,var()), preparations ),
        membero( (var(),215,var()), preparations ),

        membero( (var(),var(),"ali_shan"), preparations ),
        membero( (var(),var(),"jin_xuan"), preparations ),
    )

results = run(0, preparations, restrictions(preparations), 
            differents( preparations, ( (6.50,),(190,200,),("ali_shan",) ) )
            )
for result in results:
    print(result)
