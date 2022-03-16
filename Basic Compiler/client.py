from antlr4 import *
from antlr.grmParser import grmParser
from antlr.grmLexer import grmLexer
from listeners.gencode import GenCode

import sys

def main():
  parser = grmParser(CommonTokenStream(grmLexer(FileStream('input.txt'))))
  tree = parser.program()
  gencode = GenCode()
  walker = ParseTreeWalker()
  walker.walk(gencode, tree)


if __name__ == '__main__':
    main()