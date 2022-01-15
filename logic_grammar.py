

# logic_grammar.py
import ply.yacc as pyacc
from pprint import PrettyPrinter

from logic_lexer import LogicLexer
from logic_eval import LogicEval


class LogicGrammar:
    precedence = (
        ("left", "ou"),
        ("left", "e"),
        ("left", "<", ">"),
        ("left", "+", "-"),
        ("left", "*", "/", "cos")
    )

    def p_error(self, p):
        if p:
            raise Exception(f"Parse Error: Unexpected token '{p.type}'")
        else:
            raise Exception("Parse Error: Expecting token")

    def p_axioma0(self, p):
        """ axioma : Inicio code Fim"""
        p[0] = p[2]

    def p_code0(self, p):
        """ code : S """
        p[0] = [p[1]]

    def p_code1(self, p):
        """code : code ';' S """
        p[0] = p[1]
        p[0].append(p[3])

    def p_s(self, p):
        """S : C"""
        p[0] = p[1]

    def p_condicao(self, p):
        """ condicao : se E entao c_list senao c_list fim_se """
        p[0] = {
            "op": "se",
            "args": [p[2]],
            "data": [p[4], p[6]]
        }

    def p_c0(self, p):
        """ C : E
              | condicao """
        p[0] = p[1]

    def p_c1(self, p):
        """C : escreva '(' e_list ')' ';'"""
        p[0] = {'op': p[1], 'args': p[3]}

    def p_c2(self, p):
        """C : leia '(' var ')' ';'"""
        p[0] = {'op': 'attrib', 'args': [{'var': p[1]}, p[3]]}

    def p_c3(self, p):
        """ C : var atribui E ';' """
        p[0] = {"op": "atribui", "args": [p[1], p[3]]}

    def p_c4(self, p):
        """ C : para var de E ate E  '{' c_list '}' """
        p[0] = {
            "op": "para",
            "args": [p[2], p[4], p[6]],
            "data": [p[8]],
        }

    def p_e_list(self, p):
        """ e_list : E
                   | e_list ',' E """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[3]]

    def p_c_list(self, p):
        """ c_list : C
                     | c_list ';' C """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1]
            p[0].append(p[3])

    def p_n1(self, p):
        """N : nr """
        p[0] = p[1]

    def p_n2(self, p):
        """N : E '+' E
             | E '-' E
             | E '*' E
             | E '/' E
             | E '<' E
             | E '>' E"""
        p[0] = {"op": p[2], "args": [p[1], p[3]]}

    def p_n3(self, p):
        """N : cos '(' E ')'"""
        p[0] = {"op": p[1], "args": [p[3]]}

    def p_n4(self, p):
        """N : sen '(' E ')'"""
        p[0] = {"op": p[1], "args": [p[3]]}

    def p_b0(self, p):
        """B : F"""
        p[0] = p[1]

    def p_b1(self, p):
        """B : E e E
             | E ou E"""
        p[0] = {"op": p[2], "args": [p[1], p[3]]}

    def p_f1(self, p):
        """ F : verdadeiro """
        p[0] = True

    def p_f2(self, p):
        """ F : falso """
        p[0] = False

    def p_f3(self, p):
        """ F : nao F
              | nao var"""
        p[0] = {"op": "nao", "args": [p[2]]}

    def p_e1(self, p):
        """  E : var """
        p[0] = {'var': p[1]}

    def p_e2(self, p):
        """ E : '(' E ')' """
        p[0] = p[2]

    def p_e3(self, p):
        """ E : B
              | N
              | string """
        p[0] = p[1]

    def p_e4(self, p):
        """ E : var '(' e_list ')'
              | var '(' ')' """
        p[0] = {"op": "call",
                "args": [],
                "data": [p[1], [] if p[3] == ")" else p[3]]}


    def p_args(self, p):
        """ args :
                 | var_list """
        p[0] = p[1] if len(p) == 2 else []

    def p_var_list(self, p):
        """ var_list : var
                     | var_list ',' var """
        if len(p) == 2:
            p[0] = [{'var': p[1]}]
        else:
            p[0] = p[1]
            p[0].append({'var': p[3]})

    def p_arg_list(self, p):
        """ arg_list : E
                     | arg_list ',' E """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1]
            p[0].append(p[3])


    def __init__(self):
        self.lexer = LogicLexer()
        self.tokens = self.lexer.tokens
        self.yacc = pyacc.yacc(module=self)

    def parse(self, expression):
        ans = self.yacc.parse(lexer=self.lexer.lex, input=expression)
        pp = PrettyPrinter()
        pp.pprint(ans)  # debug rulez!
        return LogicEval.eval(ans)

