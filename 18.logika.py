#formula
class Formula:
    def __init__(self):
        self.components = []

    def interpret(self, valuation):
        pass


#promenljiva
class Var(Formula):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def interpret(self, valuation):
        return valuation[self.name]

    def __str__(self):
        return self.name 


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
    x, y, z = vars("x, y, z")
    #formula = (x & y) | (z >> y)
    formula = Or(And(x, y), Impl(z, y))
    valuation = {
        "x": True,
        "y": False,
        "z": True
    }
    print(formula)
    print(formula.interpret(valuation))

if __name__ == "__main__":
    main()
