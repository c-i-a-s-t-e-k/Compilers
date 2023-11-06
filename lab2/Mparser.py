#!/usr/bin/python

import scanner
import ply.yacc as yacc


tokens = scanner.tokens

precedence = (
   # to fill ...
   ("left", 'DOTADD', 'DOTSUB'),
   ("left", 'DOTMUL', 'DOTDIV'),
   ("left", '+', '-'),
   ("left", '+', '-'),

   ("left", '+', '-'),
   ("left", '*', '/'),
   ("left", '\'')
   # to fill ...
)


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")


def p_program(p):
    """program : instructions_opt"""

def p_instructions_opt_1(p):
    """instructions_opt : instructions """

def p_instructions_opt_2(p):
    """instructions_opt : """

def p_instructions_1(p):
    """instructions : instructions instruction """

def p_instructions_2(p):
    """instructions : instruction """

# to finish the grammar
# ....
def p_plus(p):
    p[0] = p[1] + p[2]

def p_error(p):
    print("Syntax error in input!")
    


parser = yacc.yacc()