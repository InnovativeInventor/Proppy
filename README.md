## Proppy 
Proppy is a propositional logic proving assistant. It can check the validity of statements, form wffs,

Note: I'm trying out README-driven development. This is still a WIP.

## Structure

`proposition.py` contains all the truth-functional connectives. You should be able to represent all first order logic problems with everything contained in `proposition.py`. I could have used fancy metaclasses to shorten the code in proposition.py, but I felt that it would decrease the readability of my code (otherwise why the hell am I writing this in Python).

`tree-solver` contains the tree-searching algo that determines the validity of a given argument

`inference.py` contains all the inference rules

`test_*` contains all the test cases (TDD is awesome)
