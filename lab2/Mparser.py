
#!/usr/bin/python

import scanner
import ply.yacc as yacc


tokens = scanner.tokens

<<<<<<< HEAD
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
=======
precedence = (
   ("nonassoc", 'IFX'),
   ("nonassoc" , 'ELSE') ,
>>>>>>> master
   ("left", 'DOTADD', 'DOTSUB'),
   ("left", 'ADD', 'MINUS'),
<<<<<<< HEAD
   ("left", 'DIVIDE', 'MUL'),
   ("right", '\'')
   # to fill ...
)


# def p_error(p):
=======
   ("left", 'DOTMUL', 'DOTDIVIDE'),
   ("left", 'DIVIDE', 'MUL'),
   ("right", 'UMINUS')
)


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")

>>>>>>> master

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
    """instruction : assignment ';'
                   | if_stmt
                   | loops
                   | BREAK ';'
                   | CONTINUE ';'
                   | return_expr ';'
                   | PRINT create_stmt ';'
                   | '{' instructions '}'"""

def p_assignment(p):
<<<<<<< HEAD
    """assignment : ID '=' expression ';'
                  | ID ADDASSIGN expression ';'
                  | ID SUBASSIGN expression ';'
                  | ID MULASSIGN expression ';'
                  | ID DIVASSIGN expression ';'
                  | ID '[' expression ',' expression ']' '=' expression ';' """
=======
    """assignment : ID '=' expression
                  | ID ADDASSIGN expression
                  | ID SUBASSIGN expression
                  | ID MULASSIGN expression 
                  | ID DIVASSIGN expression
                  | ID '[' expression ',' expression ']' ADDASSIGN expression
                  | ID '[' expression ',' expression ']' SUBASSIGN expression
                  | ID '[' expression ',' expression ']' MULASSIGN expression
                  | ID '[' expression ',' expression ']' DIVASSIGN expression
                  | ID '[' expression ',' expression ']' '=' expression """
    
>>>>>>> master
    return p

def p_expression_binop(p):
    """expression : expression ADD expression
                  | expression MINUS expression
                  | expression MUL expression
                  | expression DIVIDE expression"""
    return p

def p_expressions_unaryneg(p):
<<<<<<< HEAD
    '''expression : MINUS expression'''
=======
    '''expression : MINUS expression %prec UMINUS'''
>>>>>>> master
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
    """matrix_rows : '[' matrix_elems ']' ',' matrix_rows
                   | '[' matrix_elems ']'"""
    return p

def p_matrix_elems(p):
    """matrix_elems : expression ',' matrix_elems
                   | expression"""
    return p
<<<<<<< HEAD
=======
def p_condition(p):
    """condition : expression GREATER expression
                 | expression LESS expression
                 | expression GREATEREQ expression
                 | expression LESSEQ expression
                 | expression NOTEQ expression
                 | expression EQ expression"""
    
    return p
def p_if_stmt(p):
    """if_stmt : IF '(' condition ')' instruction %prec IFX
               | IF '(' condition ')' instruction ELSE instruction
               """
    return p

def p_create_stmt(p):
    """create_stmt : p_print_list"""
    return p

def p_print_list(p):
    """p_print_list : STRING
                  | p_print_list ',' expression
                  | expression"""
    return p

def p_loops(p):
    """loops : while_l
             | for_l"""
    return p

def p_while_l(p):
    """while_l : WHILE "(" condition ")" instruction"""
    return p

def p_for_l(p):
    """for_l : FOR ID "=" expression ":" expression instruction"""
    return p

def p_return_expr(p):
    """return_expr : RETURN
                   | RETURN expression"""
    return p
>>>>>>> master

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