
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programrightISEQUALleftANDORleftLESSGREATEREQUALSleftPLUSMINUSleftTIMESDIVIDEAND APOST BOOL BOOLEAN CHAR COMMA COMMENT COMMENTBLOCK DEFINE DIVIDE DO ELSE EOF EQUALS FLOAT FLOATINGPOINT GREATER HEADER IDENTIFIER IF INCLUDE INT INTEGER ISEQUAL LBRACE LBRACKET LESS LETTER LPAREN MINUS MODULUS NOT OR PLUS POUND QUOTE RBRACE RBRACKET RETURN RPAREN SEMICOLON STRING TIMES VOID WHILE\n    program : function program\n            | external-declaration program\n            | empty\n    \n    external-declaration : type assignment SEMICOLON\n                         | array_usage SEMICOLON\n                         | type array_usage SEMICOLON\n                         | macro_definition\n                         | file_inclusion\n    \n    declaration : type assignment SEMICOLON\n                | assignment SEMICOLON\n                | function_call SEMICOLON\n                | array_usage SEMICOLON\n                | type array_usage SEMICOLON\n    \n    assignment : IDENTIFIER EQUALS expression\n                | IDENTIFIER PLUS EQUALS expression\n                | IDENTIFIER MINUS EQUALS expression\n    \n    function_call : IDENTIFIER LPAREN RPAREN\n                  | IDENTIFIER LPAREN expression RPAREN\n                  | IDENTIFIER LPAREN elements RPAREN\n    \n    elements : COMMA expression\n             | COMMA expression elements\n    \n    number : INTEGER\n           | FLOATINGPOINT\n    \n    array_usage : IDENTIFIER LBRACKET elements RBRACKET\n                | IDENTIFIER LBRACKET expression RBRACKET\n    \n    function : type IDENTIFIER LPAREN argument_list_option RPAREN compound_statement\n    argument_list_option : argument_list\n                         | empty\n    argument_list : argument_list COMMA argument\n                  | argument\n    argument : type IDENTIFIER\n    compound_statement : LBRACE statement_list RBRACE\n    statement_list : statement_list statement\n                   | empty\n    statement : iteration_statement\n              | declaration\n              | selection_statement\n              | return-statement\n    \n    iteration_statement : WHILE LPAREN expression RPAREN compound_statement\n                        | WHILE LPAREN expression RPAREN statement\n                        | DO compound_statement WHILE LPAREN expression RPAREN SEMICOLON\n                        | DO statement WHILE LPAREN expression RPAREN SEMICOLON\n    \n    selection_statement : IF LPAREN expression RPAREN compound_statement\n                        | IF LPAREN expression RPAREN statement\n                        | IF LPAREN expression RPAREN compound_statement ELSE compound_statement\n                        | IF LPAREN expression RPAREN compound_statement ELSE statement\n                        | IF LPAREN expression RPAREN statement ELSE compound_statement\n                        | IF LPAREN expression RPAREN statement ELSE statement\n    \n    return-statement : RETURN SEMICOLON\n                     | RETURN expression SEMICOLON\n    \n    conditional_expression : expression ISEQUAL expression\n                           | expression NOT EQUALS expression\n                           | expression LESS expression\n                           | expression LESS EQUALS expression\n                           | expression GREATER expression\n                           | expression GREATER EQUALS expression\n                           | expression AND expression\n                           | expression OR expression\n                           | NOT expression\n    \n    expression : BOOLEAN\n               | number\n               | STRING\n               | IDENTIFIER\n               | LETTER\n               | assignment\n               | array_usage\n               | function_call\n               | math_expression\n               | conditional_expression\n    \n    type : BOOL\n        | INT\n        | FLOAT\n        | CHAR\n        | VOID\n    \n    math_expression : expression PLUS expression\n                    | expression MINUS expression\n                    | expression TIMES expression\n                    | expression DIVIDE expression\n                    | expression MODULUS expression\n                    | expression PLUS PLUS\n                    | expression MINUS MINUS\n    \n    macro_definition : POUND DEFINE IDENTIFIER assignment\n    \n    file_inclusion : POUND INCLUDE LESS HEADER GREATER\n                   | POUND INCLUDE QUOTE HEADER QUOTE\n    empty :'
    
_lr_action_items = {'$end':([0,1,2,3,4,8,9,16,17,22,29,30,31,35,36,37,38,39,40,41,42,43,44,45,55,59,60,73,75,81,82,83,86,87,88,89,90,91,92,93,95,97,99,100,102,103,104,107,108,109,110,111,114,],[-85,0,-85,-85,-3,-7,-8,-1,-2,-5,-4,-6,-63,-60,-61,-62,-64,-65,-66,-67,-68,-69,-22,-23,-14,-24,-25,-59,-82,-15,-16,-17,-75,-80,-76,-81,-77,-78,-79,-51,-53,-55,-57,-58,-83,-84,-26,-18,-19,-52,-54,-56,-32,]),'BOOL':([0,2,3,8,9,22,25,29,30,31,35,36,37,38,39,40,41,42,43,44,45,55,59,60,73,75,80,81,82,83,86,87,88,89,90,91,92,93,95,97,99,100,102,103,104,105,107,108,109,110,111,112,113,114,115,116,117,118,119,121,135,136,137,139,144,145,147,148,151,152,153,156,157,160,161,162,163,164,165,166,167,],[10,10,10,-7,-8,-5,10,-4,-6,-63,-60,-61,-62,-64,-65,-66,-67,-68,-69,-22,-23,-14,-24,-25,-59,-82,10,-15,-16,-17,-75,-80,-76,-81,-77,-78,-79,-51,-53,-55,-57,-58,-83,-84,-26,-85,-18,-19,-52,-54,-56,10,-34,-32,-33,-35,-36,-37,-38,10,-10,-11,-12,-49,-9,-13,-50,10,10,-39,-40,-43,-44,10,10,-41,-42,-45,-46,-48,-47,]),'INT':([0,2,3,8,9,22,25,29,30,31,35,36,37,38,39,40,41,42,43,44,45,55,59,60,73,75,80,81,82,83,86,87,88,89,90,91,92,93,95,97,99,100,102,103,104,105,107,108,109,110,111,112,113,114,115,116,117,118,119,121,135,136,137,139,144,145,147,148,151,152,153,156,157,160,161,162,163,164,165,166,167,],[11,11,11,-7,-8,-5,11,-4,-6,-63,-60,-61,-62,-64,-65,-66,-67,-68,-69,-22,-23,-14,-24,-25,-59,-82,11,-15,-16,-17,-75,-80,-76,-81,-77,-78,-79,-51,-53,-55,-57,-58,-83,-84,-26,-85,-18,-19,-52,-54,-56,11,-34,-32,-33,-35,-36,-37,-38,11,-10,-11,-12,-49,-9,-13,-50,11,11,-39,-40,-43,-44,11,11,-41,-42,-45,-46,-48,-47,]),'FLOAT':([0,2,3,8,9,22,25,29,30,31,35,36,37,38,39,40,41,42,43,44,45,55,59,60,73,75,80,81,82,83,86,87,88,89,90,91,92,93,95,97,99,100,102,103,104,105,107,108,109,110,111,112,113,114,115,116,117,118,119,121,135,136,137,139,144,145,147,148,151,152,153,156,157,160,161,162,163,164,165,166,167,],[12,12,12,-7,-8,-5,12,-4,-6,-63,-60,-61,-62,-64,-65,-66,-67,-68,-69,-22,-23,-14,-24,-25,-59,-82,12,-15,-16,-17,-75,-80,-76,-81,-77,-78,-79,-51,-53,-55,-57,-58,-83,-84,-26,-85,-18,-19,-52,-54,-56,12,-34,-32,-33,-35,-36,-37,-38,12,-10,-11,-12,-49,-9,-13,-50,12,12,-39,-40,-43,-44,12,12,-41,-42,-45,-46,-48,-47,]),'CHAR':([0,2,3,8,9,22,25,29,30,31,35,36,37,38,39,40,41,42,43,44,45,55,59,60,73,75,80,81,82,83,86,87,88,89,90,91,92,93,95,97,99,100,102,103,104,105,107,108,109,110,111,112,113,114,115,116,117,118,119,121,135,136,137,139,144,145,147,148,151,152,153,156,157,160,161,162,163,164,165,166,167,],[13,13,13,-7,-8,-5,13,-4,-6,-63,-60,-61,-62,-64,-65,-66,-67,-68,-69,-22,-23,-14,-24,-25,-59,-82,13,-15,-16,-17,-75,-80,-76,-81,-77,-78,-79,-51,-53,-55,-57,-58,-83,-84,-26,-85,-18,-19,-52,-54,-56,13,-34,-32,-33,-35,-36,-37,-38,13,-10,-11,-12,-49,-9,-13,-50,13,13,-39,-40,-43,-44,13,13,-41,-42,-45,-46,-48,-47,]),'VOID':([0,2,3,8,9,22,25,29,30,31,35,36,37,38,39,40,41,42,43,44,45,55,59,60,73,75,80,81,82,83,86,87,88,89,90,91,92,93,95,97,99,100,102,103,104,105,107,108,109,110,111,112,113,114,115,116,117,118,119,121,135,136,137,139,144,145,147,148,151,152,153,156,157,160,161,162,163,164,165,166,167,],[14,14,14,-7,-8,-5,14,-4,-6,-63,-60,-61,-62,-64,-65,-66,-67,-68,-69,-22,-23,-14,-24,-25,-59,-82,14,-15,-16,-17,-75,-80,-76,-81,-77,-78,-79,-51,-53,-55,-57,-58,-83,-84,-26,-85,-18,-19,-52,-54,-56,14,-34,-32,-33,-35,-36,-37,-38,14,-10,-11,-12,-49,-9,-13,-50,14,14,-39,-40,-43,-44,14,14,-41,-42,-45,-46,-48,-47,]),'IDENTIFIER':([0,2,3,5,8,9,10,11,12,13,14,21,22,23,26,29,30,31,34,35,36,37,38,39,40,41,42,43,44,45,46,47,50,55,56,57,58,59,60,61,62,63,64,65,66,68,69,70,71,73,75,81,82,83,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,104,105,107,108,109,110,111,112,113,114,115,116,117,118,119,121,122,127,129,135,136,137,138,139,144,145,147,148,149,150,151,152,153,156,157,160,161,162,163,164,165,166,167,],[6,6,6,18,-7,-8,-70,-71,-72,-73,-74,31,-5,47,31,-4,-6,-63,31,-60,-61,-62,-64,-65,-66,-67,-68,-69,-22,-23,31,74,78,-14,31,31,31,-24,-25,31,31,31,31,31,31,31,31,31,31,-59,-82,-15,-16,-17,-75,-80,-76,-81,-77,-78,-79,-51,31,-53,31,-55,31,-57,-58,-83,-84,-26,-85,-18,-19,-52,-54,-56,128,-34,-32,-33,-35,-36,-37,-38,128,134,31,31,-10,-11,-12,31,-49,-9,-13,-50,128,31,31,128,-39,-40,-43,-44,128,128,-41,-42,-45,-46,-48,-47,]),'POUND':([0,2,3,8,9,22,29,30,31,35,36,37,38,39,40,41,42,43,44,45,55,59,60,73,75,81,82,83,86,87,88,89,90,91,92,93,95,97,99,100,102,103,104,107,108,109,110,111,114,],[15,15,15,-7,-8,-5,-4,-6,-63,-60,-61,-62,-64,-65,-66,-67,-68,-69,-22,-23,-14,-24,-25,-59,-82,-15,-16,-17,-75,-80,-76,-81,-77,-78,-79,-51,-53,-55,-57,-58,-83,-84,-26,-18,-19,-52,-54,-56,-32,]),'LBRACKET':([6,18,31,128,134,],[21,21,21,21,21,]),'SEMICOLON':([7,19,20,31,35,36,37,38,39,40,41,42,43,44,45,55,59,60,73,81,82,83,86,87,88,89,90,91,92,93,95,97,99,100,107,108,109,110,111,123,124,125,127,132,133,140,158,159,],[22,29,30,-63,-60,-61,-62,-64,-65,-66,-67,-68,-69,-22,-23,-14,-24,-25,-59,-15,-16,-17,-75,-80,-76,-81,-77,-78,-79,-51,-53,-55,-57,-58,-18,-19,-52,-54,-56,135,136,137,139,144,145,147,162,163,]),'DEFINE':([15,],[23,]),'INCLUDE':([15,],[24,]),'LPAREN':([18,31,120,126,128,142,143,],[25,58,129,138,58,149,150,]),'EQUALS':([18,27,28,31,67,68,69,74,128,134,],[26,56,57,26,94,96,98,26,26,26,]),'PLUS':([18,31,33,35,36,37,38,39,40,41,42,43,44,45,55,59,60,61,72,73,74,81,82,83,84,86,87,88,89,90,91,92,93,95,97,99,100,107,108,109,110,111,128,134,140,141,146,154,155,],[27,27,61,-60,-61,-62,-64,-65,-66,-67,-68,-69,-22,-23,61,-24,-25,87,61,61,27,61,61,-17,61,-75,-80,-76,-81,-77,-78,61,61,61,61,61,61,-18,-19,61,61,61,27,27,61,61,61,61,61,]),'MINUS':([18,31,33,35,36,37,38,39,40,41,42,43,44,45,55,59,60,62,72,73,74,81,82,83,84,86,87,88,89,90,91,92,93,95,97,99,100,107,108,109,110,111,128,134,140,141,146,154,155,],[28,28,62,-60,-61,-62,-64,-65,-66,-67,-68,-69,-22,-23,62,-24,-25,89,62,62,28,62,62,-17,62,-75,-80,-76,-81,-77,-78,62,62,62,62,62,62,-18,-19,62,62,62,28,28,62,62,62,62,62,]),'COMMA':([21,31,35,36,37,38,39,40,41,42,43,44,45,52,54,55,58,59,60,72,73,78,81,82,83,86,87,88,89,90,91,92,93,95,97,99,100,106,107,108,109,110,111,],[34,-63,-60,-61,-62,-64,-65,-66,-67,-68,-69,-22,-23,80,-30,-14,34,-24,-25,34,-59,-31,-15,-16,-17,-75,-80,-76,-81,-77,-78,-79,-51,-53,-55,-57,-58,-29,-18,-19,-52,-54,-56,]),'BOOLEAN':([21,26,34,46,56,57,58,61,62,63,64,65,66,68,69,70,71,94,96,98,127,129,138,149,150,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'STRING':([21,26,34,46,56,57,58,61,62,63,64,65,66,68,69,70,71,94,96,98,127,129,138,149,150,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'LETTER':([21,26,34,46,56,57,58,61,62,63,64,65,66,68,69,70,71,94,96,98,127,129,138,149,150,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'INTEGER':([21,26,34,46,56,57,58,61,62,63,64,65,66,68,69,70,71,94,96,98,127,129,138,149,150,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'FLOATINGPOINT':([21,26,34,46,56,57,58,61,62,63,64,65,66,68,69,70,71,94,96,98,127,129,138,149,150,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'NOT':([21,26,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,55,56,57,58,59,60,61,62,63,64,65,66,68,69,70,71,72,73,81,82,83,84,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,107,108,109,110,111,127,129,138,140,141,146,149,150,154,155,],[46,46,-63,67,46,-60,-61,-62,-64,-65,-66,-67,-68,-69,-22,-23,46,-14,46,46,46,-24,-25,46,46,46,46,46,46,46,46,46,46,67,67,-15,-16,-17,67,-75,-80,-76,-81,-77,-78,67,-51,46,-53,46,-55,46,-57,-58,-18,-19,-52,-54,-56,46,46,46,67,67,67,46,46,67,67,]),'LESS':([24,31,33,35,36,37,38,39,40,41,42,43,44,45,55,59,60,72,73,81,82,83,84,86,87,88,89,90,91,92,93,95,97,99,100,107,108,109,110,111,140,141,146,154,155,],[48,-63,68,-60,-61,-62,-64,-65,-66,-67,-68,-69,-22,-23,-14,-24,-25,68,68,-15,-16,-17,68,-75,-80,-76,-81,-77,-78,68,68,-53,-55,68,68,-18,-19,-52,-54,-56,68,68,68,68,68,]),'QUOTE':([24,77,],[49,103,]),'RPAREN':([25,31,35,36,37,38,39,40,41,42,43,44,45,51,52,53,54,55,58,59,60,72,73,78,81,82,83,84,85,86,87,88,89,90,91,92,93,95,97,99,100,101,106,107,108,109,110,111,141,146,154,155,],[-85,-63,-60,-61,-62,-64,-65,-66,-67,-68,-69,-22,-23,79,-27,-28,-30,-14,83,-24,-25,-20,-59,-31,-15,-16,-17,107,108,-75,-80,-76,-81,-77,-78,-79,-51,-53,-55,-57,-58,-21,-29,-18,-19,-52,-54,-56,148,151,158,159,]),'RBRACKET':([31,32,33,35,36,37,38,39,40,41,42,43,44,45,55,59,60,72,73,81,82,83,86,87,88,89,90,91,92,93,95,97,99,100,101,107,108,109,110,111,],[-63,59,60,-60,-61,-62,-64,-65,-66,-67,-68,-69,-22,-23,-14,-24,-25,-20,-59,-15,-16,-17,-75,-80,-76,-81,-77,-78,-79,-51,-53,-55,-57,-58,-21,-18,-19,-52,-54,-56,]),'TIMES':([31,33,35,36,37,38,39,40,41,42,43,44,45,55,59,60,72,73,81,82,83,84,86,87,88,89,90,91,92,93,95,97,99,100,107,108,109,110,111,140,141,146,154,155,],[-63,63,-60,-61,-62,-64,-65,-66,-67,-68,-69,-22,-23,63,-24,-25,63,63,63,63,-17,63,63,-80,63,-81,-77,-78,63,63,63,63,63,63,-18,-19,63,63,63,63,63,63,63,63,]),'DIVIDE':([31,33,35,36,37,38,39,40,41,42,43,44,45,55,59,60,72,73,81,82,83,84,86,87,88,89,90,91,92,93,95,97,99,100,107,108,109,110,111,140,141,146,154,155,],[-63,64,-60,-61,-62,-64,-65,-66,-67,-68,-69,-22,-23,64,-24,-25,64,64,64,64,-17,64,64,-80,64,-81,-77,-78,64,64,64,64,64,64,-18,-19,64,64,64,64,64,64,64,64,]),'MODULUS':([31,33,35,36,37,38,39,40,41,42,43,44,45,55,59,60,72,73,81,82,83,84,86,87,88,89,90,91,92,93,95,97,99,100,107,108,109,110,111,140,141,146,154,155,],[-63,65,-60,-61,-62,-64,-65,-66,-67,-68,-69,-22,-23,-14,-24,-25,65,65,-15,-16,-17,65,-75,-80,-76,-81,-77,-78,65,-51,-53,-55,-57,-58,-18,-19,-52,-54,-56,65,65,65,65,65,]),'ISEQUAL':([31,33,35,36,37,38,39,40,41,42,43,44,45,55,59,60,72,73,81,82,83,84,86,87,88,89,90,91,92,93,95,97,99,100,107,108,109,110,111,140,141,146,154,155,],[-63,66,-60,-61,-62,-64,-65,-66,-67,-68,-69,-22,-23,-14,-24,-25,66,66,-15,-16,-17,66,-75,-80,-76,-81,-77,-78,66,66,-53,-55,-57,-58,-18,-19,-52,-54,-56,66,66,66,66,66,]),'GREATER':([31,33,35,36,37,38,39,40,41,42,43,44,45,55,59,60,72,73,76,81,82,83,84,86,87,88,89,90,91,92,93,95,97,99,100,107,108,109,110,111,140,141,146,154,155,],[-63,69,-60,-61,-62,-64,-65,-66,-67,-68,-69,-22,-23,-14,-24,-25,69,69,102,-15,-16,-17,69,-75,-80,-76,-81,-77,-78,69,69,-53,-55,69,69,-18,-19,-52,-54,-56,69,69,69,69,69,]),'AND':([31,33,35,36,37,38,39,40,41,42,43,44,45,55,59,60,72,73,81,82,83,84,86,87,88,89,90,91,92,93,95,97,99,100,107,108,109,110,111,140,141,146,154,155,],[-63,70,-60,-61,-62,-64,-65,-66,-67,-68,-69,-22,-23,-14,-24,-25,70,70,-15,-16,-17,70,-75,-80,-76,-81,-77,-78,70,70,-53,-55,-57,-58,-18,-19,-52,-54,-56,70,70,70,70,70,]),'OR':([31,33,35,36,37,38,39,40,41,42,43,44,45,55,59,60,72,73,81,82,83,84,86,87,88,89,90,91,92,93,95,97,99,100,107,108,109,110,111,140,141,146,154,155,],[-63,71,-60,-61,-62,-64,-65,-66,-67,-68,-69,-22,-23,-14,-24,-25,71,71,-15,-16,-17,71,-75,-80,-76,-81,-77,-78,71,71,-53,-55,-57,-58,-18,-19,-52,-54,-56,71,71,71,71,71,]),'HEADER':([48,49,],[76,77,]),'LBRACE':([79,121,148,151,160,161,],[105,105,105,105,105,105,]),'RBRACE':([105,112,113,114,115,116,117,118,119,135,136,137,139,144,145,147,152,153,156,157,162,163,164,165,166,167,],[-85,114,-34,-32,-33,-35,-36,-37,-38,-10,-11,-12,-49,-9,-13,-50,-39,-40,-43,-44,-41,-42,-45,-46,-48,-47,]),'WHILE':([105,112,113,114,115,116,117,118,119,121,130,131,135,136,137,139,144,145,147,148,151,152,153,156,157,160,161,162,163,164,165,166,167,],[-85,120,-34,-32,-33,-35,-36,-37,-38,120,142,143,-10,-11,-12,-49,-9,-13,-50,120,120,-39,-40,-43,-44,120,120,-41,-42,-45,-46,-48,-47,]),'DO':([105,112,113,114,115,116,117,118,119,121,135,136,137,139,144,145,147,148,151,152,153,156,157,160,161,162,163,164,165,166,167,],[-85,121,-34,-32,-33,-35,-36,-37,-38,121,-10,-11,-12,-49,-9,-13,-50,121,121,-39,-40,-43,-44,121,121,-41,-42,-45,-46,-48,-47,]),'IF':([105,112,113,114,115,116,117,118,119,121,135,136,137,139,144,145,147,148,151,152,153,156,157,160,161,162,163,164,165,166,167,],[-85,126,-34,-32,-33,-35,-36,-37,-38,126,-10,-11,-12,-49,-9,-13,-50,126,126,-39,-40,-43,-44,126,126,-41,-42,-45,-46,-48,-47,]),'RETURN':([105,112,113,114,115,116,117,118,119,121,135,136,137,139,144,145,147,148,151,152,153,156,157,160,161,162,163,164,165,166,167,],[-85,127,-34,-32,-33,-35,-36,-37,-38,127,-10,-11,-12,-49,-9,-13,-50,127,127,-39,-40,-43,-44,127,127,-41,-42,-45,-46,-48,-47,]),'ELSE':([114,116,117,118,119,135,136,137,139,144,145,147,152,153,156,157,162,163,164,165,166,167,],[-32,-35,-36,-37,-38,-10,-11,-12,-49,-9,-13,-50,-39,-40,160,161,-41,-42,-45,-46,-48,-47,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,2,3,],[1,16,17,]),'function':([0,2,3,],[2,2,2,]),'external-declaration':([0,2,3,],[3,3,3,]),'empty':([0,2,3,25,105,],[4,4,4,53,113,]),'type':([0,2,3,25,80,112,121,148,151,160,161,],[5,5,5,50,50,122,122,122,122,122,122,]),'array_usage':([0,2,3,5,21,26,34,46,56,57,58,61,62,63,64,65,66,68,69,70,71,94,96,98,112,121,122,127,129,138,148,149,150,151,160,161,],[7,7,7,20,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,125,125,133,40,40,40,125,40,40,125,125,125,]),'macro_definition':([0,2,3,],[8,8,8,]),'file_inclusion':([0,2,3,],[9,9,9,]),'assignment':([5,21,26,34,46,47,56,57,58,61,62,63,64,65,66,68,69,70,71,94,96,98,112,121,122,127,129,138,148,149,150,151,160,161,],[19,39,39,39,39,75,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,123,123,132,39,39,39,123,39,39,123,123,123,]),'elements':([21,58,72,],[32,85,101,]),'expression':([21,26,34,46,56,57,58,61,62,63,64,65,66,68,69,70,71,94,96,98,127,129,138,149,150,],[33,55,72,73,81,82,84,86,88,90,91,92,93,95,97,99,100,109,110,111,140,141,146,154,155,]),'number':([21,26,34,46,56,57,58,61,62,63,64,65,66,68,69,70,71,94,96,98,127,129,138,149,150,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'function_call':([21,26,34,46,56,57,58,61,62,63,64,65,66,68,69,70,71,94,96,98,112,121,127,129,138,148,149,150,151,160,161,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,124,124,41,41,41,124,41,41,124,124,124,]),'math_expression':([21,26,34,46,56,57,58,61,62,63,64,65,66,68,69,70,71,94,96,98,127,129,138,149,150,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'conditional_expression':([21,26,34,46,56,57,58,61,62,63,64,65,66,68,69,70,71,94,96,98,127,129,138,149,150,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'argument_list_option':([25,],[51,]),'argument_list':([25,],[52,]),'argument':([25,80,],[54,106,]),'compound_statement':([79,121,148,151,160,161,],[104,130,152,156,164,167,]),'statement_list':([105,],[112,]),'statement':([112,121,148,151,160,161,],[115,131,153,157,165,166,]),'iteration_statement':([112,121,148,151,160,161,],[116,116,116,116,116,116,]),'declaration':([112,121,148,151,160,161,],[117,117,117,117,117,117,]),'selection_statement':([112,121,148,151,160,161,],[118,118,118,118,118,118,]),'return-statement':([112,121,148,151,160,161,],[119,119,119,119,119,119,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> function program','program',2,'p_program','parserC.py',19),
  ('program -> external-declaration program','program',2,'p_program','parserC.py',20),
  ('program -> empty','program',1,'p_program','parserC.py',21),
  ('external-declaration -> type assignment SEMICOLON','external-declaration',3,'p_external_declaration','parserC.py',27),
  ('external-declaration -> array_usage SEMICOLON','external-declaration',2,'p_external_declaration','parserC.py',28),
  ('external-declaration -> type array_usage SEMICOLON','external-declaration',3,'p_external_declaration','parserC.py',29),
  ('external-declaration -> macro_definition','external-declaration',1,'p_external_declaration','parserC.py',30),
  ('external-declaration -> file_inclusion','external-declaration',1,'p_external_declaration','parserC.py',31),
  ('declaration -> type assignment SEMICOLON','declaration',3,'p_declaration','parserC.py',37),
  ('declaration -> assignment SEMICOLON','declaration',2,'p_declaration','parserC.py',38),
  ('declaration -> function_call SEMICOLON','declaration',2,'p_declaration','parserC.py',39),
  ('declaration -> array_usage SEMICOLON','declaration',2,'p_declaration','parserC.py',40),
  ('declaration -> type array_usage SEMICOLON','declaration',3,'p_declaration','parserC.py',41),
  ('assignment -> IDENTIFIER EQUALS expression','assignment',3,'p_assignment','parserC.py',47),
  ('assignment -> IDENTIFIER PLUS EQUALS expression','assignment',4,'p_assignment','parserC.py',48),
  ('assignment -> IDENTIFIER MINUS EQUALS expression','assignment',4,'p_assignment','parserC.py',49),
  ('function_call -> IDENTIFIER LPAREN RPAREN','function_call',3,'p_function_call','parserC.py',55),
  ('function_call -> IDENTIFIER LPAREN expression RPAREN','function_call',4,'p_function_call','parserC.py',56),
  ('function_call -> IDENTIFIER LPAREN elements RPAREN','function_call',4,'p_function_call','parserC.py',57),
  ('elements -> COMMA expression','elements',2,'p_elements','parserC.py',63),
  ('elements -> COMMA expression elements','elements',3,'p_elements','parserC.py',64),
  ('number -> INTEGER','number',1,'p_number','parserC.py',69),
  ('number -> FLOATINGPOINT','number',1,'p_number','parserC.py',70),
  ('array_usage -> IDENTIFIER LBRACKET elements RBRACKET','array_usage',4,'p_array_usage','parserC.py',74),
  ('array_usage -> IDENTIFIER LBRACKET expression RBRACKET','array_usage',4,'p_array_usage','parserC.py',75),
  ('function -> type IDENTIFIER LPAREN argument_list_option RPAREN compound_statement','function',6,'p_function','parserC.py',81),
  ('argument_list_option -> argument_list','argument_list_option',1,'p_function','parserC.py',82),
  ('argument_list_option -> empty','argument_list_option',1,'p_function','parserC.py',83),
  ('argument_list -> argument_list COMMA argument','argument_list',3,'p_function','parserC.py',84),
  ('argument_list -> argument','argument_list',1,'p_function','parserC.py',85),
  ('argument -> type IDENTIFIER','argument',2,'p_function','parserC.py',86),
  ('compound_statement -> LBRACE statement_list RBRACE','compound_statement',3,'p_function','parserC.py',87),
  ('statement_list -> statement_list statement','statement_list',2,'p_function','parserC.py',88),
  ('statement_list -> empty','statement_list',1,'p_function','parserC.py',89),
  ('statement -> iteration_statement','statement',1,'p_function','parserC.py',90),
  ('statement -> declaration','statement',1,'p_function','parserC.py',91),
  ('statement -> selection_statement','statement',1,'p_function','parserC.py',92),
  ('statement -> return-statement','statement',1,'p_function','parserC.py',93),
  ('iteration_statement -> WHILE LPAREN expression RPAREN compound_statement','iteration_statement',5,'p_iteration_statement','parserC.py',99),
  ('iteration_statement -> WHILE LPAREN expression RPAREN statement','iteration_statement',5,'p_iteration_statement','parserC.py',100),
  ('iteration_statement -> DO compound_statement WHILE LPAREN expression RPAREN SEMICOLON','iteration_statement',7,'p_iteration_statement','parserC.py',101),
  ('iteration_statement -> DO statement WHILE LPAREN expression RPAREN SEMICOLON','iteration_statement',7,'p_iteration_statement','parserC.py',102),
  ('selection_statement -> IF LPAREN expression RPAREN compound_statement','selection_statement',5,'p_selection_statement','parserC.py',108),
  ('selection_statement -> IF LPAREN expression RPAREN statement','selection_statement',5,'p_selection_statement','parserC.py',109),
  ('selection_statement -> IF LPAREN expression RPAREN compound_statement ELSE compound_statement','selection_statement',7,'p_selection_statement','parserC.py',110),
  ('selection_statement -> IF LPAREN expression RPAREN compound_statement ELSE statement','selection_statement',7,'p_selection_statement','parserC.py',111),
  ('selection_statement -> IF LPAREN expression RPAREN statement ELSE compound_statement','selection_statement',7,'p_selection_statement','parserC.py',112),
  ('selection_statement -> IF LPAREN expression RPAREN statement ELSE statement','selection_statement',7,'p_selection_statement','parserC.py',113),
  ('return-statement -> RETURN SEMICOLON','return-statement',2,'p_return_statement','parserC.py',119),
  ('return-statement -> RETURN expression SEMICOLON','return-statement',3,'p_return_statement','parserC.py',120),
  ('conditional_expression -> expression ISEQUAL expression','conditional_expression',3,'p_conditional_expression','parserC.py',125),
  ('conditional_expression -> expression NOT EQUALS expression','conditional_expression',4,'p_conditional_expression','parserC.py',126),
  ('conditional_expression -> expression LESS expression','conditional_expression',3,'p_conditional_expression','parserC.py',127),
  ('conditional_expression -> expression LESS EQUALS expression','conditional_expression',4,'p_conditional_expression','parserC.py',128),
  ('conditional_expression -> expression GREATER expression','conditional_expression',3,'p_conditional_expression','parserC.py',129),
  ('conditional_expression -> expression GREATER EQUALS expression','conditional_expression',4,'p_conditional_expression','parserC.py',130),
  ('conditional_expression -> expression AND expression','conditional_expression',3,'p_conditional_expression','parserC.py',131),
  ('conditional_expression -> expression OR expression','conditional_expression',3,'p_conditional_expression','parserC.py',132),
  ('conditional_expression -> NOT expression','conditional_expression',2,'p_conditional_expression','parserC.py',133),
  ('expression -> BOOLEAN','expression',1,'p_expression','parserC.py',138),
  ('expression -> number','expression',1,'p_expression','parserC.py',139),
  ('expression -> STRING','expression',1,'p_expression','parserC.py',140),
  ('expression -> IDENTIFIER','expression',1,'p_expression','parserC.py',141),
  ('expression -> LETTER','expression',1,'p_expression','parserC.py',142),
  ('expression -> assignment','expression',1,'p_expression','parserC.py',143),
  ('expression -> array_usage','expression',1,'p_expression','parserC.py',144),
  ('expression -> function_call','expression',1,'p_expression','parserC.py',145),
  ('expression -> math_expression','expression',1,'p_expression','parserC.py',146),
  ('expression -> conditional_expression','expression',1,'p_expression','parserC.py',147),
  ('type -> BOOL','type',1,'p_type','parserC.py',152),
  ('type -> INT','type',1,'p_type','parserC.py',153),
  ('type -> FLOAT','type',1,'p_type','parserC.py',154),
  ('type -> CHAR','type',1,'p_type','parserC.py',155),
  ('type -> VOID','type',1,'p_type','parserC.py',156),
  ('math_expression -> expression PLUS expression','math_expression',3,'p_math_expression','parserC.py',161),
  ('math_expression -> expression MINUS expression','math_expression',3,'p_math_expression','parserC.py',162),
  ('math_expression -> expression TIMES expression','math_expression',3,'p_math_expression','parserC.py',163),
  ('math_expression -> expression DIVIDE expression','math_expression',3,'p_math_expression','parserC.py',164),
  ('math_expression -> expression MODULUS expression','math_expression',3,'p_math_expression','parserC.py',165),
  ('math_expression -> expression PLUS PLUS','math_expression',3,'p_math_expression','parserC.py',166),
  ('math_expression -> expression MINUS MINUS','math_expression',3,'p_math_expression','parserC.py',167),
  ('macro_definition -> POUND DEFINE IDENTIFIER assignment','macro_definition',4,'p_macro_definition','parserC.py',172),
  ('file_inclusion -> POUND INCLUDE LESS HEADER GREATER','file_inclusion',5,'p_file_inclusion','parserC.py',178),
  ('file_inclusion -> POUND INCLUDE QUOTE HEADER QUOTE','file_inclusion',5,'p_file_inclusion','parserC.py',179),
  ('empty -> <empty>','empty',0,'p_empty','parserC.py',199),
]
