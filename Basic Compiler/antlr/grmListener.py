# Generated from c:\Users\Rangel\Documents\GitHub\CompilerDesign\Basic Compiler\antlr\grm.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .grmParser import grmParser
else:
    from grmParser import grmParser

# This class defines a complete listener for a parse tree produced by grmParser.
class grmListener(ParseTreeListener):

    # Enter a parse tree produced by grmParser#program.
    def enterProgram(self, ctx:grmParser.ProgramContext):
        pass

    # Exit a parse tree produced by grmParser#program.
    def exitProgram(self, ctx:grmParser.ProgramContext):
        pass


    # Enter a parse tree produced by grmParser#add.
    def enterAdd(self, ctx:grmParser.AddContext):
        pass

    # Exit a parse tree produced by grmParser#add.
    def exitAdd(self, ctx:grmParser.AddContext):
        pass


    # Enter a parse tree produced by grmParser#number.
    def enterNumber(self, ctx:grmParser.NumberContext):
        pass

    # Exit a parse tree produced by grmParser#number.
    def exitNumber(self, ctx:grmParser.NumberContext):
        pass


    # Enter a parse tree produced by grmParser#assignation.
    def enterAssignation(self, ctx:grmParser.AssignationContext):
        pass

    # Exit a parse tree produced by grmParser#assignation.
    def exitAssignation(self, ctx:grmParser.AssignationContext):
        pass


    # Enter a parse tree produced by grmParser#more.
    def enterMore(self, ctx:grmParser.MoreContext):
        pass

    # Exit a parse tree produced by grmParser#more.
    def exitMore(self, ctx:grmParser.MoreContext):
        pass


    # Enter a parse tree produced by grmParser#variable.
    def enterVariable(self, ctx:grmParser.VariableContext):
        pass

    # Exit a parse tree produced by grmParser#variable.
    def exitVariable(self, ctx:grmParser.VariableContext):
        pass


    # Enter a parse tree produced by grmParser#divide.
    def enterDivide(self, ctx:grmParser.DivideContext):
        pass

    # Exit a parse tree produced by grmParser#divide.
    def exitDivide(self, ctx:grmParser.DivideContext):
        pass


    # Enter a parse tree produced by grmParser#less.
    def enterLess(self, ctx:grmParser.LessContext):
        pass

    # Exit a parse tree produced by grmParser#less.
    def exitLess(self, ctx:grmParser.LessContext):
        pass


    # Enter a parse tree produced by grmParser#multiply.
    def enterMultiply(self, ctx:grmParser.MultiplyContext):
        pass

    # Exit a parse tree produced by grmParser#multiply.
    def exitMultiply(self, ctx:grmParser.MultiplyContext):
        pass


    # Enter a parse tree produced by grmParser#substract.
    def enterSubstract(self, ctx:grmParser.SubstractContext):
        pass

    # Exit a parse tree produced by grmParser#substract.
    def exitSubstract(self, ctx:grmParser.SubstractContext):
        pass


    # Enter a parse tree produced by grmParser#declaration.
    def enterDeclaration(self, ctx:grmParser.DeclarationContext):
        pass

    # Exit a parse tree produced by grmParser#declaration.
    def exitDeclaration(self, ctx:grmParser.DeclarationContext):
        pass


    # Enter a parse tree produced by grmParser#ifelse.
    def enterIfelse(self, ctx:grmParser.IfelseContext):
        pass

    # Exit a parse tree produced by grmParser#ifelse.
    def exitIfelse(self, ctx:grmParser.IfelseContext):
        pass


    # Enter a parse tree produced by grmParser#print.
    def enterPrint(self, ctx:grmParser.PrintContext):
        pass

    # Exit a parse tree produced by grmParser#print.
    def exitPrint(self, ctx:grmParser.PrintContext):
        pass



del grmParser