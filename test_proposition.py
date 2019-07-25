import proposition

# Tree solver testing


def p_and_not_p():
    pass


def p_or_not_p():
    pass


# Basic Truth testing (conditional)
def test_true_then_true():
    p = proposition.Statement(state=True)
    q = proposition.Statement(state=True)

    conditional_connective = proposition.Conditional(p, q)
    assert conditional_connective.truth()


def test_false_then_false():
    p = proposition.Statement(state=False)
    q = proposition.Statement(state=False)

    conditional_connective = proposition.Conditional(p, q)
    assert conditional_connective.truth()


def test_false_then_true():
    p = proposition.Statement(state=False)
    q = proposition.Statement(state=True)

    conditional_connective = proposition.Conditional(p, q)
    assert conditional_connective.truth()


def test_true_then_false():
    p = proposition.Statement(state=True)
    q = proposition.Statement(state=False)

    conditional_connective = proposition.Conditional(p, q)
    assert not conditional_connective.truth()


# Equality testing (conditional)
def test_false_then_true_eq_false_then_false():
    p = proposition.Statement(state=False)
    q = proposition.Statement(state=True)

    conditional_connective_p = proposition.Conditional(p, q)

    p = proposition.Statement(state=False)
    q = proposition.Statement(state=False)

    conditional_connective_q = proposition.Conditional(p, q)
    assert conditional_connective_p == conditional_connective_q
    assert conditional_connective_p == conditional_connective_p
    assert conditional_connective_q == conditional_connective_p
    assert conditional_connective_q == conditional_connective_q
    assert bool(conditional_connective_p)
    assert bool(conditional_connective_q)


def test_eq():
    p = proposition.Statement(state=True)
    q = proposition.Statement(state=False)

    conditional_connective_p = proposition.Conditional(p, q)
    conditional_connective_q = proposition.Conditional(p, q)
    assert conditional_connective_p == conditional_connective_q
    assert conditional_connective_p == conditional_connective_p
    assert conditional_connective_q == conditional_connective_p
    assert conditional_connective_q == conditional_connective_q
    assert not bool(conditional_connective_p)
    assert not bool(conditional_connective_q)
    assert not conditional_connective_p.truth()
    assert not conditional_connective_q.truth()


# Basic Truth testing (and)
def test_false_and_true():
    p = proposition.Statement(state=False)
    q = proposition.Statement(state=True)

    and_connective = proposition.And(p, q)
    assert not and_connective.truth()


def test_false_and_true_alt():
    p = proposition.Statement()
    p.false()

    q = proposition.Statement()
    q.true()

    and_connective = proposition.And(p, q)
    assert not and_connective.truth()


def test_true_and_false():
    p = proposition.Statement(state=True)
    q = proposition.Statement(state=False)

    and_connective = proposition.And(p, q)
    assert not and_connective.truth()


def test_true_and_true():
    p = proposition.Statement(state=True)
    q = proposition.Statement(state=True)

    and_connective = proposition.And(p, q)
    assert and_connective.truth()
