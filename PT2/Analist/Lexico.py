from Analist.Lexema import *
from Analist.Error import *
from Analist.Token import *
from ply import lex as lex
from ply import yacc as yacc
import json


class Lexico(object):

    def __init__(self) -> None:
        self.list_tokens = list()
        self.list_errors = list()
        self.data = ''

    # Reserved words
    reserved = {
        # Function 
        'void': 'METHOD_VOID',
        'return': 'METHOD_RETURN',
        
        # Control flow
        'break': 'BREAK',
        'continue': 'CONTINUE',
        
        # Literals (identifier, integer constant, float constant, string constant, char const)
        'int': 'TYPE_INT',
        'double': 'TYPE_DOUBLE',
        'string': 'TYPE_STRING',
        'char': 'TYPE_CHAR',
        'boolean': 'TYPE_BOOL',
        
        # Conditional structures
        'if': 'CONDITIONAL_IF',
        'else': 'CONDITIONAL_ELSE',
        
        # Iterative structures
        'while': 'ITERATIVE_WHILE',
        'do': 'ITERATIVE_DO',
    }
        
    # List of token names.   This is always required
    # ? Tokens
    tokens = (
        
        # Comments
        'COMENTMULTYLINE', 'COMENTLINE',
        
        # Literals (identifier, integer constant, float constant, string constant, char const)
        'ID',
        
        # Operators (+,-,*,/,%,|,&,~,^,<<,>>, ||, &&, !, <, <=, >, >=, ==, !=)
        'PLUS',  'AND', 'OR', 'NOT', 'MINUS', 'TIMES', 'DIVIDE', 'REST', 'GREATER', 'LESS', 'IQUAL_GREATER', 'IQUAL_LESS', 'IQUALS', 'DIFFERENT', 'COLON',
        
        # Assignment (=, *=, /=, %=, +=, -=, <<=, >>=, &=, ^=, |=)
        'IQUAL',
        
        # Literals Production (integer constant, float constant, string constant, char const)
        'STRING','CHAR','DATA_BOOL','FLOAT','INT',
        
        # Delimeters ( ) [ ] { } , . ; :
        'LPAREN','RPAREN','LKEY','RKEY','DOT_AN_DCOMMA','COMMA',

    ) + tuple(reserved.values())


    # TODO Regular expression rules for simple tokens
    # Operators
    t_IQUALS = r'=='
    t_DIFFERENT = r'!='
    t_IQUAL_GREATER = r'>='
    t_IQUAL_LESS = r'<='
    t_AND = r'&&'
    t_OR = r'\|\|'
    t_NOT = r'!'
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_REST = r'%'
    t_GREATER = r'>'
    t_LESS = r'<'
    
    # Assignment operators
    t_IQUAL = r'='
    
    # Delimeters
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LKEY = r'\{'
    t_RKEY = r'\}'
    t_DOT_AN_DCOMMA = r';'
    t_COMMA = r','
    t_COLON = r':'
    
    # Identifiers
    t_TYPE_INT = r'int'
    t_TYPE_DOUBLE = r'double'
    t_TYPE_STRING = r'string'
    t_TYPE_CHAR = r'char'
    t_TYPE_BOOL = r'boolean'
    t_METHOD_RETURN = r'return'
    t_CONDITIONAL_IF = r'if'
    t_CONDITIONAL_ELSE = r'else'
    t_ITERATIVE_WHILE = r'while'
    t_ITERATIVE_DO = r'do'
    t_METHOD_VOID = r'void'
    t_BREAK = r'break'
    t_CONTINUE = r'continue'
    
    # * A string containing ignored characters (spaces and tabs)
    t_ignore = ' \t'

    # A regular expression rule with some action code
    # Note addition of self parameter since we're in a class

    # * Beginning of the lexical analysis
    
    # Column finder
    def find_column(self,input, token):
        lexema_len = 1
        tamano = f'{token.value}'
        if 'COMENTMULTYLINE' == token.type:
            for num in tamano:
                if '\n' == num:
                    token.lexer.lineno += len('\n')
                    lexema_len = 1
                else:
                    lexema_len += 1
        else:
            for num in tamano:
                lexema_len += 1
        line_start = input.rfind('\n', 0, token.lexpos) + 1
        return (token.lexpos - line_start) + lexema_len
    
    # Syntactic column finder
    def getColumn(self,t):
        line_start = self.data.rfind('\n', 0, t.lexpos) + 1
        return (t.lexpos-line_start)+1

    # INT
    def t_INT(self,t):
        r'\d+'
        t.value = int(t.value)
        return t

    # FLOAT
    def t_FLOAT(self,t):
        r'(\d+)?\.\d+'
        t.value = float(t.value)
        return t

    # DATA_BOOL
    def t_DATA_BOOL(self,t):
        r'true|false'
        t.type = 'DATA_BOOL'
        return t
    
    # ID
    def t_ID(self,t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        reservada = Lexico
        if t.value.lower() in reservada.reserved.keys():
            t.type = reservada.reserved[t.value.lower()]
        return t

    # STRING    
    def t_STRING(self,t):
        r'\"([^\\\n]|(\\.))*?\"'
        t.type = 'STRING'
        return t

    # CHAR
    def t_CHAR(self,t):
        r'\'([^\\\n]|(\\.))?\''
        t.type = 'CHAR'
        return t

    # COMMENT LINE
    def t_COMENTLINE(self,t):
        r'\/\/(.*)'
        t.type = 'COMENTLINE'
        return t

    # COMMENT MULTY LINE
    def t_COMENTMULTYLINE(self,t):
        r'(/\*(.|\n)*?\*/)|(//.*)'
        t.type = 'COMENTMULTYLINE'
        return t

    # Define a rule so we can track line numbers
    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # * Error handling rule
    def t_error(self,t):
        col = self.find_column(self.contenido, t)
        tipo = 'Léxico'
        descripcion = f'No se reconoce el lexema:  {t.value[0]}'
        _error = Error(t.lexer.lineno, col, tipo, descripcion)
        print(t.lexer.lineno, col,
                f"No se pudo reconocer el lexema '{t.value[0]}'")
        self.list_errors.append(_error)
        #print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
    
    # Build the lexer
    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
    
    # * Beginning of the syntactic analysis
    
    # Indicates precedence in the language
    precedence = (
            ('left', 'PLUS', 'MINUS'), # level 12
            ('left', 'TIMES', 'DIVIDE', 'REST'),# level 13
            ('left', 'LPAREN', 'RPAREN'), # level 19
        )
    
    def p_INITIAL(self,p):
        '''
        INITIAL : L_INST 
        '''
        p[0] = p[1]
    
    def p_L_INST(self, p):
        '''
        L_INST : L_INST INTS
               | INTS
        '''
        if len(p) == 3:
            p[0] = p[1]
            p[0].append(p[2])
        else:
            p[0] = [p[1]]
            
    def p_INTS(self, p):
        '''
        INTS : METHOD_VOID ID LPAREN RPAREN LKEY RKEY 
             | METHOD_VOID ID LPAREN L_PARAMS RPAREN LKEY RKEY
        '''
        if len(p) == 7:
            p[0] = {"linea": p.lexer.lineno, "columna": self.getColumn(p.lexer), "metodo": p[1], "id": p[2], "parentesis_A": p[3], "parentesis_C": p[4], "llave_A": p[5], "llave_C": p[6]}
        elif len(p) == 8:
            p[0] = {"Fila": p.lexer.lineno, "columna": self.getColumn(
                p.lexer), "metodo": p[1], "id": p[2], "parentesis_A": p[3], "parametros": p[4], "parentesis_C": p[5], "llave_A": p[6], "llave_C": p[7]}
    
    def p_L_PARAMS(self,p):
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
            
    def p_PARAM(self,p):
        '''
        PARAM : TYPE_INT ID
              | TYPE_STRING ID
        '''
        if len(p) == 3:
             p[0] =  {"tipo dato": p[1], "id": p[2]}

    # def p_EXPRESSIONS(self,p):
    #     '''
    #     EXPRESSIONS : EXPRESSIONS COMMA E
    #                 | E
    #     '''
    #     if len(p)==4:
    #         p[0] = p[1]
    #         const = p[1] + p[2]
    #         p[0].append(const)
    #     else:
    #         p[0] = [p[1]]
    
    # def p_E(self, p):
    #     '''
    #     E : STRING COLON INT
    #     '''
    #     p[0] = {"linea": p.lexer.lineno, "columna": self.getColumn(
    #         p.lexer), "operacion": p[2], "izquierda": p[1], "derecha": p[3]}


    # Error rule for syntax errors
    def p_error(self,p):
        print(p)
        if p:
            print(f"Sintaxis no válida cerca de '{p.value}' ({p.type})")
        else:
            print("Ninguna instrucción válida")
        
    # Build the parser
    def build_S(self, **kwargs):
        #tabmodule='fooparsetab'
        self.parser = yacc.yacc(module=self, **kwargs,start='INITIAL')

    # Test it output
    def test_S(self, data):
        self.data = data
        result = self.parser.parse(data,self.lexer)
        print(json.dumps(result, indent=4, sort_keys=False))
        
    # Test it output
    def test(self,data):
        self.lexer.input(data)
        self.contenido = data
        while True:
            tok = self.lexer.token()
            if not tok: 
                break
            col = self.find_column(data, tok)
            descripcion = self._descriptionsTk(tok.value, tok.type)
            _lexema = Lexema(
                tok.value, descripcion['description'], tok.lineno, col, descripcion['patron'])
            _token = Token(tok.type, _lexema)
            print(tok.lineno, col,
                  f"Token procesado: {tok.type}, Lexema reconocido: {tok.value} ")
            self.list_tokens.append(_token)
        self.dict_elementos = {
            'tokens': self.list_tokens, 'errores': self.list_errors}

    # Find token description and pattern
    def _descriptionsTk(self, patron, _token) -> str:
        descipcion = {
            "==": "Operador de relacion Igualacion",
            "!=": "Operador de relacion Diferenciacion",
            ">=": "Operador de relacion Mayor igual",
            "<=": "Operador de relacion Menor igual",
            "&&": "Operador logico and",
            "||": "Operador logico or",
            "!": "Operador logico not",
            "=": "Operador de asignación",
            "+": "Operador aritmetico suma",
            "-": "Operador aritmetico resta",
            "*": "Operador aritmetico multiplicacion",
            "/": "Operador aritmetico division",
            "%": "Operador aritmetico resto",
            ">": "Operador de relacion Mayor",
            "<": "Operador de relacion Menor",
            "(": "Paréntesis abierto",
            ")": "Paréntesis cerrado",
            "{": "Llave abierta",
            "}": "Llave cerrada",
            ";": "Punto y coma",
            ",": "Operador coma",
            ":": "Operador Dos Puntos",
            "TYPE_INT": "Tipo de dato int",
            "TYPE_DOUBLE": "Tipo de dato double",
            "TYPE_STRING": "Tipo de dato string",
            "TYPE_CHAR": "Tipo de dato char",
            "TYPE_BOOL": "Tipo de dato boolean",
            "METHOD_VOID": "Funcion no retorna valor",
            "METHOD_RETURN": "Retorna un valor",
            "CONDITIONAL_IF": "Estructura condicional if",
            "CONDITIONAL_ELSE": "Estructura condicional else",
            "ITERATIVE_DO": "Estructura iterativa do",
            "ITERATIVE_WHILE": "Estructura iterativa while",
            "INT": "Dato tipo int",
            "FLOAT": "Dato tipo double",
            "COMENTLINE": "Comentario de una Linea",
            "COMENTMULTYLINE": "Comentario multilinea Linea",
            "STRING": "Dato tipo string",
            "CHAR": "Dato tipo char",
            "DATA_BOOL": "Dato tipo boolean",
            "ID": "Simbolo nombre entidad",
            "BREAK": "Terminar el ciclo inmediatamente",
            "CONTINUE": "Omitir una iteración actual de un bucle",
        }

        patrones = {
            "==": "==",
            "!=": "!=",
            ">=": ">=",
            "<=": "<=",
            "&&": "&&",
            "||": "||",
            "!": "!",
            "=": "=",
            "+": "+",
            "-": "-",
            "*": "*",
            "/": "/",
            "%": "%",
            ">": ">",
            "<": "<",
            "(": "(",
            ")": ")",
            "{": "}",
            "}": "{",
            ";": ";",
            ",": ",",
            ":":":",
            "TYPE_INT": "int",
            "TYPE_DOUBLE": "double",
            "TYPE_STRING": "string",
            "TYPE_CHAR": "char",
            "TYPE_BOOL": "boolean",
            "METHOD_VOID": "void",
            "METHOD_RETURN": "return",
            "CONDITIONAL_IF": "if",
            "CONDITIONAL_ELSE": "else",
            "ITERATIVE_DO": "do",
            "ITERATIVE_WHILE": "while",
            "INT": "[+|-]?([0-9]+)",
            "FLOAT": "[+-]?([0-9]*[.])?[0-9]+",
            "COMENTLINE": "//.\*",
            "COMENTMULTYLINE": "\/\*([^\*]|\n)\*\*\/",
            "STRING": "\"([^\"]\|(\"))*\"",
            "CHAR": "'([^']\|(\'))'",
            "DATA_BOOL": "TRUE|FALSE",
            "ID": "^([a-zA-Z_])([\w]*)",
            "BREAK": "break",
            "CONTINUE": "continue"
        }

        dict_contenido = dict()
        for token, description in descipcion.items():
            if patron == token:
                dict_contenido['description'] = description
            elif _token == token:
                dict_contenido['description'] = description

        for token, ptr in patrones.items():
            if patron == token:
                dict_contenido['patron'] = ptr
            elif _token == token:
                dict_contenido['patron'] = ptr

        return dict_contenido
    
    def estructure(self,token):
        pass
