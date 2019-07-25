"""
Solve propositional logic problems through a tree search
"""


class Proof():
    """
    One way of implementing a tree search
    remaining_line is the stuff to process
    current_line is the stuff already processed/taken as true
    """

    def __init__(self, current_line, remaining_line):
        self.left_child = None
        self.right_child = None
        self.current_line = current_line
        self.remaining_line = remaining_line
        self.completed = None

    def union(self, list_1: list, list_2: list):
        """
        Unions lists by converting them to sets.
        """
        return list(union(set(list_1), set(list_2)))

    def new_node(self):
        self.left_child = Solver(self.current_line, self.remaining_line)
        self.left_child.calculate()

        self.right_child = Solver(self.current_line, self.remaining_line)
        self.left_child.calculate()

    def eliminate(self):
        if len(self.remaining_line) == 0:
            self.completed = True

    def calculate(self):
        """
        TODO: implement some efficient ordering solution
        """
        while len(self.remaining_line) > 0:
            self.solution = self.remaining_line.pop(0).solve()
            # Write tests for this
            self.remaining_line = [
                x for x in self.remaining_line and not self.solution
            ]
            self.current_line.append(self.solution)
        else:
            print("Satisfiyable!")  # lol spellcheck

    def check_contradict(self):
        pass
