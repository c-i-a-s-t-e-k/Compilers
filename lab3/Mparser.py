
#!/usr/bin/python

import AST
import scanner as sc
import ply.yacc as yacc

class Mparser:
    tokens = sc.tokens
    scanner = sc.get_lexer()
    precedence = (
        ("nonassoc", 'IFX'),
        ("nonassoc" , 'ELSE') ,
        ("left", 'DOTADD', 'DOTSUB'),
        ("left", 'ADD', 'MINUS'),
        ("left", 'DOTMUL', 'DOTDIVIDE'),
        ("left", 'DIVIDE', 'MUL'),
        ("right", 'UMINUS'),
        )
        
    def p_error(self, p):
        if p:
            print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
        else:
            print("Unexpected end of input")
        return p


    def p_program(self, p):
        """program : instructions_opt"""
        p[0] = AST.InstructionsBlankExpr(p[1])

    def p_instructions_opt_1(self, p):
        """instructions_opt : instructions """
        p[0] = AST.InstructionsExpr(p[1])

    def p_instructions_opt_2(self, p):
        """instructions_opt : """
        p[0] = AST.InstructionsExpr()

    def p_instructions_1(self, p):
        """instructions : instructions instruction """
        p[0] = p[1] + p[2]

    def p_instructions_2(self, p):
        """instructions : instruction """
        p[0] = p[1]

    def p_instruction(self, p):
        """instruction : assignment ';'
                    | if_stmt
                    | loops
                    | BREAK ';'
                    | CONTINUE ';'
                    | return_expr ';'"""
        p[0] = [p[1]]
    
    def p_instruction_2(self, p):
        """instruction : PRINT create_stmt ';'"""
        p[0] = p[2]

    def p_instruction_brackets(self, p):
        """instruction : '{' instructions '}'"""
        p[0] = p[2]


    def p_assignment(self, p):
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
        if p[2] == "[":
            p[0] = AST.AssignExpr(p[7], AST.Variable(AST.Id(p[1]), (p[3], p[5])), p[8])
        else:
            p[0] = AST.AssignExpr(p[2], AST.Id(p[1]), p[3])

    def p_expression_binop(self, p):
        """expression : expression ADD expression
                    | expression MINUS expression
                    | expression MUL expression
                    | expression DIVIDE expression"""
        p[0] = AST.BinExpr(p[2], p[1], p[3])

    def p_expressions_unaryneg(self, p):
        '''expression : MINUS expression %prec UMINUS'''
        p[0] = AST.Uminus(p[2])

    def p_expressions_transpose(self, p):
        '''expression : ID "\'"'''
        p[0] = AST.TransposeExpr(AST.Id(p[1]))

    def p_expression_matrixop(self, p):
        """expression : expression DOTADD expression
                    | expression DOTSUB expression
                    | expression DOTMUL expression
                    | expression DOTDIVIDE expression"""
        p[0] = AST.MatrixBinExpr(p[2], p[1], p[3])

    def p_expression_number(self, p):
        """expression : matrix_expression
                    | matrix_create"""
        p[0] = p[1]

    def p_intnum(self, p):
        """expression : INTNUM"""
        p[0] = AST.IntNum(p[1])

    def p_float(self, p):
        """expression : FLOAT"""
        p[0] = AST.FloatNum(p[1])  

    def p_expression_id(self, p):
        """expression : ID"""
        p[0] = AST.Id(p[1])

    def p_matrix_expression_z(self, p):
        """matrix_expression : ZEROS '(' expression ')' """
        p[0] = AST.Zeros(p[3])

    def p_matrix_expression_o(self, p):
        """matrix_expression : ONES '(' expression ')' """
        p[0] = AST.Ones(p[3])

    def p_matrix_expression_e(self, p):
        """matrix_expression : EYE '(' expression ')' """
        p[0] = AST.Eye(p[3])

    def p_matrix_create(self, p):
        """matrix_create : '[' matrix_rows ']'"""
        p[0] = AST.Matrix(p[2])

    def p_matrix_rows(self, p):
        """matrix_rows : '[' matrix_elems ']' ',' matrix_rows
                    | '[' matrix_elems ']'"""
        if len(p) > 4:
            p[0] = [p[2]] + p[5]
        else:
            p[0] = [p[2]]

    def p_matrix_elems(self, p):
        """matrix_elems : expression ',' matrix_elems
                    | expression"""
        if len(p) > 2:
            p[0] = [p[1]] + p[3]
        else:
            p[0] = [p[1]]

    def p_condition(self, p):
        """condition : expression GREATER expression
                    | expression LESS expression
                    | expression GREATEREQ expression
                    | expression LESSEQ expression
                    | expression NOTEQ expression
                    | expression EQ expression"""
        p[0] = AST.RelExpr(p[2], p[1], p[3])

    def p_if_stmt(self, p):
        """if_stmt : IF '(' condition ')' instruction %prec IFX
                | IF '(' condition ')' instruction ELSE instruction
                """
        if len(p) < 7:
            p[0] = AST.IfExpr(p[3], AST.InstructionsExpr(p[5]))
        else:
            p[0] = AST.IfExpr(p[3], AST.InstructionsExpr(p[5]), AST.InstructionsExpr(p[7]))

    def p_create_stmt(self, p):
        """create_stmt : p_print_list"""
        p[0] = [AST.PrintExpr(p[1])]

    def p_print_list_1(self, p):
        """p_print_list : STRING """
        p[0] = [AST.String(p[1])]

    def p_print_list_2(self, p):
        """p_print_list : p_print_list ',' expression
                    | expression"""
        if len(p) < 3:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[3]]


    def p_loops(self, p):
        """loops : while_l
                | for_l"""
        p[0] = p[1]

    def p_while_l(self, p):
        """while_l : WHILE "(" condition ")" instruction"""
        p[0] = AST.WhileExpr(p[3], AST.InstructionsExpr(p[5]))

    def p_for_l(self, p):
        """for_l : FOR ID "=" expression ":" expression instruction"""
        p[0] = AST.ForExpr(AST.Id(p[2]), p[4], p[6], AST.InstructionsExpr(p[7]))

    def p_return_expr(self, p):
        """return_expr : RETURN
                    | RETURN expression"""
        if len(p) < 3:
            p[0] = AST.RetrunExpr()
        else:
            p[0] = AST.RetrunExpr(p[2])
    # Mparser = yacc.yacc()