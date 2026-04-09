from logicpuzzles import *
from time import perf_counter


# equipos(mes, chriptologists, speleologists)
equipo1 = ('January', var(), var())
equipo2 = ('February', var(), var())
equipo3 = ('March', var(), var())
equipo4 = ('April', var(), var())


equipos = (equipo1, equipo2, equipo3, equipo4)


def problemaequipos(equipos):
    return lall(
       
   
        # El equipo de Connie saldrá en algún momento después del equipo de Noel.
        somewhat_right_of(equipos, (var(), var(), 'Connie'), (var(), 'Noel', var())),
       
        # La expedición de Connie será la expedición de Horace o el equipo de Noel.
        lany( membero((var(), 'Horace', 'Connie'), equipos), membero((var(), 'Noel', 'Connie'), equipos) ),
       
        # La expedición que sale en febrero será la expedición de Kay o el equipo de Yolanda.
        lany( eq(('February', var(), 'Kay'), equipo2), eq(('February', var(), 'Yolanda'), equipo2) ),
       
        # El equipo de Darrell incluirá a Yolanda.
        membero((var(),'Darrell','Yolanda'), equipos),


        membero((var(), 'Darrell', var()), equipos),
        membero((var(), 'Horace', var()), equipos),
        membero((var(), 'Noel', var()), equipos),
        membero((var(), 'Zachary', var()), equipos),


        membero((var(), var(), 'Amelia'), equipos),
        membero((var(), var(), 'Connie'), equipos),
        membero((var(), var(), 'Kay'), equipos),
        membero((var(), var(), 'Yolanda'), equipos),


    )


start = perf_counter()
solution = run (0, equipos, problemaequipos(equipos),
                # Los cuatro equipos serán: la expedición de Zachary, la expedición de Amelia,
                # la expedición que sale en marzo y la expedición que sale en febrero.
                differents(equipos, (('March','February',), ('Zachary',), ('Amelia',))))
end = perf_counter()


print(solution)


execution_time = (end - start)
print(execution_time)