import ply.yacc as yacc
from lexerC import tokens, lexer
reglas = []
success = True

precedence = (
    ("right", "ASSIGN"),
    ("left", "AND", "OR"),
    ("left", "LESS", "GREATER", "EQUALS"),
    ("left", "PLUS", "MINUS"),
    ("left", "TIMES", "DIVIDE"),
)

start = "program"


def p_program(p):
    """
    program : empty
    """



def p_empty(p):
    "empty :"

def p_expression(p):
    """
    expression : literal
    """

def p_math_expression(p):
    """math_expression : literal PLUS literal"""

def p_type(p):
    """
    type : INT
        | CHAR
        | FLOAT
        | BOOL
        | STRING
        | VOID
    """
def literal(p):
    """
    literal : INTEGER
            | FLOATINGPOINT
            | BOOLEAN
            | LETTER
            | STRING
    """

# Build the parser
parser = yacc.yacc()

source_code = """
sa
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
parser.parse(source_code)

if success:
    print("Código Válido")
else:
    print("Código no Válido")

# funcion del analizador


def analizarSintactico(s):
    reglas.clear()  # limpio los errores
    print(s)
    result = str(parser.parse(s))
    print(result)
    return result, reglas