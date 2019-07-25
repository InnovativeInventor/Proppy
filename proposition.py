"""
TODO: Reuse inits?
"""


class Argument:
    def __init__(self, premise, conclusion, validity=None):
        assert type(premises) == Statement
        assert type(conclusion) == Statement
        self.premise = premise
        self.conclusion = conclusion
        if not validity:
            self.valid = False
            self.proof = False

    def valid(self, proof=None, tree=None):
        """
        Marks the argument as valid
        """
        if proof:
            # assert type(proof)
            self.proof = proof
        if tree:
            # assert type(tree)
            self.tree = tree


class Statement:
    def __init__(self, state=[]):
        self.size = 2
        self.possible_states = [True, False]
        if isinstance(state, bool):
            self.size = 1
            self.state = state

    def __eq__(self, other):
        if self == other:
            return True
        elif len(self.possible_states) == 1 and len(
                other.possible_states
        ) == 1 and self.possible_states == other.possible_states:
            return True
        else:
            return False

    def __bool__(self):
        return self.truth()

    def true(self):
        self.state = True
        self.size = 1

    def false(self):
        self.state = False
        self.size = 1

    def truth(self):
        if self.size == 1:
            return self.state
        else:
            raise NotImplementedError

    def solve(self):
        return None


class Not:
    def __init__(self, statement_p):
        """
        not statement_p
        English: not statement p
        Truth table:
            P | not P
            ––––––––––––
            T | F
            F | T
        """
        self.statement_p = statement_p

        if self.statement_p.size == 1:
            self.p = statement_p.state

        else:
            raise NotImplementedError

        self.p_truth = statement_p.truth()

    def __eq__(self, other):
        try:
            if self.truth() == other.truth():
                return True
        except:
            pass
        return False

    def __bool__(self):
        return self.truth()

    def solve(self):
        return None

    def truth(self):
        return not self.p


class Or:
    def __init__(self, statement_p, statement_q):
        """
        statement_p or statement_q
        English: statement_p or statement_q
        Truth table:
            P Q | P or Q
            ––––––––––––
            T T | T
            T F | T
            F T | T
            F F | F
        """
        self.statement_p = statement_p
        self.statement_q = statement_q

        if self.statement_p.size == 1 and self.statement_q.size == 1:
            self.p = statement_p.state
            self.q = statement_q.state

        else:
            raise NotImplementedError

        self.p_truth = statement_p.truth()
        self.q_truth = statement_q.truth()

    def __eq__(self, other):
        try:
            if self.truth() == other.truth():
                return True
        except:
            pass
        return False

    def __bool__(self):
        return self.truth()

    def truth(self):
        if self.p or self.q:
            return True
        else:
            return False

    def solve(self):
        """
        Returns the next elements in the tree
        Might need to move to inference.py with the other inference rules
        (although techincally not an infernce rule)
        """
        return_p = self.statement_p
        return_q = self.statement_q
        return [return_p, return_q]


class And:
    def __init__(self, statement_p, statement_q):
        """
        statement_p and statement_q
        English: statement_p and statement_q
        Truth table:
            P Q | P and Q
            ––––––––––––
            T T | T
            T F | F
            F T | F
            F F | F
        """
        self.statement_p = statement_p
        self.statement_q = statement_q

        if self.statement_p.size == 1 and self.statement_q.size == 1:
            self.p = statement_p.state
            self.q = statement_q.state

        else:
            raise NotImplementedError

        self.p_truth = statement_p.truth()
        self.q_truth = statement_q.truth()

    def __eq__(self, other):
        try:
            if self.truth() == other.truth():
                return True
        except:
            pass
        return False

    def __bool__(self):
        return self.truth()

    def truth(self):
        if self.p and self.q:
            return True
        else:
            return False


class Conditional:
    def __init__(self, statement_p, statement_q):
        """
        statement_p -> statement_q
        English: If statement_p, then statement_q
        Truth table:
            P Q | P -> Q
            ––––––––––––
            T T | T
            T F | F
            F T | T
            F F | T
        """
        self.statement_p = statement_p
        self.statement_q = statement_q

        if self.statement_p.size == 1 and self.statement_q.size == 1:
            self.p = statement_p.state
            self.q = statement_q.state

        else:
            raise NotImplementedError

        self.p_truth = statement_p.truth()
        self.q_truth = statement_q.truth()

    def __eq__(self, other):
        try:
            if self.truth() == other.truth():
                return True
        except:
            pass
        return False

    def __bool__(self):
        return self.truth()

    def truth(self):
        """
        returns the truth value (right now can only do it if the state of p and q are singular
        """
        if self.p and not self.q:
            return False
        else:
            return True

    def solve(self):
        """
        Returns the next elements in the tree
        Might need to move to inference.py with the other inference rules
        (although techincally not an infernce rule)
        """
        return_p = Not(self.statement_p)
        return_q = self.statement_q
        return [And(return_p, return_q)]
