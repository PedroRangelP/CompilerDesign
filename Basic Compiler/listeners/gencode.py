from antlr.grmListener import grmListener
from antlr.grmParser import grmParser

class GenCode(grmListener):
  def enterProgram(self, ctx:grmParser.ProgramContext):
    print(".text")
  
  def exitNumber(self, ctx:grmParser.NumberContext):
    print("li $t0, " + ctx.Number().getText())
  
  def exitVariable(self, ctx:grmParser.VariableContext):
    print("Variable")
  
  def exitAdd(self, ctx:grmParser.AddContext):
    print("add $t2, $t0, $t1\n")
  
  def exitDivide(self, ctx:grmParser.DivideContext):
    print("div $t2, $t0, $t1\n")

  def exitLess(self, ctx:grmParser.LessContext):
    print("sle $t2, $t0, $t1\n")
  
  def exitMore(self, ctx:grmParser.MoreContext):
    print("sgt $t2, $t0, $t1\n")

  def exitMultiply(self, ctx:grmParser.MultiplyContext):
    print("mulo $t2, $t0, $t1\n")
  
  def exitSubstract(self, ctx:grmParser.SubstractContext):
    print("sub $t2, $t0, $t1\n")

  def exitAssignation(self, ctx:grmParser.AssignationContext):
    print("Assignation\n")
  
  def exitDeclaration(self, ctx:grmParser.DeclarationContext):
    print(".data")
    print(ctx.Variable().getText() + " .word 0\n")
  
  def enterIfelse(self, ctx:grmParser.IfelseContext):
    print("EnterIfElse")
  
  def exitIfelse(self, ctx:grmParser.IfelseContext):
    print("EndIfElse\n")
  
  def exitPrint(self, ctx:grmParser.PrintContext):
    print("syscall")