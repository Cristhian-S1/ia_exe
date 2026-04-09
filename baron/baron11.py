from kanren import *
from logicpuzzles import *

pronostico1 = (50, var(), var())
pronostico2 = (55, var(), var())
pronostico3 = (60, var(), var())
pronostico4 = (65, var(), var())
pronosticos = (pronostico1,pronostico2,pronostico3,pronostico4)

def restricciones(pronosticos):
    return lall(
        #1. Las cuatro previsiones eran la previsión con vientos de 20 mph, la previsión de lluvias intensas, la previsión de niebla y la previsión de tormentas eléctricas.
        # Lo resuelve differents

        #2. El pronóstico con vientos de 35 mph es 5 grados más cálido que el pronóstico con vientos de 20 mph.
        right_of(pronosticos, (var(),var(),35),(var(),var(),20)),

        #3. El pronóstico de tormenta eléctrica es 5 grados más frío que el pronóstico con vientos de 20 mph.
        left_of(pronosticos, (var(),"thunderstorm", var()),(var(),var(),20)),

        # 4. El pronóstico de 65 °F era o bien el pronóstico de tormenta eléctrica o bien el pronóstico con vientos de 25 mph.
        lany(
            eq( pronostico4[1], "thunderstorm" ),
            eq( pronostico4[2], 25 )
        ), neq(pronostico4, (65, "thunderstorm", 25)),

        #5. El pronóstico de lluvia intensa tiene una temperatura de 65 °F.
        eq( pronostico4[1], "heavy_rain" ),

        #Dominios faltantes
        membero( (var(),var(),10), pronosticos ),
        membero( (var(),var(),25), pronosticos ),

        membero( (var(),"foggy",var()), pronosticos ),
        membero( (var(),"drizzly",var()), pronosticos ),
        membero( (var(),"heavy_rain",var()), pronosticos ),
        membero( (var(),"thunderstorm",var()), pronosticos )
    )

resultados = run(0, pronosticos, restricciones(pronosticos), 
                 differents(pronosticos, [[20], ["heavy_rain"], ["thunderstorm","foggy"]])
                 )

for resultado in resultados:
    print(resultado)
