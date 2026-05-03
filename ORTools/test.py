from ortools.sat.python import cp_model

"""value = array[index] donde index es variable"""
print("\n=== 8. AddElement() ===")
model = cp_model.CpModel()

# Array de valores
valores = [10, 20, 30, 40, 50]

# Variable índice (debe estar en rango válido)
index = model.NewIntVar(0, len(valores) - 1, 'index')
value = model.NewIntVar(0, 100, 'value')

# value = valores[index]
model.AddElement(index, valores, value)

# Forzar índice para demostración
model.Add(index == 2)

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL:
    print(f"valores = {valores}")
    print(f"index = {solver.Value(index)}")
    print(f"value = valores[index] = {solver.Value(value)}")
