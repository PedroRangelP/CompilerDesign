# Generated from c:\Users\Rangel\Documents\GitHub\CompilerDesign\Basic Compiler\antlr\grm.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("G\4\2\t\2\4\3\t\3\4\4\t\4\3\2\6\2\n\n\2\r\2\16\2\13\3")
        buf.write("\2\7\2\17\n\2\f\2\16\2\22\13\2\3\3\3\3\3\3\5\3\27\n\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3.\n\3\f\3\16\3\61\13")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4:\n\4\3\4\3\4\3\4\5")
        buf.write("\4?\n\4\3\4\3\4\3\4\3\4\5\4E\n\4\3\4\2\3\4\5\2\4\6\2\2")
        buf.write("\2Q\2\t\3\2\2\2\4\26\3\2\2\2\6D\3\2\2\2\b\n\5\4\3\2\t")
        buf.write("\b\3\2\2\2\n\13\3\2\2\2\13\t\3\2\2\2\13\f\3\2\2\2\f\20")
        buf.write("\3\2\2\2\r\17\5\6\4\2\16\r\3\2\2\2\17\22\3\2\2\2\20\16")
        buf.write("\3\2\2\2\20\21\3\2\2\2\21\3\3\2\2\2\22\20\3\2\2\2\23\24")
        buf.write("\b\3\1\2\24\27\7\17\2\2\25\27\7\20\2\2\26\23\3\2\2\2\26")
        buf.write("\25\3\2\2\2\27/\3\2\2\2\30\31\f\13\2\2\31\32\7\3\2\2\32")
        buf.write(".\5\4\3\f\33\34\f\n\2\2\34\35\7\4\2\2\35.\5\4\3\13\36")
        buf.write("\37\f\t\2\2\37 \7\5\2\2 .\5\4\3\n!\"\f\b\2\2\"#\7\6\2")
        buf.write("\2#.\5\4\3\t$%\f\7\2\2%&\7\7\2\2&.\5\4\3\b\'(\f\6\2\2")
        buf.write("()\7\b\2\2).\5\4\3\7*+\f\5\2\2+,\7\t\2\2,.\5\4\3\6-\30")
        buf.write("\3\2\2\2-\33\3\2\2\2-\36\3\2\2\2-!\3\2\2\2-$\3\2\2\2-")
        buf.write("\'\3\2\2\2-*\3\2\2\2.\61\3\2\2\2/-\3\2\2\2/\60\3\2\2\2")
        buf.write("\60\5\3\2\2\2\61/\3\2\2\2\62\63\7\n\2\2\63E\7\20\2\2\64")
        buf.write("\65\7\13\2\2\65\66\5\4\3\2\669\7\f\2\2\67:\5\4\3\28:\5")
        buf.write("\6\4\29\67\3\2\2\298\3\2\2\2:;\3\2\2\2;>\7\r\2\2<?\5\4")
        buf.write("\3\2=?\5\6\4\2><\3\2\2\2>=\3\2\2\2?E\3\2\2\2@A\7\16\2")
        buf.write("\2AB\5\4\3\2BC\7\f\2\2CE\3\2\2\2D\62\3\2\2\2D\64\3\2\2")
        buf.write("\2D@\3\2\2\2E\7\3\2\2\2\n\13\20\26-/9>D")
        return buf.getvalue()


class grmParser ( Parser ):

    grammarFileName = "grm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'*'", "'/'", "'-'", "'<'", "'>'", 
                     "'='", "'int'", "'if('", "')'", "'else'", "'print('" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "Number", "Variable", "WS" ]

    RULE_program = 0
    RULE_expression = 1
    RULE_statement = 2

    ruleNames =  [ "program", "expression", "statement" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    Number=13
    Variable=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grmParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(grmParser.ExpressionContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grmParser.StatementContext)
            else:
                return self.getTypedRuleContext(grmParser.StatementContext,i)


        def getRuleIndex(self):
            return grmParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = grmParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.expression(0)
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==grmParser.Number or _la==grmParser.Variable):
                    break

            self.state = 14
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << grmParser.T__7) | (1 << grmParser.T__8) | (1 << grmParser.T__11))) != 0):
                self.state = 11
                self.statement()
                self.state = 16
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grmParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AddContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grmParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grmParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(grmParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class NumberContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grmParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Number(self):
            return self.getToken(grmParser.Number, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)


    class AssignationContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grmParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grmParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(grmParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignation" ):
                listener.enterAssignation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignation" ):
                listener.exitAssignation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignation" ):
                return visitor.visitAssignation(self)
            else:
                return visitor.visitChildren(self)


    class MoreContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grmParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grmParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(grmParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMore" ):
                listener.enterMore(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMore" ):
                listener.exitMore(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMore" ):
                return visitor.visitMore(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grmParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Variable(self):
            return self.getToken(grmParser.Variable, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class DivideContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grmParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grmParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(grmParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivide" ):
                listener.enterDivide(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivide" ):
                listener.exitDivide(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivide" ):
                return visitor.visitDivide(self)
            else:
                return visitor.visitChildren(self)


    class LessContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grmParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grmParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(grmParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLess" ):
                listener.enterLess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLess" ):
                listener.exitLess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLess" ):
                return visitor.visitLess(self)
            else:
                return visitor.visitChildren(self)


    class MultiplyContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grmParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grmParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(grmParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiply" ):
                listener.enterMultiply(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiply" ):
                listener.exitMultiply(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiply" ):
                return visitor.visitMultiply(self)
            else:
                return visitor.visitChildren(self)


    class SubstractContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grmParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grmParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(grmParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubstract" ):
                listener.enterSubstract(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubstract" ):
                listener.exitSubstract(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubstract" ):
                return visitor.visitSubstract(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = grmParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grmParser.Number]:
                localctx = grmParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 18
                self.match(grmParser.Number)
                pass
            elif token in [grmParser.Variable]:
                localctx = grmParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 19
                self.match(grmParser.Variable)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 45
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 43
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = grmParser.AddContext(self, grmParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 22
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 23
                        self.match(grmParser.T__0)
                        self.state = 24
                        self.expression(10)
                        pass

                    elif la_ == 2:
                        localctx = grmParser.MultiplyContext(self, grmParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 25
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 26
                        self.match(grmParser.T__1)
                        self.state = 27
                        self.expression(9)
                        pass

                    elif la_ == 3:
                        localctx = grmParser.DivideContext(self, grmParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 28
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 29
                        self.match(grmParser.T__2)
                        self.state = 30
                        self.expression(8)
                        pass

                    elif la_ == 4:
                        localctx = grmParser.SubstractContext(self, grmParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 31
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 32
                        self.match(grmParser.T__3)
                        self.state = 33
                        self.expression(7)
                        pass

                    elif la_ == 5:
                        localctx = grmParser.LessContext(self, grmParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 34
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 35
                        self.match(grmParser.T__4)
                        self.state = 36
                        self.expression(6)
                        pass

                    elif la_ == 6:
                        localctx = grmParser.MoreContext(self, grmParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 37
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 38
                        self.match(grmParser.T__5)
                        self.state = 39
                        self.expression(5)
                        pass

                    elif la_ == 7:
                        localctx = grmParser.AssignationContext(self, grmParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 40
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 41
                        self.match(grmParser.T__6)
                        self.state = 42
                        self.expression(4)
                        pass

             
                self.state = 47
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grmParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grmParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(grmParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)


    class DeclarationContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grmParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Variable(self):
            return self.getToken(grmParser.Variable, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)


    class IfelseContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grmParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grmParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(grmParser.ExpressionContext,i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grmParser.StatementContext)
            else:
                return self.getTypedRuleContext(grmParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfelse" ):
                listener.enterIfelse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfelse" ):
                listener.exitIfelse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfelse" ):
                return visitor.visitIfelse(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = grmParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grmParser.T__7]:
                localctx = grmParser.DeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.match(grmParser.T__7)
                self.state = 49
                self.match(grmParser.Variable)
                pass
            elif token in [grmParser.T__8]:
                localctx = grmParser.IfelseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.match(grmParser.T__8)
                self.state = 51
                self.expression(0)
                self.state = 52
                self.match(grmParser.T__9)
                self.state = 55
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [grmParser.Number, grmParser.Variable]:
                    self.state = 53
                    self.expression(0)
                    pass
                elif token in [grmParser.T__7, grmParser.T__8, grmParser.T__11]:
                    self.state = 54
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 57
                self.match(grmParser.T__10)
                self.state = 60
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [grmParser.Number, grmParser.Variable]:
                    self.state = 58
                    self.expression(0)
                    pass
                elif token in [grmParser.T__7, grmParser.T__8, grmParser.T__11]:
                    self.state = 59
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [grmParser.T__11]:
                localctx = grmParser.PrintContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 62
                self.match(grmParser.T__11)
                self.state = 63
                self.expression(0)
                self.state = 64
                self.match(grmParser.T__9)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         




