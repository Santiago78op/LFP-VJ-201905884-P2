from Lexico import *
import ply.yacc as yacc
import sys

class Parser(object):
    
    # CONSTRUCTOR
    def __init__(self, lexer):
        print("Parser constructor called")
        self.parser = yacc.yacc(module=self)
        self.lexer = lexer
