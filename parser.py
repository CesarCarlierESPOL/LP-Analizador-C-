import ply.yacc as yacc
from lexer import tokens, lexer

precedence = (
    ("right", "ASSIGN"),
    ("left", "AND", "OR"),
    ("left", "LESS", "GREATER", "EQUALS"),
    ("left", "PLUS", "MINUS"),
    ("left", "TIMES", "DIVIDE"),
)

start = "program"


def p_macro_definition(p):
    """
    macro_definition : POUND DEFINE ID assignment
    """


def p_file_inclusion(p):
    """
    file_inclusion : POUND INCLUDE LESS HEADER GREATER
                   | POUND INCLUDE QUOTE HEADER QUOTE
    """

# Error rule for syntax errors


def p_error(p):
    if p:
        print("Syntax error near '%s', line '%s'" % (p.value, p.lineno - 1))


def p_empty(p):
    "empty :"
    pass


# Build the parser
parser = yacc.yacc()

source_code = """
# include <stdlib.h>
# define TRUE 1
// comment
int main (int a) {
    if (a =  2) {
    }
}
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
