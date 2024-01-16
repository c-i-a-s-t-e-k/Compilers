import ply.lex as lex
import sys

reserved = {
    "if": "IF",
    "else": "ELSE",
    "for": "FOR",
    "while": "WHILE",
    "break": "BREAK",
    "continue": "CONTINUE",
    "return": "RETURN",
    "eye": "EYE",
    "zeros": "ZEROS",
    "ones": "ONES",
    "print": "PRINT",
}

tokens = (
    "ADD",
    "MINUS",
    "MUL",
    "DIVIDE",
    "DOTADD",
    "DOTSUB",
    "DOTMUL",
    "DOTDIVIDE",
    "ADDASSIGN",
    "SUBASSIGN",
    "MULASSIGN",
    "DIVASSIGN",
    "GREATER",
    "LESS",
    "GREATEREQ",
    "LESSEQ",
    "NOTEQ",
    "EQ",
    "FLOAT",
    "INTNUM",
    "STRING",
    "ID",
) + tuple(reserved.values())

t_ADD = r"\+"
t_MINUS = r"-"
t_MUL = r"\*"
t_DIVIDE = r"/"
t_DOTADD = r"\.\+"
t_DOTSUB = r"\.\-"
t_DOTMUL = r"\.\*"
t_DOTDIVIDE = r"\./"
t_ADDASSIGN = r"\+="
t_SUBASSIGN = r"-="
t_MULASSIGN = r"\*="
t_DIVASSIGN = r"/="
t_GREATER = r">"
t_LESS = r"<"
t_GREATEREQ = r">="
t_LESSEQ = r"<="
t_NOTEQ = r"!="
t_EQ = r"=="

literals = ["+", "-", "*", "/", "(", ")", ";", "=", "'", ",", "[", "]", "{", "}", ":"]

def t_FLOAT(t):
    r"[0-9]+\.[0-9]+|[0-9]+[eE][-+]?[0-9]+|[0-9]+\.[0-9]+[eE][-+]?[0-9]+"
    t.value = float(t.value)
    return t


def t_INTNUM(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_ID(t):
    r"[a-zA-Z_][\w_]*"
    t.type = reserved.get(t.value, "ID")  # Check for reserved words
    return t


def t_STRING(t):
    r"\"[^\"\n]*\""
    t.type = reserved.get(t.value, "STRING")
    return t


t_ignore = " \t"


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"\t|Line|: {t.lexer.lineno}\n\t|Illegal character|: '{t.value[0]}'")
    t.lexer.skip(1)


def t_COMMENT(t):
    r"\#.*"
    pass

lexer = lex.lex()
def get_lexer():
    return lexer

if __name__ == "__main__":
    lexer = lex.lex()
    fh = open(sys.argv[1], "r")
    lexer.input(fh.read())
    for token in lexer:
        print(f"(%d): %s(%s)" % (token.lineno, token.type, token.value))
