#!/usr/bin/python

import scanner
import ply.yacc as yacc


tokens = scanner.tokens

# 1 - name error
# 2 - variable is not a matrix
# 3 - matrix diffrent size

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


def p_error(p):
    global error_code
    match error_code:
        case 1: print("name error")
        case 2: print("variable is not a matrix error")
        case 3: print("matrix diffrent size error")
        case other: print("Something wrong :D")

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
    global error_code
    
    if p[2] == "[" and p[4] == ',' and p[6] == ']':
        tmp = check_existance_matrix(p[1])
        if tmp == 0:
            names[p[1]][p[3]][p[5]] = p[8]
        else:
            p_error(p)        
    elif p[2] == '=':
        names[p[1]] = p[3]
    elif p[1] in names:
        match p[2]:
            case '+=': names[p[1]] += p[3]
            case '-=': names[p[1]] += p[3]
            case '*=': names[p[1]] *= p[3]
            case '\=': names[p[1]] /= p[3]
    else:
        error_code = 1
        p_error(p)

def p_expression_binop(p):
    """expression : expression ADD expression
                  | expression MINUS expression
                  | expression MUL expression
                  | expression DIVIDE expression"""
    if p[2] == '+'  : p[0] = p[1] + p[3]
    elif p[2] == '-': p[0] = p[1] - p[3]
    elif p[2] == '*': p[0] = p[1] * p[3]
    elif p[2] == '/': p[0] = p[1] / p[3]

def p_expressions_unaryneg(p):
    '''expression : MINUS expression'''
    if (len(p) == 3):
        if (type(p[2]) == list):
            len_tab = len(p[2])
            p[0] = [[-p[2][i][j] for i in range(len_tab)] for j in range(len_tab)]
        else:
            p[0] = -p[2]

def p_expressions_transpose(p):
    '''expression : expression "\'" '''
    if (len(p) == 3):
        len_tab = len(p[1])
        p[0] = [[p[1][j][i] for i in range(len_tab)] for j in range(len_tab)]

def p_expression_matroxop(p):
    """expression : expression DOTADD expression
                  | expression DOTSUB expression
                  | expression DOTMUL expression
                  | expression DOTDIVIDE expression"""
    global error_code
    if len(p[1]) != len(p[3]):
        error_code = 3
        p_error(p)

    m_len = len(p[1])
    tmp_tab = [[0 for _ in range(m_len)] for _ in range(m_len)]

    if p[2] == '.+':
        for i in range(m_len):
            tmp_tab = p[1][i] + p[3][i]
        p[0] = tmp_tab
            
    elif p[2] == '.-':
        for i in range(m_len):
            tmp_tab = p[1][i] - p[3][i]
        p[0] = tmp_tab

    elif p[2] == '.*':
        for i in range(m_len):
            tmp_tab = p[1][i] * p[3][i]
        p[0] = tmp_tab

    elif p[2] == './':
        for i in range(m_len):
            tmp_tab = p[1][i] / p[3][i]
        p[0] = tmp_tab

def p_expression_number(p):
    """expression : INTNUM
                  | FLOAT
                  | matrix_expression
                  | matrix_create"""
    p[0] = p[1]

def p_expression_id(p):
    """expression : ID"""
    global error_code
    if p[1] in names:
        p[0] = names[p[1]]
    else:
        error_code = 1
        p_error(p)

def p_matrix_expression(p):
    """matrix_expression : ZEROS '(' expression ')'
                         | ONES '(' expression ')'
                         | EYE '(' expression ')'"""
    if p[1] == "zeros":
        p[0] = [[0 for _ in range(p[3])] for _ in range(p[3])]
    elif p[1] == "ones":
        p[0] = [[1 for _ in range(p[3])] for _ in range(p[3])]
    elif p[1] == "eye":
        p[0] = [[1 if i == j else 0 for i in range(p[3]) ] for j in range(p[3])]

def p_matrix_create(p):
    """matrix_create : '[' matrix_rows ']'"""
    p[2] = p[2][::-1]
    p[0] = [p[2][i][::-1] for i in range(len(p[2]))]

def p_matrix_rows(p):
    """matrix_rows : matrix_rows ',' matrix_rows
                   | '[' matrix_elems ']'"""
    tab = []
    if p[1] == "[":
        tab.append(p[2])
    else:
        tab.extend(p[3])
        tab.extend(p[1])

    p[0] = tab

def p_matrix_elems(p):
    """matrix_elems : matrix_elems ',' matrix_elems
                   | expression"""
    tab = []
    if len(p) < 3:
        tab.append(p[1])
    else:
        tab.extend(p[3])
        tab.extend(p[1])
    p[0] = tab

def p_condition(p):
    """expression : condition"""
    p[0] = p[1]

def p_condition_operations(p):
    """condition : expression EQ expression
                  | expression NOTEQ expression
                  | expression GREATER expression
                  | expression GREATEREQ expression
                  | expression LESS expression
                  | expression LESSEQ expression"""
    if p[2] == '==':
        p[0] = p[1] == p[3]      
    elif p[2] == '!=':
        p[0] = p[1] != p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '>=':
        p[0] = p[1] >= p[3]
    elif p[2] == '<=':
        p[0] = p[1] <= p[3]

def p_instruction_if_else(p):
    """instruction : IF '(' condition ')' expression
                  | IF '(' condition ')' expression ELSE expression"""
    global error_code
    
    if len(p) == 6:
        print("in if")
        if p[3]:
            p[0] = p[5]
    elif len(p) == 8:
        print("in if else")
        if p[3]:
            p[0] = p[5]
        else:
            p[0] = p[7]
    else:
        error_code = 1
        p_error(p)
    
parser = yacc.yacc()