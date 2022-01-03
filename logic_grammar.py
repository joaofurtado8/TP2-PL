# logic_grammar.py
import ply.yacc as pyacc
from pprint import PrettyPrinter

from logic_lexer import LogicLexer
from logic_eval import LogicEval


class LogicGrammar:
    precedence = (
        ("left", "+", "-"),
        ("left", "*", "/"),
        ("right", "uminus"),
        ("left", "ou"),   # menor prioridade
        ("left", "e"),
    )

    def p_error(self, p):
        if p:
            raise Exception(f"Parse Error: Unexpected token '{p.type}'")
        else:
            raise Exception("Parse Error: Expecting token")

        #


    def p_code1(self, p):
        """ code : r """
        p[0] = [p[1]]

    def p_code2(self, p):
        """ code : code ';' r """

        p[0] = p[1] + [p[3]]  # concatenate!

    def p_ciclo(self, p):
        """ ciclo : for var '[' n ellipsis n ']' code ';' endfor """
        p[0] = {
            "op": "for",
            "args": [p[2], p[4], p[6]],
            "data": [p[8]],
        }



    def p_r1(self, p):
        """ r : a
              | ciclo """
        p[0] = p[1]

    def p_r2(self, p):
        """ r : var atribui a"""
        p[0] = {"op": "atribui", "args": [p[1], p[3]]}

    def p_r3(self, p):
        """r : escreva a_list"""
        p[0] = {"op": "escreva", "args": p[2]}

    #def p_r4(self, p):
        #"""r : leia a_list"""
        #p[0] = {"op": "leia", "args": p[2]}

    def p_a_list(self, p):
        """a_list : a
                  | a_list ',' a """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[3]]

    def p_n1(self, p):
        """ n : nr
              | '-' a  %prec uminus  """
        p[0] = p[1] if len(p) == 2 else {"op": "-", "args": [0.0, p[2]]}

    def p_n2(self, p):
        """ n : a '+' a
              | a '-' a
              | a '*' a
              | a '/' a
              | a 't' a"""
        p[0] = dict(op=p[2], args=[p[1], p[3]])

    def p_b1(self, p):
        """ b : f
              | a ou a
              | a e a """
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = dict(op=p[2], args=[p[1], p[3]])

    def p_f1(self, p):
        """ f : verdadeiro """
        p[0] = True

    def p_f2(self, p):
        """ f : falso """
        p[0] = False

    def p_f3(self, p):
        """ f : nao f """
        p[0] = dict(op="nao", args=[p[2]])

    def p_a1(self, p):
        """ a : var """
        p[0] = {'var': p[1]}

    def p_a2(self, p):
        """ a : '(' a ')' """
        p[0] = p[2]

    def p_a3(self, p):
        """ a : b
              | n
              | string """
        p[0] = p[1]

    def __init__(self):
        self.lexer = LogicLexer()
        self.tokens = self.lexer.tokens
        self.yacc = pyacc.yacc(module=self)

    def parse(self, expression):
        ans = self.yacc.parse(lexer=self.lexer.lex, input=expression)
        pp = PrettyPrinter()
        pp.pprint(ans)  # debug rulez!
        return LogicEval.eval(ans)




