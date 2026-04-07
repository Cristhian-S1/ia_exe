from kanren import run,var,eq,conde

def father(x,y):
    
    return conde(   [ eq( (x,y), ("Cristhian","Jimmy") ) ],
                    [ eq( (x,y), ("Samuel", "Jimmy")   ) ],
                    [ eq( (x,y), ("Jimmy", "Jesus")) ],
                    [ eq( (x,y), ("Jimmy", "Gloria") )]
                )

def grand_father(x,y):
    w = var()
    return conde ( [ father(x,w), father(w,y) ] )

x = var()
result = run(0,x,father("Samuel",x))
result_grand = run(0,x,grand_father("Cristhian",x))
print(result)
print(result_grand)