def implies(p, q):
    return (not p) or q


def iff(p, q):
    return (p and q) or (not p and not q)


propositions = {
    'A': True,
    'B': False,
    'C': True
}


def evaluate_expressions():
    print("\n--- Propositional Logic Evaluation ---")

    result1 = propositions['A'] and not propositions['C']
    print("A ∧ ¬C =", result1)

    result2 = (propositions['A'] or propositions['B']) and propositions['C']
    print("(A ∨ B) ∧ C =", result2)

    result3 = not propositions['B'] or propositions['A']
    print("¬B ∨ A =", result3)

    result4 = implies(propositions['A'], propositions['C'])
    print("A → C =", result4)

    result5 = iff(propositions['B'], propositions['C'])
    print("B ↔ C =", result5)


# Run the program
evaluate_expressions()
