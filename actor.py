symbols = {}

def resolve(x):
    if x and isinstance(x, Node):
        return x.execute()
    else:
        return x

class Node:

    def __init__(self, action=None, params=None):
        self.action = action
        self.params = params

    def execute(self):
        result = None

        if self.action == 'print':
            print(' '.join(str(resolve(x)) for x in list(self.params[1:])))
        elif self.action == 'assign':
            result = symbols[self.params[0]] = resolve(self.params[1])
        elif self.action == 'get':
            result = symbols.get(self.params[0], 0)
        elif self.action == 'func_assign':
            symbols[self.params[0]] = self.params[1]
        elif self.action == 'func':
            resolve(symbols[self.params[0]])
        elif self.action == 'loop':
            while True:
                if not resolve(*self.params[0].params):
                    break
                for stmt in self.params[1:]:
                    resolve(stmt)
        elif self.action == 'if':
            if resolve(self.params[0]):
                result = resolve(self.params[1])
        elif self.action == 'try':
            try:
                resolve(self.params[0])
            except:
                resolve(self.params[1])
        elif self.action == 'binop':
            result = {
                '+':  lambda a, b: a + b,
                '-':  lambda a, b: a - b,
                '*':  lambda a, b: a * b,
                '/':  lambda a, b: a / b,
                '^':  lambda a, b: a ** b,
                '>':  lambda a, b: (a > b),
                '>=': lambda a, b: (a >= b),
                '<':  lambda a, b: (a < b),
                '<=': lambda a, b: (a <= b),
                '==': lambda a, b: (a == b)
            }[self.params[1]](resolve(self.params[0]), resolve(self.params[2]))
        return result
