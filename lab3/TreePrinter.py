from __future__ import print_function
import AST
from Mparser import Mparser
from ply.lex import LexError
import ply.yacc as yacc
import os



def addToClass(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func

    return decorator


class TreePrinter:
    
    def print_indent(num):
        print(num * "|\t", end="")

    @addToClass(AST.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(AST.IntNum)
    def printTree(self, indent=0):
        TreePrinter.print_indent(indent)
        print(self.value)

    @addToClass(AST.FloatNum)
    def printTree(self, indent=0):
        TreePrinter.print_indent(indent)
        print(self.value)

    @addToClass(AST.Variable)
    def printTree(self, indent=0):
        TreePrinter.print_indent(indent)
        print("REF")
        self.name.printTree(indent + 1)
        if self.idx is not None:
            for expr in self.idx:
                expr.printTree(indent + 1)
    
    @addToClass(AST.String)
    def printTree(self, indent=0):
        TreePrinter.print_indent(indent)
        print("STRING")
        print(self.string)

    @addToClass(AST.BinExpr)
    def printTree(self, indent=0):
        TreePrinter.print_indent(indent)
        print(self.op)
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.RelExpr)
    def printTree(self, indent=0):
        TreePrinter.print_indent(indent)
        print(self.op)
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.BreakExpr)
    def printTree(self, indent=0):
        TreePrinter.print_indent(indent)
        print("BREAK")
    
    @addToClass(AST.ContinueExpr)
    def printTree(self, indent=0):
        TreePrinter.print_indent(indent)
        print("CONTINUE")

    @addToClass(AST.RetrunExpr)
    def printTree(self, indent=0):
        TreePrinter.print_indent(indent)
        print("RETURN")
        if self.return_val is not None:
            self.return_val.printTree(indent + 1)

    @addToClass(AST.PrintExpr)
    def printTree(self, indent=0):
        TreePrinter.print_indent(indent)
        print("PRINT")
        for to_print in self.print_ins:
            to_print.printTree(indent + 1)
    
    @addToClass(AST.WhileExpr)
    def printTree(self, indent=0):
        TreePrinter.print_indent(indent)
        print("WHILE")
        self.cond.printTree(indent + 1)
        self.body.printTree(indent + 1)
    
    @addToClass(AST.ForExpr)
    def printTree(self, indent=0):
        TreePrinter.print_indent(indent)
        print("FOR")
        self.var.printTree(indent + 1)
        TreePrinter.print_indent(indent + 1)
        print("RANGE")
        self.start.printTree(indent + 2)
        self.end.printTree(indent + 2)
        self.body.printTree(indent + 1)
    
    @addToClass(AST.IfExpr)
    def printTree(self, indent=0):
        TreePrinter.print_indent(indent)
        print("IF")

        self.cond.printTree(indent + 1)
        TreePrinter.print_indent(indent)

        print("THEN")
        self.if_body.printTree(indent + 1)

        if self.else_body is not None:
            TreePrinter.print_indent(indent)
            print("ELSE")
            self.else_body.printTree(indent + 1)
    
    @addToClass(AST.AssignExpr)
    def printTree(self, indent=0):
        TreePrinter.print_indent(indent)
        print(self.op)
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.TransposeExpr)
    def printTree(self, indent=0):
        TreePrinter.print_indent(indent)
        print("TRANSPOSE")
        self.val.printTree(indent + 1)

    @addToClass(AST.MatrixBinExpr)
    def printTree(self, indent=0):
        TreePrinter.print_indent(indent)
        print(self.op)
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.InstructionsExpr)
    def printTree(self, indent=0):
        for instr in self.instructions:
            instr.printTree(indent)

    @addToClass(AST.InstructionsBlankExpr)
    def printTree(self, indent=0):
        self.instructions.printTree(indent)
    
    @addToClass(AST.Matrix)
    def printTree(self, indent=0):
        TreePrinter.print_indent(indent)
        print("VECTOR")
        for row in self.matrix:
            TreePrinter.print_indent(indent + 1)
            print("VECTOR")
            for col in row:
                col.printTree(indent + 2)

    @addToClass(AST.Uminus)
    def printTree(self, indent=0):
        TreePrinter.print_indent(indent)
        print("UMINUS")
        self.val.printTree(indent + 1)
    
    @addToClass(AST.Id)
    def printTree(self, indent=0):
        TreePrinter.print_indent(indent)
        print(self.id)
    
    @addToClass(AST.Zeros)
    def printTree(self, indent=0):
        TreePrinter.print_indent(indent)
        print("zeros")
        self.val.printTree(indent + 1)
    
    @addToClass(AST.Ones)
    def printTree(self, indent=0):
        TreePrinter.print_indent(indent)
        print("ones")
        self.val.printTree(indent + 1)

    @addToClass(AST.Eye)
    def printTree(self, indent=0):
        TreePrinter.print_indent(indent)
        print("eye")
        self.val.printTree(indent + 1)

    @addToClass(AST.Error)
    def printTree(self, indent=0):
        TreePrinter.print_indent(indent)
        print("BOO - error bruh")
    
