#!/usr/bin/python
from collections import defaultdict
import AST
ttype = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: "")))
from SymbolTable import SymbolTable

#Bin expression
ttype['+']['int']['int'] = 'int'
ttype['+']['int']['float'] = 'float'
ttype['+']['float']['int'] = 'float'
ttype['+']['float']['float'] = 'float'

ttype['-']['int']['int'] = 'int'
ttype['-']['int']['float'] = 'float'
ttype['-']['float']['int'] = 'float'
ttype['-']['float']['float'] = 'float'

ttype['*']['int']['int'] = 'int'
ttype['*']['int']['float'] = 'float'
ttype['*']['float']['int'] = 'float'
ttype['*']['float']['float'] = 'float'

ttype['/']['int']['int'] = 'float'
ttype['/']['int']['float'] = 'float'
ttype['/']['float']['int'] = 'float'
ttype['/']['float']['float'] = 'float'


#Matrix bin expression
ttype['.+']['matrix']['matrix'] = 'matrix'
ttype['.-']['matrix']['matrix'] = 'matrix'
ttype['.*']['matrix']['matrix'] = 'matrix'
ttype['./']['matrix']['matrix'] = 'matrix'

#Vector bin expression
ttype['+']['vector']['vector'] = 'vector'
ttype['-']['vector']['vector'] = 'vector'


#Relation expression
ttype['<']['int']['int'] = 'bool'
ttype['<']['int']['float'] = 'bool'
ttype['<']['float']['int'] = 'bool'
ttype['<']['float']['float'] = 'bool'

ttype['>']['int']['int'] = 'bool'
ttype['>']['int']['float'] = 'bool'
ttype['>']['float']['int'] = 'bool'
ttype['>']['float']['float'] = 'bool'

ttype['>=']['int']['int'] = 'bool'
ttype['>=']['int']['float'] = 'bool'
ttype['>=']['float']['int'] = 'bool'
ttype['>=']['float']['float'] = 'bool'

ttype['<=']['int']['int'] = 'bool'
ttype['<=']['int']['float'] = 'bool'
ttype['<=']['float']['int'] = 'bool'
ttype['<=']['float']['float'] = 'bool'

ttype['==']['int']['int'] = 'bool'
ttype['==']['int']['float'] = 'bool'
ttype['==']['float']['int'] = 'bool'
ttype['==']['float']['float'] = 'bool'

ttype['!=']['int']['int'] = 'bool'
ttype['!=']['int']['float'] = 'bool'
ttype['!=']['float']['int'] = 'bool'
ttype['!=']['float']['float'] = 'bool'


#Assign expression
ttype['+=']['int']['int'] = 'int'
ttype['+=']['int']['float'] = 'float'
ttype['+=']['float']['int'] = 'float'
ttype['+=']['float']['float'] = 'float'

ttype['-=']['int']['int'] = 'int'
ttype['-=']['int']['float'] = 'float'
ttype['-=']['float']['int'] = 'float'
ttype['-=']['float']['float'] = 'float'

ttype['*=']['int']['int'] = 'int'
ttype['*=']['int']['float'] = 'float'
ttype['*=']['float']['int'] = 'float'
ttype['*=']['float']['float'] = 'float'

ttype['/=']['int']['int'] = 'float'
ttype['/=']['int']['float'] = 'float'
ttype['/=']['float']['int'] = 'float'
ttype['/=']['float']['float'] = 'float'


class NodeVisitor(object):
    def __init__(self):
        self.symbol_table = SymbolTable(None, "root")
        self.current_scope = self.symbol_table
        self.loop_indent = 0

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)


    def generic_visit(self, node):        # Called if no explicit visitor function exists for a node.
        if isinstance(node, list):
            for elem in node:
                self.visit(elem)
        else:
            for child in node.children:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, AST.Node):
                            self.visit(item)
                elif isinstance(child, AST.Node):
                    self.visit(child)

    # simpler version of generic_visit, not so general
    #def generic_visit(self, node):
    #    for child in node.children:
    #        self.visit(child)



class TypeChecker(NodeVisitor):
    
    def visit_InstructionsExpr(self, node: AST.InstructionsExpr):
        for instruction in node.instructions:
            self.visit(instruction)
        # print(self.symbol_table.symbols)
        
    
    def visit_InstructionsBlankExpr(self, node: AST.InstructionsBlankExpr):
        if node.instructions is not None:
            self.visit(node.instructions)
        # print(self.symbol_table.symbols)

    def visit_IntNum(self, node: AST.IntNum):
        return 'int'
    
    def visit_FloatNum(self, node: AST.FloatNum):
        return 'float'
 
    # TODO: sprawdzić później czy działa (?)
    def visit_Variable(self, node: AST.Variable):
        if node.name.id not in self.symbol_table:
            print(f"{node.lineno} id not found")
            return None
        shape = self.symbol_table.shape[node.name.id]

        if len(shape) != len(node.idx):
            print(f"Line: {node.lineno} Error: Vector size not matched")
            return None

        for i in range(len(node.idx)):
            if node.idx[i] >= shape[i]:
                print(f"Line: {node.lineno}, Error: index out of range")
                return None
        return self.symbol_table.type[node.name.id]
        
    def visit_String(self, node: AST.String):
        return 'str'
    
    def visit_BinExpr(self, node: AST.BinExpr):
        if self.symbol_table.get(node.right.id, node.lineno) is None:
            return None
    
        if self.symbol_table.get(node.left.id, node.lineno) is None:
            return None        

        type1 = self.visit(node.left)     # type1 = node.left.accept(self) 
        type2 = self.visit(node.right)    # type2 = node.right.accept(self)
        op    = node.op
        if ttype[op][type1][type2] == "":
            print(f"Line {node.lineno} Type error: {type1} {op} {type2} is not correct")
            return None
        
        if type1 == "vector" or type2 == "vector":
            
            # if len(node.left.idx) != len(node.right.idx):
            if self.symbol_table.shape[node.left.id] != self.symbol_table.shape[node.right.id]:
                print(f"Line: {node.lineno} Error: Cannot add different dimensions")
                return None
            
            # if node.left.idx != node.right.idx:
            #     print(f"Line: {node.lineno} Error: Not the same shape")
            #     return None

        return ttype[op][type1][type2]
    
    def visit_RelExpr(self, node: AST.RelExpr):
        type1 = self.visit(node.left)
        type2 = self.visit(node.right)
        op    = node.op

        if ttype[op][type1][type2] == "":
            print(f"Line {node.lineno} Type error: {type1} {op} {type2} is not correct")
            return None

        return ttype[op][type1][type2]

    def visit_BreakExpr(self, node: AST.BreakExpr):
        if self.loop_indent == 0:
            print(f"Line {node.lineno} Indent error: cannot break")
            return None
    
    def visit_ContinueExpr(self, node: AST.ContinueExpr):
        if self.loop_indent == 0:
            print(f"Line {node.lineno} Error: cannot continue in not loop expression")
            
    
    def visit_RetrunExpr(self, node: AST.RetrunExpr):
        if node.return_val is not None:
            return node.return_val
        return
    
    def visit_PrintExpr(self, node: AST.PrintExpr):
        for to_print in node.print_ins:
            self.visit(to_print)
    
    def visit_WhileExpr(self, node: AST.WhileExpr):
        self.symbol_table = self.symbol_table.pushScope("while")
        self.loop_indent += 1
        self.visit(node.cond)
        self.visit(node.body)
        self.symbol_table = self.symbol_table.popScope()
        self.loop_indent -= 1

    def visit_ForExpr(self, node: AST.ForExpr):
        self.symbol_table = self.symbol_table.pushScope('for')
        self.loop_indent += 1
        start = self.visit(node.start)
        end = self.visit(node.end)

        if start is None or end is None or start != end:
            print(f"Line {node.lineno} Error in start or end condition")
            self.symbol_table.put(node.var, None)
        else:
            if isinstance(node.var, AST.Id):
                self.symbol_table.put(node.var.id, start)
            else:
                self.symbol_table.put(node.id, start)

        self.visit(node.body)
        self.symbol_table = self.symbol_table.popScope()
        self.loop_indent -= 1
    
    def visit_IfExpr(self, node: AST.IfExpr):
        self.symbol_table = self.symbol_table.pushScope("if")
        self.visit(node.cond)
        self.visit(node.if_body)
        self.symbol_table = self.symbol_table.popScope()
        if node.else_body is not None:
            self.symbol_table = self.symbol_table.pushScope("else")
            self.visit(node.else_body)
            self.symbol_table = self.symbol_table.popScope()

    def visit_AssignExpr(self, node: AST.AssignExpr):
        
        val_type = self.visit(node.right)
        num = -1
        if isinstance(val_type, tuple):
            num = val_type[1]
            val_type = val_type[0]

        if val_type is None:
            return None
        # print(val_type)
        left_id = node.left.id
        if node.op == '=':
            # print(left_id)
            if isinstance(left_id, str):   
                self.symbol_table.put(left_id, val_type)
                self.symbol_table.last_symbol = left_id
            else:
                self.symbol_table.put(left_id.id, val_type)
                self.symbol_table.last_symbol = left_id

            if num != -1:
                self.symbol_table.shape[left_id] = (num, num)
                self.symbol_table.type[left_id] = 'int'
            
            elif val_type == 'vector' and num == -1:
                
                if isinstance(node.right.vector[0], AST.IntNum):
                    self.symbol_table.shape[left_id] = (
                        len(node.right.vector), )
                    flag = True
                else:
                    self.symbol_table.shape[left_id] = (
                        len(node.right.vector), len(node.right.vector[0].vector)
                        )
                    flag = False

                if flag:
                    if isinstance(node.right.vector[0], AST.IntNum):
                        self.symbol_table.type[left_id] = 'int'
                    if isinstance(node.right.vector[0], AST.FloatNum):
                        self.symbol_table.type[left_id] = 'float'
                else:
                    if isinstance(node.right.vector[0].vector[0], AST.IntNum):
                        self.symbol_table.type[left_id] = 'int'
                    if isinstance(node.right.vector[0].vector[0], AST.FloatNum):
                        self.symbol_table.type[left_id] = 'float'

        else:
            var_type = self.symbol_table.get(left_id, node.lineno)
            if var_type == 'vector' and val_type == 'vector':
                var_d = self.symbol_table.shape[left_id]
                val_d = node.right.idx

                if len(var_d) != len(val_d):
                    print(f"{node.lineno} wrong dimensions")
                    return None

                for i in range(len(var_d)):
                    if var_d[i] != val_d[i]:
                        print(f"{node.lineno} wrong dimensions")
                        return None

            if ttype[node.op][var_type][val_type] != '':
                return ttype[node.op][var_type][val_type]
            else:
                print(f"{node.lineno} operation on given values is not defined")
                return None
    

    def visit_TransposeExpr(self, node: AST.TransposeExpr):
        if node.val not in self.symbol_table:
            print(f"{node.lineno} id not found")
            return None
        return

    def visit_Vector(self, node: AST.Vector):
        
        d = len(node.vector)
        for vec in node.vector:
            if isinstance(vec, AST.Vector):
                self.visit(vec.vector)
                ed = len(vec.vector)
            elif isinstance(vec, list):
                ed = len(vec.vector)
            else:
                ed = 1
            if d != ed and ed != 1:
                print("Line: {0} Error: Wrong size of vector".format(node.lineno), end='\n')
                return None
        return 'vector'

    def visit_Uminus(self, node: AST.Uminus):
        val_type = self.visit(node.val)
        if val_type not in ("int", "float"):
            print("Line: {0} Error: Wrong uminus for expression".format(node.lineno))
            return None
    
    def visit_Id(self, node: AST.Id):
        return self.symbol_table.get(node.id, node.lineno)

    def visit_Zeros(self, node: AST.Zeros):
        val_type = self.visit(node.val)
        if val_type != "int":
            print(f"Line: {node.lineno} Error: Incorrect input for function")
            return None
        return ("vector", node.val.value)
    
    def visit_Ones(self, node: AST.Ones):
        val_type = self.visit(node.val)
        if val_type != "int":
            print(f"Line: {node.lineno} Error: Incorrect input for function")
            return None
    
    def visit_Eye(self, node: AST.Eye):
        # print("WITAM v2")
        # print(self.symbol_table.symbols)
        val_type = self.visit(node.val)
        if val_type != "int":
            print(f"Line: {node.lineno} Error: Incorrect input for function")
            return None
        return ("vector", node.val.value)
    
    def visit_Error(self, node: AST.Error):
        print(f"Line: {node.lineno} BOO ERROR :(")