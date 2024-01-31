
import AST
import SymbolTable
from Memory import *
from Exceptions import  *
from visit import *
import sys
import time

sys.setrecursionlimit(10000)

class Interpreter(object):
    @on('node')
    def visit(self, node):
        pass
    
    @when(AST.InstructionsBlankExpr)
    def visit(self, node):
        self.memory = MemoryStack()
        node.instructions.accept(self)
        return
    
    @when(AST.InstructionsExpr)
    def visit(self, node):
        for instruction in node.instructions:
            instruction.accept(self)
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
        if not isinstance(node.left, AST.Variable):
            if node.op == "=":
                self.memory.set(node.left.id, node.right.accept(self))
            elif node.op == "+=":
                self.memory.set(node.left.id, self.memory.get(node.left.id) + node.right.accept(self))
            elif node.op == "-=":
                self.memory.set(node.left.id, self.memory.get(node.left.id) - node.right.accept(self))
            elif node.op == "*=":
                self.memory.set(node.left.id, self.memory.get(node.left.id) * node.right.accept(self))
            elif node.op == "/=":
                self.memory.set(node.left.id, self.memory.get(node.left.id) / node.right.accept(self))
        else:
            ...

    @when(AST.Id)
    def visit(self, node):
        if self.memory.get(node.id) is not None:
            return self.memory.get(node.id)

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
        return int(node.value)

    @when(AST.FloatNum)
    def visit(self, node):
        return float(node.value)
    
    @when(AST.String)
    def visit(self, node):
        return str(node.string)
    
    @when(AST.Variable)
    def visit(self, node):
        vector = self.memory.get(node.name.id)
        print(vector)
    
    @when(AST.PrintExpr)
    def visit(self, node):
        for print_val in node.print_ins:
            print(print_val.accept(self), end=" ")
        print()
        return
        
    @when(AST.WhileExpr)
    def visit(self, node):
        while node.cond.accept(self):
            try:
                if isinstance(node.body, list):
                    for instruction in node.body:
                        instruction.accept(self)
                else:
                    node.body.accept(self)
            except ContinueException as e:
                continue
            except BreakException as e:
                break
            except ReturnValueException as e:
                return e.value
    
    @when(AST.RelExpr)
    def visit(self, node):
        r1 = node.left.accept(self)
        r2 = node.right.accept(self)
        if node.op == "<" :
            return r1 < r2
        elif node.op == "<=":
            return r1 <= r2
        elif node.op == ">":
            return r1 > r2
        elif node.op == ">=":
            return r1 >= r2
        return 

    @when(AST.ForExpr)
    def visit(self, node):
        var = node.var
        end = node.end.accept(self)
        start = node.start.accept(self)
        self.memory.push("for")
        self.memory.set(var.id, start)
        while self.memory.get(var.id) < end:
            try:
                if isinstance(node.body, list):
                    for instruction in node.body:
                        instruction.accept(self)
                else:
                    node.body.accept(self)
            except BreakException as e:
                break
            except ContinueException as e:
                continue
            except ReturnValueException as e:
                self.memory.pop()
                return e.value
            finally:
                self.memory.set(var.id, self.memory.get(var.id) + 1)
        self.memory.pop()
    
    @when(AST.IfExpr)
    def visit(self, node):
        cond = node.cond
        if cond:
            self.memory.push("if")
            if isinstance(node.if_body, AST.InstructionsExpr):
                node.if_body.accept(self)
            else:
                for instruction in node.if_body:
                    instruction.accept(self)
            self.memory.pop()
        else:
            if node.else_body is not None:
                self.push("else")
                node.else_body.accept(self)
                self.memory.pop()
    
    @when(AST.Zeros)
    def visit(self, node):
        val = node.val.accept(self)
        return [[0 for _ in range(val)] for _ in range(val)]
    
    @when(AST.Ones)
    def visit(self, node):
        val = node.val.accept(self)
        return [[1 for _ in range(val)] for _ in range(val)]
    
    @when(AST.Eye)
    def visit(self, node):
        val = node.val.accept(self)
        return [[1 if i == j else 0 for i in range(val)] for j in range(val)]
