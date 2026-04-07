# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Environment

- Python 3.14.3 with a virtual environment at `.venv/`
- Activate before running any script: `source .venv/bin/activate`

## Running Scripts

```bash
python main.py        # Basic miniKanren example
python for.py         # List operations examples
python simpsons.py    # Family relationship modeling
python -i simpsons.py # Interactive mode to query the relations manually
```

## Dependencies

Managed via the `.venv/` virtual environment. Key packages:
- `kanren` (miniKanren 1.0.5) — core logic/relational programming library
- `cons`, `etuples`, `logical_unification` — supporting unification/constraint libraries

To install dependencies from scratch: `pip install miniKanren`

## Architecture

This is a **logic programming learning project** using miniKanren (a Python port of the Scheme miniKanren DSL).

**Core pattern** used across files:
- Facts are asserted with `facts(relation, (arg1, arg2), ...)` or `Relation()`
- Queries are run with `run(n, var, goal)` — returns up to `n` solutions for `var` satisfying `goal`
- Variables are declared with `var('name')` or `vars_('a', 'b', ...)`

**`simpsons.py`** is the main logic file. It models family relationships using:
- `parent(x, y)` — derived from `father`/`mother` relations
- `grandparent(x, y)` — composed parent calls
- `sibling(x, y)` — same parents, inequality constraint via `neq`
- `ancestor(x, y)` — recursive with `Zzz()` (lazy evaluation to avoid infinite recursion)

**`main.py`** shows the minimal pattern: a `human` fact + `mortal` rule + a single query.

**`for.py`** is standalone Python (no miniKanren) — list slicing, comprehensions, and enumeration.
