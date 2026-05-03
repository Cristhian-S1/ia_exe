# AGENTS.md — OpenCode Guidance

## Repo Structure

This repo contains **two separate projects**:

| Directory | Purpose |
|-----------|---------|
| `ORTools/pt1/` | OR-Tools CP-SAT tutorials (basic constraint programming) |
| `ORTools/more/` | Advanced puzzle solvers (sudoku, nonogram, rascacielos, etc.) |
| Root (`.py` files) | miniKanren logic programming examples (see `CLAUDE.md`) |

## ORTools — Running Code

```bash
cd ORTools/pt1
source .venv/bin/activate
python lvl1.py      # Basic example (x != y constraint)
python lvl3.py      # More complex example
```

**Dependencies** (already in `.venv/`):
- `ortools` 9.15.6755 — CP-SAT solver
- `numpy` 2.4.4, `pandas` 3.0.2 — data handling

## ORTools — Core Pattern

```python
from ortools.sat.python import cp_model

model = cp_model.CpModel()
x = model.new_int_var(0, 2, "x")      # Variables belong to their model
model.add(x != y)                      # Constraints accumulate in model
solver = cp_model.CpSolver()
status = solver.solve(model)
```

**Key constraint:** Variables cannot be mixed between different `CpModel` instances — they carry internal indices tied to their creator model.

## Puzzle Solvers (`ORTools/more/`)

Each file is a standalone solver:
- `sudoku.py` — uses `SearchForAllSolutions` with callback
- `nonogram.py`, `kakurasu.py`, `rascacielos.py` — logic puzzles
- `cripto0.py`, `cripto1.py` — cryptarithmetic
- `map0.py`, `map1.py` — map coloring
- `malaga.py`, `magic.py` — custom constraints

Run directly with the venv active:
```bash
python sudoku.py
```

## miniKanren (Root Level)

See `CLAUDE.md` for the logic programming examples (`main.py`, `simpsons.py`, `for.py`).

## Git

- Remote: `git@github.com:Cristhian-S1/IA.git`
- Branch: `main`
