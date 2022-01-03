# logic_eval
import math


class LogicEval:

    # Dispatch Table (Design Pattern)
    operators = {
        "ou": lambda args: args[0] or args[1],
        "∨": lambda args: args[0] or args[1],
        "e": lambda args: args[0] and args[1],
        "∧": lambda args: args[0] and args[1],
        "nao": lambda a: not a[0],
        "+": lambda args: args[0] + args[1],
        "-": lambda args: args[0] - args[1],
        "*": lambda args: args[0] * args[1],
        "/": lambda args: args[0] / args[1],
        "t": lambda args: args[0] ** args[1],
        "cos": lambda args:  math.cos(args[0]),
        "sen()": lambda args:  math.sin(args[0]),


        "atribui": lambda a: LogicEval._assign(*a),
        "escreva": lambda a: print(*a),
        "leia": lambda a: input(*a),
        "for": lambda args: LogicEval._for(*args)
    }
    # Symbol Table (Tabela de Símbolos)
    symbols = {}

    @staticmethod
    def _for(var, lower, higher, code):
        inc, comp = (1, lambda a, b: a <= b) \
            if lower < higher else (-1, lambda a, b: a >= b)
        value = lower
        LogicEval._assign(var, value)
        while comp(value, higher):
            LogicEval.eval(code)
            value += inc
            LogicEval._assign(var, value)

    @staticmethod
    def _assign(var, value):
        LogicEval.symbols[var] = value

    @staticmethod
    def eval(ast):
        if type(ast) in (float, bool, str):
            return ast
        if type(ast) is dict:
            return LogicEval._eval_dict(ast)
        if type(ast) is list:
            ans = None
            for c in ast:
                ans = LogicEval._eval_dict(c)
            return ans
        raise Exception(f"Eval called with weird type: {type(ast)}")

    @staticmethod
    def _eval_dict(ast):
        if "op" in ast:
            op = ast["op"]
            # args = [LogicEval.eval(x) for x in ast["args"]]
            args = list(map(LogicEval.eval, ast["args"]))
            if "data" in ast:
                args += ast["data"]

            if op in LogicEval.operators:
                func = LogicEval.operators[op]
                return func(args)
            else:
                raise Exception(f"Unknown operator: {op}")
        elif "var" in ast:
            if ast["var"] in LogicEval.symbols:
                return LogicEval.symbols[ast["var"]]
            raise Exception(f"Unknown variable {ast['var']}")
        else:
            raise Exception("Weird dict on eval")

