# logic_lexer.py
import ply.lex as plex


class LogicLexer:

    keywords = ()
    tokens = ("var", "atribui", "nr", "ellipsis", "string", "inteiro", "real", "caracter", "logico",
                "verdadeiro", "falso", "nao", "e", "ou", "escreva", "leia", "for", "endfor", "Inicio", "Fim", "cos")

    literals = ['(', ')', '+', '-', '/', '*', ';', '[', ']', '#', ':']
    t_ignore = " \t\n"

    def t_comment(self, t):
        r"""\#.*"""
        pass

    def t_ellipsis(self, t):
        r"""\.{3}"""
        return t

    def t_string(self, t):
        r'"[^"]*"'
        t.value = t.value[1:-1]
        return t

    def t_str(self, t):
        r"não|verdadeiro|falso|e(screva)?|ou|for|Inicio|Fim|cos|atribui"
        t.type = t.value
        return t

    def t_var(self, t):
        r"[a-z_]+"
        return t

    def t_nr(self, t):
        r"""[0-9]+(\.[0-9]+)?"""
        t.value = float(t.value)
        return t

    def t_atribui(self, t):
        r"""<-"""
        return t

    def t_error(self, t):
        raise Exception(f"Unexpected token {t.value[:10]}")

    def __init__(self):
        self.lex = plex.lex(module=self)

    def token(self):
        return self.lex.token()