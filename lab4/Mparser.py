
#!/usr/bin/python
import sys
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

        
    def p_program(self, p):
        """program : instructions_opt"""
        p[0] = AST.InstructionsBlankExpr(p[1], lineno=p.lineno(1))

    def p_instructions_opt_1(self, p):
        """instructions_opt : instructions """
        p[0] = AST.InstructionsExpr(p[1], lineno=p.lineno(1))

    def p_instructions_opt_2(self, p):
        """instructions_opt : """
        p[0] = AST.InstructionsBlankExpr(lineno=p.lineno(0))

    def p_instructions_1(self, p):
        """instructions : instructions instruction """
        p[0] = p[1] + p[2]

    def p_instructions_2(self, p):
        """instructions : instruction """
        p[0] = p[1]

    def p_instruction(self, p):
        """instruction : assignment 
                    | if_stmt
                    | loops
                    | break
                    | continue 
                    | return_expr ';'"""
        p[0] = [p[1]]

    def p_instruction_2(self, p):
        """instruction : PRINT create_stmt ';'"""
        p[0] = p[2]

    def p_instruction_brackets(self, p):
        """instruction : '{' instructions '}'"""
        p[0] = p[2]

    def p_continue(self, p):
        """continue : CONTINUE ';'"""
        p[0] = AST.ContinueExpr(lineno=p.lineno(1))

    def p_break(self, p):
        """break : BREAK ';'"""
        p[0] = AST.BreakExpr(lineno=p.lineno(1))

    def p_id_change(self, p):
        """id_change : ID 
                    | ID '[' expression ',' expression ']'
                    | ID '[' expression ']'"""
        if len(p) == 2:
            p[0] = AST.Id(p[1], lineno=p.lineno(1))
        elif len(p) > 5:
            p[0] = AST.Variable(AST.Id(p[1], lineno=p.lineno(1)), (p[3], p[5]), lineno=p.lineno(1))
        else:
            p[0] = AST.Variable(AST.Id(p[1], lineno=p.lineno(1)), (p[3], ), lineno=p.lineno(1))

    def p_assignment(self, p):
        """assignment : id_change '=' expression ';'
                    | id_change ADDASSIGN expression ';'
                    | id_change SUBASSIGN expression ';'
                    | id_change MULASSIGN expression ';'
                    | id_change DIVASSIGN expression ';'
                    | id_change '=' id_change ';'
                    | id_change ADDASSIGN id_change ';'
                    | id_change SUBASSIGN id_change ';'
                    | id_change MULASSIGN id_change ';'
                    | id_change DIVASSIGN id_change ';'"""
        p[0] = AST.AssignExpr(p[2], p[1], p[3], lineno=p.lineno(2))

    def p_expression_binop(self, p):
        """expression : expression ADD expression
                    | expression MINUS expression
                    | expression MUL expression
                    | expression DIVIDE expression"""
        p[0] = AST.BinExpr(p[2], p[1], p[3], lineno=p.lineno(2))

    def p_expressions_unaryneg(self, p):
        '''expression : MINUS expression %prec UMINUS'''
        p[0] = AST.Uminus(p[2], lineno=p.lineno(1))

    def p_expressions_transpose(self, p):
        '''expression : ID "\'"'''
        p[0] = AST.TransposeExpr(AST.Id(p[1], lineno=p.lineno(1)), lineno=p.lineno(1))

    def p_expression_matrixop(self, p):
        """expression : expression DOTADD expression
                    | expression DOTSUB expression
                    | expression DOTMUL expression
                    | expression DOTDIVIDE expression"""
        p[0] = AST.MatrixBinExpr(p[2], p[1], p[3], lineno=p.lineno(2))

    def p_expression_number(self, p):
        """expression : matrix_expression
                    | matrix_create
                    | vector_create"""
        p[0] = p[1]

    def p_intnum(self, p):
        """expression : INTNUM"""
        p[0] = AST.IntNum(p[1], lineno=p.lineno(1))

    def p_float(self, p):
        """expression : FLOAT"""
        p[0] = AST.FloatNum(p[1], lineno=p.lineno(1))  

    def p_expression_id(self, p):
        """expression : ID"""
        p[0] = AST.Id(p[1], lineno=p.lineno(1))

    def p_matrix_expression_z(self, p):
        """matrix_expression : ZEROS '(' expression ')' """
        p[0] = AST.Zeros(p[3], lineno=p.lineno(1))

    def p_matrix_expression_o(self, p):
        """matrix_expression : ONES '(' expression ')' """
        p[0] = AST.Ones(p[3], lineno=p.lineno(1))

    def p_matrix_expression_e(self, p):
        """matrix_expression : EYE '(' expression ')' """
        p[0] = AST.Eye(p[3], lineno=p.lineno(1))

    def p_matrix_create(self, p):
        """matrix_create : '[' matrix_rows ']'"""
        p[0] = AST.Matrix(p[2], lineno=p.lineno(1))

    def p_vector_create(self, p):
        """vector_create : '[' vector_elems ']'"""
        p[0] = AST.Vector(p[2], lineno=p.lineno(1))
    
    def p_vector_elems(self, p):
        """vector_elems : expression ',' vector_elems
                    | expression"""
        if len(p) > 2:
            p[0] = [p[1]] + p[3]
        else:
            p[0] = [p[1]]

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
        p[0] = AST.RelExpr(p[2], p[1], p[3], lineno=p.lineno(2))

    def p_if_stmt(self, p):
        """if_stmt : IF '(' condition ')' instruction %prec IFX
                | IF '(' condition ')' instruction ELSE instruction
                """
        if len(p) < 7:
            p[0] = AST.IfExpr(p[3], AST.InstructionsExpr(p[5], lineno=p.lineno(1)), lineno=p.lineno(1))
        else:
            p[0] = AST.IfExpr(p[3], AST.InstructionsExpr(p[5], lineno=p.lineno(1)), AST.InstructionsExpr(p[7], lineno=p.lineno(1)), lineno=p.lineno(1))

    def p_create_stmt(self, p):
        """create_stmt : p_print_list"""
        p[0] = [AST.PrintExpr(p[1], lineno=p.lineno(1))]

    def p_print_list_1(self, p):
        """p_print_list : STRING """
        p[0] = [AST.String(p[1], lineno=p.lineno(1))]

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
        p[0] = AST.WhileExpr(p[3], AST.InstructionsExpr(p[5], lineno=p.lineno(1)), lineno=p.lineno(1))

    def p_for_l(self, p):
        """for_l : FOR ID "=" expression ":" expression instruction"""
        p[0] = AST.ForExpr(AST.Id(p[2], lineno=p.lineno(1)), p[4], p[6], AST.InstructionsExpr(p[7], lineno=p.lineno(1)), lineno=p.lineno(1))

    def p_return_expr(self, p):
        """return_expr : RETURN
                    | RETURN expression"""
        if len(p) < 3:
            p[0] = AST.RetrunExpr(lineno=p.lineno(1))
        else:
            p[0] = AST.RetrunExpr(p[2], lineno=p.lineno(1))

    def p_error(self, p):
        if p:
            print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
        else:
            print("Unexpected end of input")
        # AST.Error()

    # Mparser = yacc.yacc()