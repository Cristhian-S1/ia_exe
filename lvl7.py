from kanren import eq,var,run,membero

right = (1,var())
left = (var(),2)
lista = [1,2,3,4,5]
trans = list(zip(lista,lista[3:]))

print(trans)
print( run(0,right,membero(right,trans)) )
