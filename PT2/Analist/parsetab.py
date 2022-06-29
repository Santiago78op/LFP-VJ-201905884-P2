
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'INITIALleftPLUSMINUSleftTIMESDIVIDERESTleftLPARENRPARENAND BREAK CHAR COLON COMENTLINE COMENTMULTYLINE COMMA CONDITIONAL_ELSE CONDITIONAL_IF CONTINUE DATA_BOOL DIFFERENT DIVIDE DOT_AN_DCOMMA FLOAT GREATER ID INT IQUAL IQUALS IQUAL_GREATER IQUAL_LESS ITERATIVE_DO ITERATIVE_WHILE LESS LKEY LPAREN METHOD_RETURN METHOD_VOID MINUS NOT OR PLUS REST RKEY RPAREN STRING TIMES TYPE_BOOL TYPE_CHAR TYPE_DOUBLE TYPE_INT TYPE_STRING\n        INITIAL : L_INST \n        \n        L_INST : L_INST INTS\n               | INTS\n        \n        INTS : METHOD_VOID ID LPAREN RPAREN LKEY RKEY \n             | METHOD_VOID ID LPAREN L_PARAMS RPAREN LKEY RKEY\n             | METHOD_VOID ID LPAREN L_PARAMS RPAREN LKEY SENTENCES RKEY\n             | SENTENCES\n        \n        SENTENCES : SENTENCES SENTENCE\n                  | SENTENCE\n        \n        SENTENCE : DECLARATIONS\n                  | ASSIGNMENTS\n        \n        DECLARATIONS : DECLARATIONS DECLARATION\n                     | DECLARATION\n        \n        DECLARATION : TYPE_INT ID IQUAL INT DOT_AN_DCOMMA\n                    | TYPE_DOUBLE ID IQUAL FLOAT DOT_AN_DCOMMA\n                    | TYPE_STRING ID IQUAL STRING DOT_AN_DCOMMA\n                    | TYPE_CHAR ID IQUAL CHAR DOT_AN_DCOMMA\n                    | TYPE_BOOL ID IQUAL DATA_BOOL DOT_AN_DCOMMA\n        \n        ASSIGNMENTS : ASSIGNMENTS ASSIGNMENT\n                    | ASSIGNMENT\n        \n        ASSIGNMENT : ID IQUAL INT DOT_AN_DCOMMA\n                   | ID IQUAL FLOAT DOT_AN_DCOMMA\n                   | ID IQUAL STRING DOT_AN_DCOMMA\n                   | ID IQUAL CHAR DOT_AN_DCOMMA\n                   | ID IQUAL DATA_BOOL DOT_AN_DCOMMA\n        \n        L_PARAMS : L_PARAMS COMMA PARAM\n                 | PARAM\n        \n        PARAM : TYPE_INT ID\n              | TYPE_STRING ID\n        '
    
_lr_action_items = {'METHOD_VOID':([0,2,3,6,7,8,9,10,11,17,20,21,22,44,45,46,47,48,59,60,61,62,63,64,67,69,],[4,4,-3,-7,-9,-10,-11,-13,-20,-2,-8,-12,-19,-21,-22,-23,-24,-25,-14,-15,-16,-17,-18,-4,-5,-6,]),'TYPE_INT':([0,2,3,6,7,8,9,10,11,17,20,21,22,28,44,45,46,47,48,56,59,60,61,62,63,64,65,67,68,69,],[12,12,-3,12,-9,12,-11,-13,-20,-2,-8,-12,-19,42,-21,-22,-23,-24,-25,42,-14,-15,-16,-17,-18,-4,12,-5,12,-6,]),'TYPE_DOUBLE':([0,2,3,6,7,8,9,10,11,17,20,21,22,44,45,46,47,48,59,60,61,62,63,64,65,67,68,69,],[13,13,-3,13,-9,13,-11,-13,-20,-2,-8,-12,-19,-21,-22,-23,-24,-25,-14,-15,-16,-17,-18,-4,13,-5,13,-6,]),'TYPE_STRING':([0,2,3,6,7,8,9,10,11,17,20,21,22,28,44,45,46,47,48,56,59,60,61,62,63,64,65,67,68,69,],[14,14,-3,14,-9,14,-11,-13,-20,-2,-8,-12,-19,43,-21,-22,-23,-24,-25,43,-14,-15,-16,-17,-18,-4,14,-5,14,-6,]),'TYPE_CHAR':([0,2,3,6,7,8,9,10,11,17,20,21,22,44,45,46,47,48,59,60,61,62,63,64,65,67,68,69,],[15,15,-3,15,-9,15,-11,-13,-20,-2,-8,-12,-19,-21,-22,-23,-24,-25,-14,-15,-16,-17,-18,-4,15,-5,15,-6,]),'TYPE_BOOL':([0,2,3,6,7,8,9,10,11,17,20,21,22,44,45,46,47,48,59,60,61,62,63,64,65,67,68,69,],[16,16,-3,16,-9,16,-11,-13,-20,-2,-8,-12,-19,-21,-22,-23,-24,-25,-14,-15,-16,-17,-18,-4,16,-5,16,-6,]),'ID':([0,2,3,4,6,7,8,9,10,11,12,13,14,15,16,17,20,21,22,42,43,44,45,46,47,48,59,60,61,62,63,64,65,67,68,69,],[5,5,-3,18,5,-9,-10,5,-13,-20,23,24,25,26,27,-2,-8,-12,-19,57,58,-21,-22,-23,-24,-25,-14,-15,-16,-17,-18,-4,5,-5,5,-6,]),'$end':([1,2,3,6,7,8,9,10,11,17,20,21,22,44,45,46,47,48,59,60,61,62,63,64,67,69,],[0,-1,-3,-7,-9,-10,-11,-13,-20,-2,-8,-12,-19,-21,-22,-23,-24,-25,-14,-15,-16,-17,-18,-4,-5,-6,]),'IQUAL':([5,23,24,25,26,27,],[19,34,35,36,37,38,]),'RKEY':([7,8,9,10,11,20,21,22,44,45,46,47,48,54,59,60,61,62,63,65,68,],[-9,-10,-11,-13,-20,-8,-12,-19,-21,-22,-23,-24,-25,64,-14,-15,-16,-17,-18,67,69,]),'LPAREN':([18,],[28,]),'INT':([19,34,],[29,49,]),'FLOAT':([19,35,],[30,50,]),'STRING':([19,36,],[31,51,]),'CHAR':([19,37,],[32,52,]),'DATA_BOOL':([19,38,],[33,53,]),'RPAREN':([28,40,41,57,58,66,],[39,55,-27,-28,-29,-26,]),'DOT_AN_DCOMMA':([29,30,31,32,33,49,50,51,52,53,],[44,45,46,47,48,59,60,61,62,63,]),'LKEY':([39,55,],[54,65,]),'COMMA':([40,41,57,58,66,],[56,-27,-28,-29,-26,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'INITIAL':([0,],[1,]),'L_INST':([0,],[2,]),'INTS':([0,2,],[3,17,]),'SENTENCES':([0,2,65,],[6,6,68,]),'SENTENCE':([0,2,6,65,68,],[7,7,20,7,20,]),'DECLARATIONS':([0,2,6,65,68,],[8,8,8,8,8,]),'ASSIGNMENTS':([0,2,6,65,68,],[9,9,9,9,9,]),'DECLARATION':([0,2,6,8,65,68,],[10,10,10,21,10,10,]),'ASSIGNMENT':([0,2,6,9,65,68,],[11,11,11,22,11,11,]),'L_PARAMS':([28,],[40,]),'PARAM':([28,56,],[41,66,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> INITIAL","S'",1,None,None,None),
  ('INITIAL -> L_INST','INITIAL',1,'p_INITIAL','Sintactico.py',30),
  ('L_INST -> L_INST INTS','L_INST',2,'p_L_INST','Sintactico.py',36),
  ('L_INST -> INTS','L_INST',1,'p_L_INST','Sintactico.py',37),
  ('INTS -> METHOD_VOID ID LPAREN RPAREN LKEY RKEY','INTS',6,'p_INTS','Sintactico.py',47),
  ('INTS -> METHOD_VOID ID LPAREN L_PARAMS RPAREN LKEY RKEY','INTS',7,'p_INTS','Sintactico.py',48),
  ('INTS -> METHOD_VOID ID LPAREN L_PARAMS RPAREN LKEY SENTENCES RKEY','INTS',8,'p_INTS','Sintactico.py',49),
  ('INTS -> SENTENCES','INTS',1,'p_INTS','Sintactico.py',50),
  ('SENTENCES -> SENTENCES SENTENCE','SENTENCES',2,'p_SENTENCES','Sintactico.py',66),
  ('SENTENCES -> SENTENCE','SENTENCES',1,'p_SENTENCES','Sintactico.py',67),
  ('SENTENCE -> DECLARATIONS','SENTENCE',1,'p_SENTENCE','Sintactico.py',77),
  ('SENTENCE -> ASSIGNMENTS','SENTENCE',1,'p_SENTENCE','Sintactico.py',78),
  ('DECLARATIONS -> DECLARATIONS DECLARATION','DECLARATIONS',2,'p_DECLARATIONS','Sintactico.py',85),
  ('DECLARATIONS -> DECLARATION','DECLARATIONS',1,'p_DECLARATIONS','Sintactico.py',86),
  ('DECLARATION -> TYPE_INT ID IQUAL INT DOT_AN_DCOMMA','DECLARATION',5,'p_DECLARATION','Sintactico.py',96),
  ('DECLARATION -> TYPE_DOUBLE ID IQUAL FLOAT DOT_AN_DCOMMA','DECLARATION',5,'p_DECLARATION','Sintactico.py',97),
  ('DECLARATION -> TYPE_STRING ID IQUAL STRING DOT_AN_DCOMMA','DECLARATION',5,'p_DECLARATION','Sintactico.py',98),
  ('DECLARATION -> TYPE_CHAR ID IQUAL CHAR DOT_AN_DCOMMA','DECLARATION',5,'p_DECLARATION','Sintactico.py',99),
  ('DECLARATION -> TYPE_BOOL ID IQUAL DATA_BOOL DOT_AN_DCOMMA','DECLARATION',5,'p_DECLARATION','Sintactico.py',100),
  ('ASSIGNMENTS -> ASSIGNMENTS ASSIGNMENT','ASSIGNMENTS',2,'p_ASSIGNMENTS','Sintactico.py',107),
  ('ASSIGNMENTS -> ASSIGNMENT','ASSIGNMENTS',1,'p_ASSIGNMENTS','Sintactico.py',108),
  ('ASSIGNMENT -> ID IQUAL INT DOT_AN_DCOMMA','ASSIGNMENT',4,'p_ASSIGNMENT','Sintactico.py',118),
  ('ASSIGNMENT -> ID IQUAL FLOAT DOT_AN_DCOMMA','ASSIGNMENT',4,'p_ASSIGNMENT','Sintactico.py',119),
  ('ASSIGNMENT -> ID IQUAL STRING DOT_AN_DCOMMA','ASSIGNMENT',4,'p_ASSIGNMENT','Sintactico.py',120),
  ('ASSIGNMENT -> ID IQUAL CHAR DOT_AN_DCOMMA','ASSIGNMENT',4,'p_ASSIGNMENT','Sintactico.py',121),
  ('ASSIGNMENT -> ID IQUAL DATA_BOOL DOT_AN_DCOMMA','ASSIGNMENT',4,'p_ASSIGNMENT','Sintactico.py',122),
  ('L_PARAMS -> L_PARAMS COMMA PARAM','L_PARAMS',3,'p_L_PARAMS','Sintactico.py',129),
  ('L_PARAMS -> PARAM','L_PARAMS',1,'p_L_PARAMS','Sintactico.py',130),
  ('PARAM -> TYPE_INT ID','PARAM',2,'p_PARAM','Sintactico.py',141),
  ('PARAM -> TYPE_STRING ID','PARAM',2,'p_PARAM','Sintactico.py',142),
]
