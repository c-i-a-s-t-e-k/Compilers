
import AST
import SymbolTable
from Memory import *
from Exceptions import  *
from visit import *
import sys

sys.setrecursionlimit(10000)

class Interpreter(object):
    def __init__(self) -> None:
        self.srack = MemoryStack()
        self.memory = Memory("variabes")

    @on('node')
    def visit(self, node):
        pass

    @when(AST.InstructionsExpr)
    def visit(self, node):
        for instruction in node.instructions:
            instruction.accept(self)
        return
    
    @when(AST.InstructionsBlankExpr)
    def visit(self, node):
        node.instructions.accept(self)
        return
        
    @when(AST.BinExpr)
    def visit(self, node):
        r1 = node.left.accept(self)
        r2 = node.right.accept(self)
        if node.op == "+" :
            return r1 + r2
        elif node.op == "-":
            return r1 - r2
        elif node.op == "*":
            return r1 * r2
        elif node.op == "/":
            return r1 / r2
        # try sth smarter than:
        # if(node.op=='+') return r1+r2
        # elsif(node.op=='-') ...
        # but do not use python eval

    @when(AST.AssignExpr)
    def visit(self, node):
        r1 = node.left
        r2 = node.right.accept(self)
        print(r2)
        name = r1.id
        if node.op == "=":
            self.memory.put(name, r2)
            return r2
        elif node.op == "+=":
            val = self.memory.get(name)
            self.memory.put(name, val + r2)
            return r1 + r2
        elif node.op == "-=":
            val = self.memory.get(name)
            self.memory.put(name, val - r2)
            return r1 - r2
        elif node.op == "*=":
            val = self.memory.get(name)
            self.memory.put(name, val * r2)
            return r1 * r2
        elif node.op == "/=":
            val = self.memory.get(name)
            self.memory.put(name, val / r2)
            return r1 / r2

    @when(AST.BreakExpr)
    def visit(self, node):
        raise BreakException()
    
    @when(AST.ContinueExpr)
    def visit(self, node):
        raise ContinueException()
    
    @when(AST.RetrunExpr)
    def visit(self, node):
        r = node.return_val.accept(self)
        raise ReturnValueException(r)

    @when(AST.IntNum)
    def visit(self, node):
        return node.value

    @when(AST.FloatNum)
    def visit(self, node):
        return node.value
    
    @when(AST.String)
    def visit(self, node):
        return node.string
    
    @when(AST.Variable)
    def visit(self, node):
        if self.memory.has_key(node.name):
            return self.memory.get(node.name)
        else:
            self.memory.put(node.name, None)
        return None
    
    @when(AST.PrintExpr)
    def visit(self, node):
        to_print = node.print_ins
        for print_val in to_print:
            if isinstance(print_val, AST.Id):
                print(self.memory.get(print_val.id))
            else:
                print(print_val, end=" ")
        print()
        return
        
    # simplistic while loop interpretation
    @when(AST.WhileExpr)
    def visit(self, node):
        r = None
        while node.cond.accept(self):
            try:
                r = node.body.accept(self)
            except BreakException as e:
                return r
            except ContinueException as e:
                pass
            except ReturnValueException as e:
                return e.value
        return r
    
    @when(AST.ForExpr)
    def visit(self, node):
        r = None
        end = node.end.accept(self)
        curr = node.start.accept(self)
        while curr < end:
            try:
                r = node.body.accept(self)
                curr +=  node.var.accept(self)
            except BreakException as e:
                return r
            except ContinueException as e:
                curr +=  node.var.accept(self)
            except ReturnValueException as e:
                return e.value
    
    @when(AST.IfExpr)
    def visit(self, node):
        try:
            if node.cond.accept(self):
                return node.if_body.accept(self)
            else:
                return node.else_body.accept(self)
        except ReturnValueException as e:
            return e.value