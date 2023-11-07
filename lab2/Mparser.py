#!/usr/bin/python

import scanner
import ply.yacc as yacc


tokens = scanner.tokens

# 1 - name error
# 2 - variable is not a matrix
# 3 - matrix diffrent size
# 4 - input error

error_code = 0

names = {}

def check_existance_matrix(name):
    if name in names:
        if isinstance(names[name], list):
            error_code = 0
            return error_code
        else:
            error_code = 2
            return error_code
    error_code = 1
    return error_code

precedence = (
   # to fill ...
   ("left", 'EQ', 'NOTEQ', 'LESS', 'GREATER', 'LESSEQ', 'GREATEREQ'),
   ("left", 'DOTADD', 'DOTSUB'),
   ("left", 'DOTMUL', 'DOTDIVIDE'),
   ("left", 'ADD', 'MINUS'),
   ("left", 'DIVIDE', 'MUL'),
   ("right", '\'')
   # to fill ...
)


# def p_error(p):

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

def p_instruction(p):
    """instruction : assignment """

def p_assignment(p):
    """assignment : ID '=' expression ';'
                  | ID ADDASSIGN expression ';'
                  | ID SUBASSIGN expression ';'
                  | ID MULASSIGN expression ';'
                  | ID DIVASSIGN expression ';'
                  | ID '[' expression ',' expression ']' '=' expression ';' """
    return p

def p_expression_binop(p):
    """expression : expression ADD expression
                  | expression MINUS expression
                  | expression MUL expression
                  | expression DIVIDE expression"""
    return p

def p_expressions_unaryneg(p):
    '''expression : MINUS expression'''
    return p

def p_expressions_transpose(p):
    '''expression : expression "\'" '''
    return p

def p_expression_matroxop(p):
    """expression : expression DOTADD expression
                  | expression DOTSUB expression
                  | expression DOTMUL expression
                  | expression DOTDIVIDE expression"""
    return p

def p_expression_number(p):
    """expression : INTNUM
                  | FLOAT
                  | matrix_expression
                  | matrix_create"""
    return p

def p_expression_id(p):
    """expression : ID"""
    return p

def p_matrix_expression(p):
    """matrix_expression : ZEROS '(' expression ')'
                         | ONES '(' expression ')'
                         | EYE '(' expression ')'"""
    return p

def p_matrix_create(p):
    """matrix_create : '[' matrix_rows ']'"""
    return p

def p_matrix_rows(p):
    """matrix_rows : matrix_rows ',' matrix_rows
                   | '[' matrix_elems ']'"""
    return p

def p_matrix_elems(p):
    """matrix_elems : matrix_elems ',' matrix_elems
                   | expression"""
    return p

def p_condition(p):
    """expression : condition"""
    return p

def p_condition_operations(p):
    """condition : expression EQ expression
                  | expression NOTEQ expression
                  | expression GREATER expression
                  | expression GREATEREQ expression
                  | expression LESS expression
                  | expression LESSEQ expression"""
    return p



def p_expression_if_else(p):
    """expression : IF '(' condition ')' expression
                  | IF '(' condition ')' expression ELSE expression"""
    return p
    
parser = yacc.yacc()