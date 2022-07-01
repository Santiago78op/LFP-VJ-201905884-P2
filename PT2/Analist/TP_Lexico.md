# Grammar Simple

## Tokens
    'STRING',
    'CHAR',
    'IQUALS',
    'DIFFERENT',
    'IQUAL_GREATER',
    'IQUAL_LESS',
    'AND',
    'OR',
    'NOT',
    'IQUAL',
    'PLUS',
    'MINUS',
    'COMENTMULTYLINE',
    'TIMES',
    'COMENTLINE',
    'DIVIDE',
    'REST',
    'GREATER',
    'LESS',
    'LPAREN',
    'RPAREN',
    'LKEY',
    'RKEY',
    'DOT_AN_DCOMMA',
    'COMMA',
    'TYPE_INT',
    'TYPE_DOUBLE',
    'TYPE_STRING',
    'TYPE_CHAR',
    'TYPE_BOOL',
    'METHOD_VOID',
    'METHOD_RETURN',
    'CONDITIONAL_IF',
    'CONDITIONAL_ELSE',
    'ITERATIVE_WHILE',
    'ITERATIVE_DO',
    'DATA_BOOL',
    'FLOAT',
    'INT',
    'ID',
    'BREAK',
    'CONTINUE',

## Lenguaje

```c

// método
void miFuncion ( PARAMETROS, )* {
    sentencia*
    return;

}


int miFuncionDos ( PARAMETROS, )* {
    sentencia*
    return 8;
}
```

## Gramatica

G = {lo, N, T}

- **lo**: LISTA_INSTR
- **T**: Simbolos terminales -> no poducen nada
- **N**: Simbolos no terminales -> producen algo
  
lo = {INITIAL}

N = {INITIAL,L_INST,INTS,METHODS,FUNTIONS,SENTENCES,METHOD,SENTENCES_METHOD,L_PARAMS,FUNTIONS,FUNTION,COUPLER,SENTENCES_FUNTION,SENTENCES_METHOD,SENTENCE_METHOD,DECLARATIONS,ASSIGNMENTS,SENTENCES_IF,SENTENCES_WHILE,CALLS,SENTENCE_FUNTION,SENTENCE,SENTENCE_IF,INSTRUCTIONS,SENTENCE_WHILE,OPTIONS,OPTION,EXPRESSIONS,E,TYPE_DATO,DECLARATION,ASSIGNMENT,PARAM,CALL}

T = {empty,METHOD_VOID,ID,LPAREN,RPAREN,LKEY,RKEY,TYPE_INT,TYPE_DOUBLE,TYPE_STRING,TYPE_CHAR,TYPE_BOOL,COMENTLINE,COMENTMULTYLINE,BREAK,DOT_AN_DCOMMA,CONTINUE,METHOD_RETURN,CONDITIONAL_IF,CONDITIONAL_ELSE,ITERATIVE_WHILE,ITERATIVE_DO,AND,OR,NOT,IQUALS,DIFFERENT,IQUAL_GREATER,IQUAL_LESS,GREATER,LESS,PLUS,MINUS,DIVIDE,REST,INT,FLOAT,STRING,CHAR,DATA_BOOL,COMMA}



### G: Gramatica

``` c++

    // Estado inicial INITIAL

    INITIAL -> L_INST 

    // Lista Instrucciones

    L_INST -> L_INST INTS
            | INTS
            | empty

            //empty
    
    // Instrucción

    INTS -> METHODS
            | FUNTIONS
            | SENTENCES

    // Lista Metodos

    METHODS -> METHODS METHOD
            | METHOD 

    // Estrucutura del metodo

    METHOD -> METHOD_VOID ID LPAREN RPAREN LKEY empty RKEY 
            | METHOD_VOID ID LPAREN RPAREN LKEY SENTENCES_METHOD RKEY
            | METHOD_VOID ID LPAREN L_PARAMS RPAREN LKEY empty RKEY
            | METHOD_VOID ID LPAREN L_PARAMS RPAREN LKEY SENTENCES_METHOD RKEY
    
    // Lista Funciones

    FUNTIONS -> FUNTIONS FUNTION
                | FUNTION 

    // Acople Funcióm

    FUNTION -> TYPE_INT COUPLER
            | TYPE_DOUBLE COUPLER
            | TYPE_STRING COUPLER
            | TYPE_CHAR COUPLER
            | TYPE_BOOL COUPLER
    
    // Estructura Función

    COUPLER -> ID LPAREN RPAREN LKEY empty RKEY 
            | ID LPAREN RPAREN LKEY SENTENCES_FUNTION RKEY
            | ID LPAREN L_PARAMS RPAREN LKEY empty RKEY
            | ID LPAREN L_PARAMS RPAREN LKEY SENTENCES_FUNTION RKEY

    // Metodo

    SENTENCES_METHOD -> SENTENCES_METHOD SENTENCE_METHOD
                        | SENTENCE_METHOD

    // Contenido Metodo

    SENTENCE_METHOD -> DECLARATIONS
                    | ASSIGNMENTS
                    | SENTENCES_IF
                    | SENTENCES_WHILE
                    | COMENTLINE
                    | COMENTMULTYLINE
                    | BREAK DOT_AN_DCOMMA
                    | CONTINUE DOT_AN_DCOMMA
                    | METHOD_RETURN DOT_AN_DCOMMA
                    | ID LPAREN CALLS RPAREN

    // Función

    SENTENCES_FUNTION -> SENTENCES_FUNTION SENTENCE_FUNTION
                        | SENTENCE_FUNTION

    // Contenido Función

    SENTENCE_FUNTION -> DECLARATIONS
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

    // Contenido Block

    SENTENCES -> SENTENCES SENTENCE
                | SENTENCE

    // Block

    SENTENCE -> DECLARATIONS
                | ASSIGNMENTS
                | SENTENCE_IF
                | SENTENCE_WHILE
                | COMENTLINE
                | COMENTMULTYLINE
                | BREAK DOT_AN_DCOMMA
                | CONTINUE DOT_AN_DCOMMA
                | ID LPAREN CALLS RPAREN
    
    // Lista Sentencia if

    SENTENCES_IF -> SENTENCES_IF SENTENCE_IF
                    | SENTENCE_IF

    // Estructura if

    SENTENCE_IF -> CONDITIONAL_IF LPAREN INSTRUCTIONS RPAREN LKEY SENTENCES RKEY
            | CONDITIONAL_IF LPAREN INSTRUCTIONS RPAREN LKEY SENTENCES RKEY CONDITIONAL_ELSE LKEY SENTENCES RKEY
            | CONDITIONAL_IF LPAREN INSTRUCTIONS RPAREN LKEY SENTENCES_FUNTION RKEY
            | CONDITIONAL_IF LPAREN INSTRUCTIONS RPAREN LKEY SENTENCES_FUNTION RKEY CONDITIONAL_ELSE LKEY SENTENCES_FUNTION RKEY
            | CONDITIONAL_IF LPAREN INSTRUCTIONS RPAREN LKEY SENTENCES_METHOD RKEY
            | CONDITIONAL_IF LPAREN INSTRUCTIONS RPAREN LKEY SENTENCES_METHOD RKEY CONDITIONAL_ELSE LKEY SENTENCES_METHOD RKEY
    
    // Lista Sentencia while

    SENTENCES_WHILE -> SENTENCES_WHILE SENTENCE_WHILE
                    | SENTENCE_WHILE

    // Estructura while

    SENTENCE_WHILE -> ITERATIVE_WHILE LPAREN INSTRUCTIONS RPAREN LKEY SENTENCES RKEY
                    | ITERATIVE_DO LKEY SENTENCES RKEY ITERATIVE_WHILE LPAREN INSTRUCTIONS RPAREN DOT_AN_DCOMMA
                    | ITERATIVE_WHILE LPAREN INSTRUCTIONS RPAREN LKEY SENTENCES_FUNTION RKEY
                    | ITERATIVE_DO LKEY SENTENCES_FUNTION RKEY ITERATIVE_WHILE LPAREN INSTRUCTIONS RPAREN DOT_AN_DCOMMA
                    | ITERATIVE_WHILE LPAREN INSTRUCTIONS RPAREN LKEY SENTENCES_METHOD RKEY
                    | ITERATIVE_DO LKEY SENTENCES_METHOD RKEY ITERATIVE_WHILE LPAREN INSTRUCTIONS RPAREN DOT_AN_DCOMMA

    // Operaciones

    INSTRUCTIONS -> INSTRUCTIONS OPTIONS
                    | OPTIONS

    // Opción

    OPTIONS -> OPTIONS AND OPTIONS
            | OPTIONS OR OPTIONS
            | OPTIONS NOT OPTIONS
            | OPTION

    // Estructura Opción

    OPTION -> OPTION IQUALS OPTION
            | OPTION DIFFERENT OPTION
            | OPTION IQUAL_GREATER OPTION
            | OPTION IQUAL_LESS OPTION
            | OPTION GREATER OPTION
            | OPTION LESS OPTION
            | ID
            | EXPRESSIONS
    
    // Lista Opciones Aritmeticas

    EXPRESSIONS -> EXPRESSIONS E
                | E
    
    // Opción Aritmetica

    E -> E PLUS E
        | E MINUS E
        | E TIMES E
        | E DIVIDE E
        | E REST E
        | ID
        | TYPE_DATO
    
    // Lista Declaraciones

    DECLARATIONS -> DECLARATIONS DECLARATION
                    | DECLARATION
    
    // Declaracion

    DECLARATION -> TYPE_INT ID IQUAL INT DOT_AN_DCOMMA
                | TYPE_DOUBLE ID IQUAL FLOAT DOT_AN_DCOMMA
                | TYPE_STRING ID IQUAL STRING DOT_AN_DCOMMA
                | TYPE_CHAR ID IQUAL CHAR DOT_AN_DCOMMA
                | TYPE_BOOL ID IQUAL DATA_BOOL DOT_AN_DCOMMA
    
    // Lista Asignaciones

    ASSIGNMENTS -> ASSIGNMENTS ASSIGNMENT
                | ASSIGNMENT

    // Asignaciones

    ASSIGNMENT -> ID IQUAL INT DOT_AN_DCOMMA
                | ID IQUAL FLOAT DOT_AN_DCOMMA
                | ID IQUAL STRING DOT_AN_DCOMMA
                | ID IQUAL CHAR DOT_AN_DCOMMA
                | ID IQUAL DATA_BOOL DOT_AN_DCOMMA
                | ID IQUAL EXPRESSIONS DOT_AN_DCOMMA
    
    // Lista Parametros

    L_PARAMS -> L_PARAMS COMMA PARAM
                | PARAM

    // Parametro

    PARAM -> TYPE_INT ID
            | TYPE_DOUBLE ID
            | TYPE_STRING ID 
            | TYPE_CHAR ID
            | TYPE_BOOL ID 
    
    // Argumento de funcion o metodo

    CALLS -> CALLS COMMA CALL
            | CALL
    
    // Argumento

    CALL -> TYPE_DATO
            | ID

    // Datos de Tipo 1. string 2. char 3. int 4. float 5. bool

    TYPE_DATO -> STRING | CHAR | INT | FLOAT | DATA_BOOL

    // Contenido Vacio
    empty -> 

```