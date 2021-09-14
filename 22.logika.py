import copy
from itertools import combinations

def all_valuations(variables):
    for r in range(len(variables)+1):
        for true_variables in combinations(variables, r):
            result = {x: False for x in variables}
            result.update({x: True for x in true_variables})
            yield result

#formula
class Formula:
    def __init__(self):
        self.components = []

    def interpret(self, valuation):
        pass

    def __and__(self, rhs):
        return And(self.copy(), rhs.copy())

    def __or__(self, rhs):
        return Or(self.copy(), rhs.copy())

    def __rshift__(self, rhs):
        return Impl(self.copy(), rhs.copy())

    def __eq__(self, rhs):
        return Eq(self.copy(), rhs.copy())

    def __invert__(self):
        return Not(self.copy())

    def copy(self):
        return copy.deepcopy(self)

    #tautologija
    def is_valid(self):
        variables = list(self.get_all_variables())
        for valuation in all_valuations(variables):
            if self.interpret(valuation) == False:
                return False, valuation
        return True, None

    def get_all_variables(self):
        result = set()
        for c in self.components:
            result.update(c.get_all_variables())
        return result

    #zadovoljiva
    def is_satisfiable(self):
        variables = list(self.get_all_variables())
        for valuation in all_valuations(variables):
            if self.interpret(valuation) == True:
                return True, valuation
        return False, None 

    #kontradikcija
    def is_contradictory(self):
        variables = list(self.get_all_variables())
        for valuation in all_valuations(variables):
            if self.interpret(valuation) == True:
                return False, valuation
        return True, None 

    #poreciva
    def is_falsifiable(self):
        variables = list(self.get_all_variables())
        for valuation in all_valuations(variables):
            if self.interpret(valuation) == False:
                return True, valuation
        return False, None 


    def all_true_valuations(self):
        result = []
        variables = list(self.get_all_variables())
        for valuation in all_valuations(variables):
            if self.interpret(valuation) == True:
                result.append(valuation)
        return result


#promenljiva
class Var(Formula):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def interpret(self, valuation):
        return valuation[self.name]

    def __str__(self):
        return self.name 

    def get_all_variables(self):
        return set([self.name])


#konstanta
class Const(Formula):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def interpret(self, valuation):
        return self.value

    def __str__(self):
        return "{}".format(1 if self.value else 0)


#logicke operacije
class And(Formula):
    def __init__(self, lhs, rhs):
        super().__init__()
        self.components = [lhs, rhs]

    def interpret(self, valuation):
        return self.components[0].interpret(valuation) and self.components[1].interpret(valuation)

    def __str__(self):
        return f"({self.components[0]}) & ({self.components[1]})"


class Or(Formula):
    def __init__(self, lhs, rhs):
        super().__init__()
        self.components = [lhs, rhs]

    def interpret(self, valuation):
        return self.components[0].interpret(valuation) or self.components[1].interpret(valuation)

    def __str__(self):
        return f"({self.components[0]}) | ({self.components[1]})"


class Impl(Formula):
    def __init__(self, lhs, rhs):
        super().__init__()
        self.components = [lhs, rhs]

    def interpret(self, valuation):
        return not self.components[0].interpret(valuation) or self.components[1].interpret(valuation)

    def __str__(self):
        return f"({self.components[0]}) >> ({self.components[1]})"


class Eq(Formula):
    def __init__(self, lhs, rhs):
        super().__init__()
        self.components = [lhs, rhs]

    def interpret(self, valuation):
        return self.components[0].interpret(valuation) == self.components[1].interpret(valuation)

    def __str__(self):
        return f"({self.components[0]}) == ({self.components[1]})"


class Not(Formula):
    def __init__(self, op):
        super().__init__()
        self.components = [op]

    def interpret(self, valuation):
        return not self.components[0].interpret(valuation)

    def __str__(self):
        return f"~({self.components[0]})"


def vars(names):
    return [Var(name.strip()) for name in names.split(",")]

def main():
    '''
    U igri mines dimenzija 2x3 dobijena je sledeca konfiguracija
    |1|A|C|
    |1|B|2|
    A,B,C su neotvorena polja, a brojevi oznacavaju broj mina u okolnim poljima.
    Zapisati u iskaznoj logici uslove koji moraju da vaze.
    '''
    A, B, C = vars("A, B, C") 
    formula = (A | B) & ~(A & B) \
        & (B | A) & ~(B & A) \
        & ~(~A & ~B & ~C) \
        & (A | B) \
        & (B | C) \
        & (A | C) \
        & ~(A & B & C)

    #A, B, C, D = vars("A, B, C, D")
    #formula = (A >> (~B | ~C | ~D)) & (~D >> ((A & B) | (B & C) | (A & C)))
    print("is_valid: ", formula.is_valid())
    print("is_satisfiable: ", formula.is_satisfiable())
    print("is_falsifiable: ", formula.is_falsifiable())
    print("is_contradictory: ", formula.is_contradictory())

    print("Sva resenja: ")
    for resenje in formula.all_true_valuations():
        print(resenje)

if __name__ == "__main__":
    main()
