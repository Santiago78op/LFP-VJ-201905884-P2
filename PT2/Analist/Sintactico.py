from Analist.Lexico import *
from Analist.Error import Error
from Analist.Ast import AST
import ply.yacc as yacc
import json
import sys
import os


class Parser(object):

    # CONSTRUCTOR
    def __init__(self):
        self.id_n = 1
        self.tree = 'digraph T{\n \tnode[shape=box fontname="Arial" fillcolor="white" style=filled ]'

    # Syntactic column finder
    def getColumn(self,input, p):
        lexema_len = 1
        tamano = f'{p.value}'
        for num in tamano:
            lexema_len += 1
        line_start = input.rfind('\n', 0, p.lexpos) + 1
        return(p.lexpos - line_start) + lexema_len

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
                        | SENTENCES_WHILE
                        | COMENTLINE
                        | COMENTMULTYLINE
                        | BREAK DOT_AN_DCOMMA
                        | CONTINUE DOT_AN_DCOMMA
                        | METHOD_RETURN DOT_AN_DCOMMA
                        | ID LPAREN CALLS RPAREN
        '''
        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 3:
            p[0] = {'return': p[1]}
        elif len(p) == 5:
            p[0] = {'ID': p[1], 'CALL': p[3]}
        else:
            p[0] = {'control': p[1]}
    
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
                         | SENTENCES_IF
                         | SENTENCES_WHILE
                         | COMENTLINE
                         | COMENTMULTYLINE
                         | BREAK DOT_AN_DCOMMA
                         | CONTINUE DOT_AN_DCOMMA
                         | METHOD_RETURN TYPE_DATO DOT_AN_DCOMMA
                         | METHOD_RETURN ID DOT_AN_DCOMMA
                         | ID LPAREN CALLS RPAREN
        '''
        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 4:
            p[0] = {'return': p[1], 'Valor': p[2],
                    'Dato Tipo': p.slice[2].type}
        elif len(p) == 5:
            p[0] = {'ID': p[1], 'CALL': p[3]}
        else:
            p[0] = {'control': p[1]}


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
                 | SENTENCE_IF
                 | SENTENCE_WHILE
                 | COMENTLINE
                 | COMENTMULTYLINE
                 | BREAK DOT_AN_DCOMMA
                 | CONTINUE DOT_AN_DCOMMA
                 | ID LPAREN CALLS RPAREN
        '''
        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 5:
            p[0] = {'ID':p[1],'CALL':p[3]}
        else:
            p[0] = {'control':p[1]}
            
    def p_SENTENCES_IF(self, p):
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
        SENTENCE_IF : CONDITIONAL_IF LPAREN INSTRUCTIONS RPAREN LKEY SENTENCES RKEY
                    | CONDITIONAL_IF LPAREN INSTRUCTIONS RPAREN LKEY SENTENCES RKEY CONDITIONAL_ELSE LKEY SENTENCES RKEY
                    | CONDITIONAL_IF LPAREN INSTRUCTIONS RPAREN LKEY SENTENCES_FUNTION RKEY
                    | CONDITIONAL_IF LPAREN INSTRUCTIONS RPAREN LKEY SENTENCES_FUNTION RKEY CONDITIONAL_ELSE LKEY SENTENCES_FUNTION RKEY
                    | CONDITIONAL_IF LPAREN INSTRUCTIONS RPAREN LKEY SENTENCES_METHOD RKEY
                    | CONDITIONAL_IF LPAREN INSTRUCTIONS RPAREN LKEY SENTENCES_METHOD RKEY CONDITIONAL_ELSE LKEY SENTENCES_METHOD RKEY
        '''
        if len(p) == 8:
            p[0] = {"CONDITIONAL_IF": p[1],
                    "INSTRUCTIONS": p[3], 'SENTENCES': p[6]}
        else:
            p[0] = {"CONDITIONAL_IF": p[1],
                    "INSTRUCTIONS": p[3], 'SENTENCES_1': p[6], 'CONDITIONAL_ELSE': p[8], 'SENTENCES_2': p[10]}

    def p_SENTENCES_WHILE(self, p):
        '''
        SENTENCES_WHILE : SENTENCES_WHILE SENTENCE_WHILE
                        | SENTENCE_WHILE
        '''
        if len(p) == 3:
            p[0] = p[1]
            p[0].append(p[2])
        else:
            p[0] = [p[1]]

    def p_SENTENCE_WHILE(self, p):
        '''
        SENTENCE_WHILE : ITERATIVE_WHILE LPAREN INSTRUCTIONS RPAREN LKEY SENTENCES RKEY
                       | ITERATIVE_DO LKEY SENTENCES RKEY ITERATIVE_WHILE LPAREN INSTRUCTIONS RPAREN DOT_AN_DCOMMA
                       | ITERATIVE_WHILE LPAREN INSTRUCTIONS RPAREN LKEY SENTENCES_FUNTION RKEY
                       | ITERATIVE_DO LKEY SENTENCES_FUNTION RKEY ITERATIVE_WHILE LPAREN INSTRUCTIONS RPAREN DOT_AN_DCOMMA
                       | ITERATIVE_WHILE LPAREN INSTRUCTIONS RPAREN LKEY SENTENCES_METHOD RKEY
                       | ITERATIVE_DO LKEY SENTENCES_METHOD RKEY ITERATIVE_WHILE LPAREN INSTRUCTIONS RPAREN DOT_AN_DCOMMA
        
        '''
        if len(p) == 8:
            p[0] = {"ITERATIVE_WHILE": p[1],
                    "INSTRUCTIONS": p[3], 'SENTENCES': p[6]}
        else:
            p[0] = {"ITERATIVE_DO": p[1],
                    "SENTENCES": p[3], 'ITERATIVE_WHILE': p[5], 'INSTRUCTIONS': p[7]}
    
    def p_INSTRUCTIONS(self, p):
        '''
        INSTRUCTIONS : INSTRUCTIONS OPTIONS
                     | OPTIONS
        '''
        if len(p) == 3:
            p[0] = p[1]
            p[0].append(p[2])
        else:
            p[0] = [p[1]]
    
    def p_OPTIONS(self, p):
        '''
        OPTIONS : OPTIONS AND OPTIONS
                | OPTIONS OR OPTIONS
                | OPTIONS NOT OPTIONS
                | OPTION
        '''
        if len(p) == 4:
            p[0] = {"Izquierda": p[1], "Operators": p[2], "Derecha": p[3]}
        else:
            p[0] = [p[1]]

    def p_OPTION(self, p):
        '''
        OPTION : OPTION IQUALS OPTION
               | OPTION DIFFERENT OPTION
               | OPTION IQUAL_GREATER OPTION
               | OPTION IQUAL_LESS OPTION
               | OPTION GREATER OPTION
               | OPTION LESS OPTION
               | ID
               | EXPRESSIONS
        '''
        if len(p) == 2:
            p[0] = {"valor": p[1]}
        else:
            p[0] = {"Izquierda": p[1], "Operators": p[2], "Derecha": p[3]}

    
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
        # * Analisis de yacc
        p[0] = {'TYPE': p[1], 'ID': p[2],
                'DATO': {'Tipo': p.slice[4].type, 'valor': p[4]}}

    def p_ASSIGNMENTS(self, p):
        '''
        ASSIGNMENTS : ASSIGNMENTS ASSIGNMENT
                    | ASSIGNMENT
        '''
        if len(p) == 3:
            self.tree += '\n \t{} -> {}'.format(self.id_n, self.id_n+1)
            self.Ast = AST('ASSIGNMENTS', '')
            self.Ast.hijos.append(AST('ASSIGNMENTS ASSIGNMENT', ''))
            self.ast(self.Ast)
            p[0] = p[1]
            p[0].append(p[2])
        else:
            self.Ast = AST('ASSIGNMENTS', '')
            self.Ast.hijos.append(AST('ASSIGNMENT', ''))
            p[0] = [p[1]]

    def p_ASSIGNMENT(self, p):
        '''
        ASSIGNMENT : ID IQUAL INT DOT_AN_DCOMMA
                   | ID IQUAL FLOAT DOT_AN_DCOMMA
                   | ID IQUAL STRING DOT_AN_DCOMMA
                   | ID IQUAL CHAR DOT_AN_DCOMMA
                   | ID IQUAL DATA_BOOL DOT_AN_DCOMMA
                   | ID IQUAL EXPRESSIONS DOT_AN_DCOMMA
        '''   
        if len(p) == 5:
            self.Ast = AST('ASSIGNMENT', '')
            self.Ast.hijos.append(AST(p[1], 'ID'))
            self.Ast.hijos.append(AST(p[3], p.slice[3].type))
            self.ast(self.Ast)
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
            
    def p_CALLS(self, p):
        '''
        CALLS : CALLS COMMA CALL
              | CALL
        '''
        if len(p) == 4:
            p[0] = p[1]
            p[0].append(p[3])
        else:
            p[0] = [p[1]]

    def p_CALL(self, p):
        '''
        CALL : TYPE_DATO
             | ID
        '''
        p[0] = {"tipo dato": p[1]}

    def p_EXPRESSIONS(self, p):
        '''
        EXPRESSIONS : EXPRESSIONS E
                    | E
        '''
        if len(p) == 3:
            p[0] = p[1]
            p[0].append(p[2])
        else:
            p[0] = [p[1]]

    def p_E(self, p):
        '''
        E : E PLUS E
            | E MINUS E
            | E TIMES E
            | E DIVIDE E
            | E REST E
            | ID
            | TYPE_DATO
        '''
        if len(p) == 2:
            p[0] = {"valor": p[1]}
        else:
            p[0] = {"operacion": p[2], "izquierda": p[1], "derecha": p[3]}
            
    def p_TYPE_DATO(self, p):
        '''
        TYPE_DATO : INT 
                  | FLOAT 
                  | STRING
                  | CHAR 
                  | DATA_BOOL 
        '''
        p[0] = {'DATO': p[1]}

    def p_empty(self, p):
        'empty :'
        p[0] = {'empty': 'Sin Codigo'}

    # Error rule for syntax errors
    def p_error(self, p):
        col = self.getColumn(self.data, p)
        tipo = 'Sintáctico'
        if p:
            descripcion =f"Sintaxis no válida cerca de '{p.value}' ({p.type})"
            _error = Error(p.lineno, col, tipo, descripcion)
            self.elementos['errores'].append(_error)
        else:
            descripcion = f"Ninguna instrucción válida"
            _error = Error(p.lineno, col, tipo, descripcion)
            self.elementos['errores'].append(_error)

    # Build the parser
    def build(self, **kwargs):
        #tabmodule='fooparsetab'
        self.parser = yacc.yacc(module=self, **kwargs, start='INITIAL')

    # Test it output
    def test(self, dict_elementos, data, lexer):
        self.elementos = dict_elementos
        self.lexer = lexer
        self.data = data
        result = self.parser.parse(data, self.lexer)
        self.ast(self.Ast)
        print(self.tree)
        print(json.dumps(result, indent=4, sort_keys=False))
        return self.tree

    def ast(self,nodo):
        if nodo.id == 0:
            nodo.id = self.id_n
            self.id_n += 1
        
        self.tree += '\n \t{}[label="{}"]'.format(nodo.id, nodo.valor)
        for hijo in nodo.hijos:
            self.tree += '\n \t{} -> {}'.format(nodo.id, self.id_n)
            self.ast(hijo)
        
        self.tree += '\n}'
        
        
        
