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

// función
int miFuncionDos ( PARAMETROS, )* {
    sentencia*
    return hola;
}

               
```

## Gramatica

G = {lo, N, T, G}

- **lo**: LISTA_INSTR
- **N**: Simbolos terminales -> no poducen nada
- **T**: Simbolos no terminales -> producen algo
  
lo = {block}

N = {block,instr,parametro,sentencia,finaliza,type_decl,dato_assign,println,type_dato,dato_type}

T = {}

### G: Gramatica

``` c++

    // Estado inicial INITIAL

    INITIAL -> L_INST 

    // Lista Instrucciones

    L_INST -> L_INST INTS
            | INTS

            //empty
    
    // Funcion sin parametros
    INTS -> void id lparen rparen lkey rkey 
          | void id lparen L_PARAMETROS rparen lkey rkey
          | void id lparen L_PARAMETROS rparen lkey 
          SENTENCES rkey

    SENTENCES -> 

    L_PARAMETROS -> L_PARAMETROS dot_and_comma TYPE_DATO id
                  | TYPE_DATO id

    DATOS -> 
                  

    LISTA_SENTENCIAS ->  LISTA_SENTENCIAS SENTENCIAS 
                | SENTENCIAS;

    SENTENCIAS -> SENTENCIA_DA;

    // Tipos de sentencia_D_A  1. decaracion 2. asiganacion 3. impresion

    sentencia_D_A -> type_decl | dato_assign;
    
    type_decl -> type_dato ID IQUAL dato_type DOT_AN_DCOMMA;

    dato_assign -> ID IQUAL dato_type DOT_AN_DCOMMA;
    
    println -> println dato_type DOT_AN_DCOMMA;

    // Tipos de Dato 1. string 2. char 3. int 4. float 5. bool

    type_dato -> TYPE_STRING | TYPE_CHAR | TYPE_INT | TYPE_DOUBLE | TYPE_BOOL;

    // Datos de Tipo 1. string 2. char 3. int 4. float 5. bool

    dato_type -> STRING | CHAR | INT | FLOAT | DATA_BOOL;

```