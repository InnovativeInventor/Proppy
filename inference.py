class MP:
    """
    Provides inference rules for Modus Ponens (MP).
    """
    def __init__(self, current_line, remaining_line, dest=None):
        self.current_line = current_line
        self.remaining_line = remaining_line
        if dest:
            self.dest = dest

    def solve(self, dest):
        """
        Attempts to get to the destination from the current line
        """
        if dest:
            self.dest = dest
        for each_statement in current_line:
            if type(each_statement) == proposition.Conditional:



class MT:
    def __init__(self, current_line, remaining_line, dest=None):
        self.current_line = current_line
        self.remaining_line = remaining_line


class MTP:
    def __init__(self, current_line, remaining_line, dest=None):
        self.current_line = current_line
        self.remaining_line = remaining_line


class MTP:
    def __init__(self, current_line, remaining_line, dest=None):
        self.current_line = current_line
        self.remaining_line = remaining_line


class ADJ:
    def __init__(self, current_line, remaining_line, dest=None):
        self.current_line = current_line
        self.remaining_line = remaining_line


class ADD:
    def __init__(self, current_line, remaining_line, dest=None):
        self.current_line = current_line
        self.remaining_line = remaining_line


class SEP:
    def __init__(self, current_line, remaining_line, dest=None):
        self.current_line = current_line
        self.remaining_line = remaining_line
