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


#konstanta
class Const(Formula):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def interpret(self, valuation):
        return self.value


#logicke operacije
class And(Formula):
    def __init__(self, lhs, rhs):
        super().__init__()
        self.components = [lhs, rhs]

    def interpret(self, valuation):
        return self.components[0].interpret(valuation) and self.components[1].interpret(valuation)


class Or(Formula):
    def __init__(self, lhs, rhs):
        super().__init__()
        self.components = [lhs, rhs]


class Impl(Formula):
    def __init__(self, lhs, rhs):
        super().__init__()
        self.components = [lhs, rhs]


class Eq(Formula):
    def __init__(self, lhs, rhs):
        super().__init__()
        self.components = [lhs, rhs]


class Not(Formula):
    def __init__(self, op):
        super().__init__()
        self.components = [op]


def vars(names):
    return [Var(name.strip()) for name in names.split(",")]

def main():
    x, y, z = vars("x, y, z")
    formula = And(x, y)
    valuation = {
        "x": True,
        "y": False,
    }
    print(formula.interpret(valuation))

if __name__ == "__main__":
    main()
