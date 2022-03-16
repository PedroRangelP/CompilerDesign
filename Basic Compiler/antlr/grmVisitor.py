# Generated from c:\Users\Rangel\Documents\GitHub\CompilerDesign\Basic Compiler\antlr\grm.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .grmParser import grmParser
else:
    from grmParser import grmParser

# This class defines a complete generic visitor for a parse tree produced by grmParser.

class grmVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by grmParser#program.
    def visitProgram(self, ctx:grmParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grmParser#add.
    def visitAdd(self, ctx:grmParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grmParser#number.
    def visitNumber(self, ctx:grmParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grmParser#assignation.
    def visitAssignation(self, ctx:grmParser.AssignationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grmParser#more.
    def visitMore(self, ctx:grmParser.MoreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grmParser#variable.
    def visitVariable(self, ctx:grmParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grmParser#divide.
    def visitDivide(self, ctx:grmParser.DivideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grmParser#less.
    def visitLess(self, ctx:grmParser.LessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grmParser#multiply.
    def visitMultiply(self, ctx:grmParser.MultiplyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grmParser#substract.
    def visitSubstract(self, ctx:grmParser.SubstractContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grmParser#declaration.
    def visitDeclaration(self, ctx:grmParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grmParser#ifelse.
    def visitIfelse(self, ctx:grmParser.IfelseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grmParser#print.
    def visitPrint(self, ctx:grmParser.PrintContext):
        return self.visitChildren(ctx)



del grmParser