import ply.yacc as yacc
from lexerC import tokens, lexer
reglas = []
success = True

precedence = (
    ("right", "ISEQUAL"),
    ("left", "AND", "OR"),
    ("left", "LESS", "GREATER", "EQUALS"),
    ("left", "PLUS", "MINUS"),
    ("left", "TIMES", "DIVIDE"),
)

start = "iteration_statement"

def p_iteration_statement(p):
    """
    iteration_statement : WHILE LPAREN STRING RPAREN
    """




def p_number(p):
    """
    number : INTEGER
           | FLOATINGPOINT
    """






def p_conditional_expression(p):
    """
    conditional_expression : expression ISEQUAL expression
                           | expression NOT EQUALS expression
                           | expression LESS expression
                           | expression LESS EQUALS expression
                           | expression GREATER expression
                           | expression GREATER EQUALS expression
                           | expression AND expression
                           | expression OR expression
                           | NOT expression
    """

def p_expression(p):
    """
    expression : BOOLEAN
               | number
               | STRING
               | IDENTIFIER
               | LETTER
               | math_expression
               | conditional_expression
    """

def p_math_expression(p):
    """
    math_expression : expression PLUS expression
                    | expression MINUS expression
                    | expression TIMES expression
                    | expression DIVIDE expression
                    | expression MODULUS expression
                    | expression PLUS PLUS
                    | expression MINUS MINUS
    """

# Error rule for syntax errors




def p_error(p):
   if p:
       print("Syntax error near '%s', line '%s'" % (p.value, p.lineno - 1))




# Build the parser
parser = yacc.yacc()

source_code = """
while hola
    
"""

lexer.input(source_code)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)

print("\n")

lexer.lineno = 0

# Parse
resultado = parser.parse(source_code)

print (resultado)

# funcion del analizador


def analizarSintactico(s):
    reglas.clear()  # limpio los errores
    print(s)
    result = str(parser.parse(s))
    print(result)
    return result, reglas
