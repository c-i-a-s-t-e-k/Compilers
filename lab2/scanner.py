import sys
import ply.lex as lex

reserved = {
    'if'    : 'IF',
    'else'  : 'ELSE',
    'while' : 'WHILE',
    'for'  : 'FOR',
    'break' : 'BREAK',
    'continue': 'CONTINUE',
    'return': 'RETURN', 
    'eye': 'EYE', 
    'zeros': 'ZEROSA', 
    'ones': 'ONES', 
    'print': 'PRINT'
}

tokens = ('DOTADD', 'DOTSUB', 'DOTMUL', 'DOTDIV', 'ADDEQ', 'SUBEQ', 
          'MULEQ', 'DIVEQ', 'LOWEQ', 'HIGEQ', 'NOTEQ', 'EQ', 'NUMINT',
            'NUMFLOAT', 'ID', 'STR') + tuple(reserved.values())

t_DOTADD = r"\.\+"
t_DOTSUB = r"\.\-"
t_DOTMUL = r"\.\*"
t_DOTDIV = r"\.\/"
t_ADDEQ = r"\+="
t_SUBEQ = r"\-="
t_MULEQ = r"\*="
t_DIVEQ = r"\/="
t_LOWEQ = r"<="
t_HIGEQ = r">="
t_NOTEQ = r"!="
t_EQ = r"=="
 
literals = [ '+','-','*','/','(',')', '=', '\'', '<', '>', '[',']','{','}', ':', ',', ';']


def t_NUMINT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NUMFLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_]\w*'
    return t

def t_STR(t):
    r'\"*\"'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '%s'" %t.value[0])
    t.lexer.skip(1)

t_ignore = '  \t'

lexer = lex.lex()