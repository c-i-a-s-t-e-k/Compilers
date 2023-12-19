class Node(object):
    def accept(self, visitor):
        return visitor.visit(self)
    

class IntNum(Node):
    def __init__(self, value, lineno = 0):
        self.value = value
        self.lineno = lineno

class FloatNum(Node):
    def __init__(self, value, lineno = 0):
        self.value = value
        self.lineno = lineno

class Variable(Node):
    def __init__(self, name, idx = None, lineno = 0):
        self.name = name
        self.idx = idx
        self.lineno = lineno

class String(Node):
    def __init__(self, string, lineno = 0):
        self.string = string
        self.lineno = lineno

class BinExpr(Node):
    def __init__(self, op, left, right, lineno = 0):
        self.op = op
        self.left = left
        self.right = right
        self.lineno = lineno

class RelExpr(Node):
    def __init__(self, op, left, right, lineno = 0):
        self.op = op
        self.left = left
        self.right = right
        self.lineno = lineno

class BreakExpr(Node):
    def __init__(self, lineno = 0):
        self.lineno = lineno
        ...

class ContinueExpr(Node):
    def __init__(self, lineno = 0):
        self.lineno = lineno
        ...

class RetrunExpr(Node):
    def __init__(self, return_val = None, lineno = 0):
        self.return_val = return_val
        self.lineno = lineno

class PrintExpr(Node):
    def __init__(self, print_ins, lineno = 0):
        self.print_ins = print_ins
        self.lineno = lineno

class WhileExpr(Node):
    def __init__(self, cond, body, lineno = 0):
        self.cond = cond
        self.body = body
        self.lineno = lineno

class ForExpr(Node):
    def __init__(self, var, start, end, body, lineno = 0):
        self.var = var
        self.start = start
        self.end = end
        self.body = body
        self.lineno = lineno

class IfExpr(Node):
    def __init__(self, cond, if_body, else_body = None, lineno = 0):
        self.cond = cond
        self.if_body = if_body
        self.else_body = else_body
        self.lineno = lineno

class AssignExpr(Node):
    def __init__(self, op, left, right, lineno = 0):
        self.op = op
        self.left = left
        self.right = right
        self.lineno = lineno

class TransposeExpr(Node):
    def __init__(self, val, lineno = 0):
        self.val = val
        self.lineno = lineno

class MatrixBinExpr(Node):
    def __init__(self, op, left, right, lineno = 0):
        self.op = op
        self.left = left
        self.right = right
        self.lineno = lineno

class InstructionsExpr(Node):
    def __init__(self, instructions, lineno = 0):
        self.instructions = instructions
        self.lineno = lineno

class InstructionsBlankExpr(Node):
    def __init__(self, instructions = None, lineno = 0):
        self.instructions = instructions
        self.lineno = lineno

class Matrix(Node):
    def __init__(self, matrix, lineno = 0):
        self.matrix = matrix
        self.lineno = lineno

class Vector(Node):
    def __init__(self, vector, lineno = 0):
        self.vector = vector
        self.lineno = lineno

class Uminus(Node):
    def __init__(self, val, lineno = 0):
        self.val = val
        self.lineno = lineno

class Id(Node):
    def __init__(self, ID, lineno = 0):
        self.id = ID
        self.lineno = lineno

class Zeros(Node):
    def __init__(self, val, lineno = 0):
        self.val = val
        self.lineno = lineno
        
class Ones(Node):
    def __init__(self, val, lineno = 0):
        self.val = val
        self.lineno = lineno

class Eye(Node):
    def __init__(self, val, lineno = 0):
        self.val = val
        self.lineno = lineno

class Error(Node):
    def __init__(self, lineno = 0):
        self.lineno = lineno
      