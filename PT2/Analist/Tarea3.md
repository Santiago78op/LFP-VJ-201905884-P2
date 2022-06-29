
# Tarea  III

## Gramática de JSON

### Alfabeto

### Simbolos Terminales

### Expresiones regulares


| Token         |        Patrón        |
| ------------- | :------------------: |
| OpenKey       |       {              |
| name          | "([^\n]|(.))*?\"     |
| colon         | :                    |
| value         | \[((("([^\n]I(.))*")I\d+I)(,?)*)*\]|
| coma          |       ,              |
| CloseKey      |       }              |


### Símbolos no terminales


| Token         |        Descripción   |
| ------------- | :------------------: |
| JSON          |  Estado inicial de la sintáxis   |
| EXPRESSIONS   | Lista de expresiones clave valor |
| E             | Cualquier expresión              |


### Precedencia 


Precedencia de operadores de más a menos:

| Precedencia   |        Operador      |    Asociatividad    |
| ------------- | :------------------: |:------------------: |
|  18           |  Acceso a arreglo    |    Izquierda        |


### Producciones

```

JSON : OpenKey EXPRESSIONS CloseKey

EXPRESSIONS : EXPRESSIONS coma E
            | E

E : name colon value

```
