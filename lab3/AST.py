class Node(object):
    pass

class IntNum(Node):
    def __init__(self, value):
        self.value = value

class FloatNum(Node):
    def __init__(self, value):
        self.value = value

class Variable(Node):
    def __init__(self, name, idx = None):
        self.name = name
        self.idx = idx

class String(Node):
    def __init__(self, string):
        self.string = string

class BinExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class RelExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class BreakExpr(Node):
    def __init__(self):
        ...

class ContinueExpr(Node):
    def __init__(self):
        ...

class RetrunExpr(Node):
    def __init__(self, return_val = None):
        self.return_val = return_val

class PrintExpr(Node):
    def __init__(self, print_ins):
        self.print_ins = print_ins

class WhileExpr(Node):
    def __init__(self, cond, body):
        self.cond = cond
        self.body = body

class ForExpr(Node):
    def __init__(self, var, start, end, body):
        self.var = var
        self.start = start
        self.end = end
        self.body = body

class IfExpr(Node):
    def __init__(self, cond, if_body, else_body = None):
        self.cond = cond
        self.if_body = if_body
        self.else_body = else_body

class AssignExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class TransposeExpr(Node):
    def __init__(self, val):
        self.val = val

class MatrixBinExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class InstructionsExpr(Node):
    def __init__(self, instructions):
        self.instructions = instructions

class InstructionsBlankExpr(Node):
    def __init__(self, instructions = None):
        self.instructions = instructions

class Matrix(Node):
    def __init__(self, matrix):
        self.matrix = matrix

class Uminus(Node):
    def __init__(self, val):
        self.val = val

class Id(Node):
    def __init__(self, ID):
        self.id = ID

class Zeros(Node):
    def __init__(self, val):
        self.val = val
        
class Ones(Node):
    def __init__(self, val):
        self.val = val

class Eye(Node):
    def __init__(self, val):
        self.val = val

class Error(Node):
    def __init__(self):
        pass
      