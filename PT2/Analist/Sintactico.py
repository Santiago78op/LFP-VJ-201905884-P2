from Analist.Lexico import *
import ply.yacc as yacc
import json
import sys
import os

class Parser(object):
    
    # CONSTRUCTOR
    def __init__(self):
        self.arbol = 'digraph "round-table" {\n \tnode[shape=box fontname="Arial" fillcolor="white" style=filled ]'
    
    # Syntactic column finder
    def getColumn(self, t):
        line_start = self.data.rfind('\n', 0, t.lexpos) + 1
        return (t.lexpos-line_start)+1
    
    tokens = Lexico.tokens
    
    # * Beginning of the syntactic analysis

    # Indicates precedence in the language
    precedence = (
        ('left', 'PLUS', 'MINUS'),  # level 12
        ('left', 'TIMES', 'DIVIDE', 'REST'),  # level 13
        ('left', 'LPAREN', 'RPAREN'),  # level 19
    )
    
    def p_INITIAL(self, p):
        '''
        INITIAL : L_INST 
        '''
        p[0] = p[1]

    def p_L_INST(self, p):
        '''
        L_INST : L_INST INTS
               | INTS
               | empty
        '''
        if len(p) == 3:
            p[0] = p[1]
            p[0].append(p[2])
        else:
            p[0] = [p[1]]      

    def p_INTS(self, p):
        '''
        INTS : METHODS
             | FUNTIONS
             | SENTENCES
        '''
        if len(p) == 2:
            p[0] = p[1]
    
    def p_METHODS(self, p):
        '''
        METHODS : METHODS METHOD
                | METHOD 
        '''
        if len(p) == 3:
            p[0] = p[1]
            p[0].append(p[2])
        else:
            p[0] = [p[1]]
    
    def p_METHOD(self, p):
        '''
        METHOD : METHOD_VOID ID LPAREN RPAREN LKEY empty RKEY 
               | METHOD_VOID ID LPAREN RPAREN LKEY SENTENCES_METHOD RKEY
               | METHOD_VOID ID LPAREN L_PARAMS RPAREN LKEY empty RKEY
               | METHOD_VOID ID LPAREN L_PARAMS RPAREN LKEY SENTENCES_METHOD RKEY
        '''
        if len(p) == 8:
            p[0] = {"metodo": p[1], "id": p[2], "contenido": p[6]}
        elif len(p) == 9:
            p[0] = {"metodo": p[1], "id": p[2],
                    "parametros": p[4], "contenido": p[7]}
    
    def p_SENTENCES_METHOD(self, p):
        '''
        SENTENCES_METHOD : SENTENCES_METHOD SENTENCE_METHOD
                         | SENTENCE_METHOD
        '''
        if len(p) == 3:
            p[0] = p[1]
            p[0].append(p[2])
        else:
            p[0] = [p[1]]
    
    def p_SENTENCE_METHOD(self, p):
        '''
        SENTENCE_METHOD : DECLARATIONS
                        | ASSIGNMENTS
                        | SENTENCES_IF
                        | METHOD_RETURN DOT_AN_DCOMMA
        '''
        if len(p) == 2:
            p[0] = p[1]
        if len(p) == 3:
            p[0] = {'return': p[1]}
            
    def p_FUNTIONS(self, p):
        '''
        FUNTIONS : FUNTIONS FUNTION
                | FUNTION 
        '''
        if len(p) == 3:
            p[0] = p[1]
            p[0].append(p[2])
        else:
            p[0] = [p[1]]
    
    def p_FUNTION(self, p):
        '''
        FUNTION : TYPE_INT COUPLER
                | TYPE_DOUBLE COUPLER
                | TYPE_STRING COUPLER
                | TYPE_CHAR COUPLER
                | TYPE_BOOL COUPLER
        '''
        if len(p) == 3:
            conts = {'Tipo Dato': p[1]}
            p[2].update(conts)
            p[0] = {"funcion": p[2]}
            
    def p_COUPLER(self, p):
        '''
        COUPLER : ID LPAREN RPAREN LKEY empty RKEY 
                | ID LPAREN RPAREN LKEY SENTENCES_FUNTION RKEY
                | ID LPAREN L_PARAMS RPAREN LKEY empty RKEY
                | ID LPAREN L_PARAMS RPAREN LKEY SENTENCES_FUNTION RKEY
        '''
        if len(p) == 7:
            p[0] = {"id": p[1], "contenido": p[5]}
        elif len(p) == 8:
            p[0] = {"id": p[1],
                    "parametros": p[3], "contenido": p[6]}
    
    def p_SENTENCES_FUNTION(self, p):
        '''
        SENTENCES_FUNTION : SENTENCES_FUNTION SENTENCE_FUNTION
                          | SENTENCE_FUNTION
        '''
        if len(p) == 3:
            p[0] = p[1]
            p[0].append(p[2])
        else:
            p[0] = [p[1]]
    
    def p_SENTENCE_FUNTION(self, p):
        '''
        SENTENCE_FUNTION : DECLARATIONS
                         | ASSIGNMENTS
                         | METHOD_RETURN TYPE_DATO DOT_AN_DCOMMA
                         | METHOD_RETURN ID DOT_AN_DCOMMA
        '''
        if len(p) == 2:
            p[0] = p[1]
        if len(p) == 4:
            p[0] = {'return': p[1], 'Valor':p[2], 'Dato Tipo': p.slice[2].type}

    
    def p_SENTENCES_IF(self,p):
        '''
        SENTENCES_IF : SENTENCES_IF SENTENCE_IF
                     | SENTENCE_IF
        '''
        if len(p) == 3:
            p[0] = p[1]
            p[0].append(p[2])
        else:
            p[0] = [p[1]]
    
    def p_SENTENCE_IF(self, p):
        '''
        SENTENCE_IF : CONDITIONAL_IF LPAREN OPTIONS RPAREN LKEY SENTENCES RKEY
        '''
        p[0] = {"CONDITIONAL_IF": p[1], "OPTIONS": p[3], 'SENTENCES':p[6]}
            
    def p_OPTIONS(self, p):
        '''
        OPTIONS : OPTIONS OPTION
                | OPTION
        '''
        if len(p) == 3:
            p[0] = p[1]
            p[0].append(p[2])
        else:
            p[0] = [p[1]]
    
    
    def p_OPTION(self, p):
        '''
        OPTION : OPTION IQUALS OPTION
               | OPTION DIFFERENT OPTION
               | OPTION IQUAL_GREATER OPTION
               | OPTION IQUAL_LESS OPTION
               | OPTION AND OPTION
               | OPTION OR OPTION
               | OPTION NOT OPTION
               | OPTION GREATER OPTION
               | OPTION LESS OPTION
               | ID
               | TYPE_DATO
        '''
        if len(p) == 2:
            p[0] = {"valor": p[1]}
        else:
            p[0] = {"OPTION_1": p[1], "Operators": p[2], "OPTION_2": p[3]}

    def p_SENTENCES(self, p):
        '''
        SENTENCES : SENTENCES SENTENCE
                  | SENTENCE
        '''
        if len(p) == 3:
            p[0] = p[1]
            p[0].append(p[2])
        else:
            p[0] = [p[1]]

    def p_SENTENCE(self, p):
        '''
        SENTENCE : DECLARATIONS
                 | ASSIGNMENTS
        '''
        if len(p) == 2:
            p[0] = p[1]

    def p_DECLARATIONS(self, p):
        '''
        DECLARATIONS : DECLARATIONS DECLARATION
                     | DECLARATION
        '''
        if len(p) == 3:
            p[0] = p[1]
            p[0].append(p[2])
        else:
            p[0] = [p[1]]

    def p_DECLARATION(self, p):
        '''
        DECLARATION : TYPE_INT ID IQUAL INT DOT_AN_DCOMMA
                    | TYPE_DOUBLE ID IQUAL FLOAT DOT_AN_DCOMMA
                    | TYPE_STRING ID IQUAL STRING DOT_AN_DCOMMA
                    | TYPE_CHAR ID IQUAL CHAR DOT_AN_DCOMMA
                    | TYPE_BOOL ID IQUAL DATA_BOOL DOT_AN_DCOMMA
        '''
        self.arbol += '\n \tA [label="{}"]'.format('DECLARATION')
        self.arbol += '\n \tB [label="{}"]'.format(p[1])
        self.arbol += '\n \tC [label="{}"]'.format(p[2])
        if p.slice[4].type == 'STRING':
            new_string = p[4].replace('"', '')
            self.arbol += '\n \tD [label="primitivo<{}> \n {}"]'.format(
                p.slice[4].type, new_string)
        self.arbol += '\n \tA -> B'
        self.arbol += '\n \tA -> C'
        self.arbol += '\n \tA -> D'
        p[0] = {'Tipo Dato': p[1], 'ID': p[2],
                'Dato': {'Dato Tipo': p.slice[4].type, 'valor': p[4]}}

    def p_ASSIGNMENTS(self, p):
        '''
        ASSIGNMENTS : ASSIGNMENTS ASSIGNMENT
                    | ASSIGNMENT
        '''
        if len(p) == 3:
            p[0] = p[1]
            p[0].append(p[2])
        else:
            p[0] = [p[1]]

    def p_ASSIGNMENT(self, p):
        '''
        ASSIGNMENT : ID IQUAL INT DOT_AN_DCOMMA
                   | ID IQUAL FLOAT DOT_AN_DCOMMA
                   | ID IQUAL STRING DOT_AN_DCOMMA
                   | ID IQUAL CHAR DOT_AN_DCOMMA
                   | ID IQUAL DATA_BOOL DOT_AN_DCOMMA
        '''
        p[0] = {'ID': p[1],
                'Dato': {'Dato Tipo': p.slice[3].type, 'valor': p[3]}}

    def p_L_PARAMS(self, p):
        '''
        L_PARAMS : L_PARAMS COMMA PARAM
                 | PARAM
        '''
        if len(p) == 4:
            p[0] = p[1]
            cosnt = p[2] + p[3]
            p[0].append(cosnt)
        else:
            p[0] = [p[1]]

    def p_PARAM(self, p):
        '''
        PARAM : TYPE_INT ID
              | TYPE_DOUBLE ID
              | TYPE_STRING ID 
              | TYPE_CHAR ID
              | TYPE_BOOL ID 
        '''
        if len(p) == 3:
            p[0] = {"tipo dato": p[1], "id": p[2]}

    def p_TYPE_DATO(self, p):
        '''
        TYPE_DATO : INT 
                  | FLOAT 
                  | STRING
                  | CHAR 
                  | DATA_BOOL 
        '''
        p[0] = {'Dato Tipo': p[1]}
    
            
    def p_empty(self, p):
        'empty :'
        p[0] = {'empty': 'Sin Codigo'}

    
    # Error rule for syntax errors
    def p_error(self, p):
        print(p)
        if p:
            print(f"Sintaxis no válida cerca de '{p.value}' ({p.type})")
        else:
            print("Ninguna instrucción válida")
    
    # Build the parser
    def build(self, **kwargs):
        #tabmodule='fooparsetab'
        self.parser = yacc.yacc(module=self, **kwargs, start='INITIAL')

    # Test it output
    def test(self, data, lexer):
        self.lexer = lexer
        self.data = data
        result = self.parser.parse(data, self.lexer)
        print(json.dumps(result, indent=4, sort_keys=False))

    def ast(self):
        self.arbol += '\n}'
        print(self.arbol)
        dot = "PT2/HTML/AST/AST_{}_dot.txt".format('prueba')
        with open(dot, 'w') as f:
            f.write(self.arbol)
        result = "PT2/HTML/AST/AST_{}_.pdf".format('prueba')
        os.system("dot -Tpdf " + dot + " -o " + result)
        
