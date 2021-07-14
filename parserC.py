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
    program : function program
            | external-declaration program
            | empty
    """


def p_external_declaration(p):
    """
    external-declaration : type assignment SEMICOLON
                         | array_usage SEMICOLON
                         | type array_usage SEMICOLON
                         | macro_definition
                         | file_inclusion
    """


def p_declaration(p):
    """
    declaration : type assignment SEMICOLON
                | assignment SEMICOLON
                | function_call SEMICOLON
                | array_usage SEMICOLON
                | type array_usage SEMICOLON
    """


def p_assignment(p):
    """
    assignment : IDENTIFIER ASSIGN assignment
               | IDENTIFIER ASSIGN function_call
               | IDENTIFIER ASSIGN array_usage
               | array_usage ASSIGN assignment
               | IDENTIFIER COMMA assignment
               | INTEGER COMMA assignment
               | IDENTIFIER PLUS assignment
               | IDENTIFIER MINUS assignment
               | IDENTIFIER TIMES assignment
               | IDENTIFIER DIVIDE assignment
               | IDENTIFIER MODULUS assignment
               | INTEGER PLUS assignment
               | INTEGER MINUS assignment
               | INTEGER TIMES assignment
               | INTEGER DIVIDE assignment
               | INTEGER MODULUS assignment
               | APOST assignment APOST
               | LPAREN assignment RPAREN
               | MINUS assignment
               | INTEGER PLUS PLUS
               | IDENTIFIER PLUS PLUS
               | array_usage PLUS PLUS
               | INTEGER MINUS MINUS
               | IDENTIFIER MINUS MINUS
               | array_usage MINUS MINUS
               | BOOLEAN
               | FLOATINGPOINT
               | INTEGER
               | STRING
               | IDENTIFIER
               | LETTER
    """


def p_function_call(p):
    """
    function_call : IDENTIFIER LPAREN RPAREN
                  | IDENTIFIER LPAREN assignment RPAREN
    """


def p_type(p):
    """
    type : INT
         | FLOAT
         | CHAR
         | VOID
    """


def p_array_usage(p):
    """
    array_usage : IDENTIFIER LBRACKET assignment RBRACKET
    """


def p_function(p):
    """
    function : type IDENTIFIER LPAREN argument_list_option RPAREN compound_statement
    argument_list_option : argument_list
                         | empty
    argument_list : argument_list COMMA argument
                  | argument
    argument : type IDENTIFIER
    compound_statement : LBRACE statement_list RBRACE
    statement_list : statement_list statement
                   | empty
    statement : iteration_statement
              | declaration
              | selection_statement
              | return-statement
    """


def p_iteration_statement(p):
    """
    iteration_statement : WHILE LPAREN expression RPAREN compound_statement
                        | WHILE LPAREN expression RPAREN statement
                        | DO compound_statement WHILE LPAREN expression RPAREN SEMICOLON
                        | DO statement WHILE LPAREN expression RPAREN SEMICOLON
    """


def p_selection_statement(p):
    """
    selection_statement : IF LPAREN expression RPAREN compound_statement
                        | IF LPAREN expression RPAREN statement
                        | IF LPAREN expression RPAREN compound_statement ELSE compound_statement
                        | IF LPAREN expression RPAREN compound_statement ELSE statement
                        | IF LPAREN expression RPAREN statement ELSE compound_statement
                        | IF LPAREN expression RPAREN statement ELSE statement
    """


def p_return_statement(p):
    """
    return-statement : RETURN SEMICOLON
                     | RETURN expression SEMICOLON
    """


def p_expression(p):
    """
    expression : expression EQUALS expression
               | expression LESS expression
               | expression GREATER expression
               | expression AND expression
               | expression OR expression
               | NOT expression
               | assignment
               | array_usage
    """


def p_macro_definition(p):
    """
    macro_definition : POUND DEFINE IDENTIFIER assignment
    """


def p_file_inclusion(p):
    """
    file_inclusion : POUND INCLUDE LESS HEADER GREATER
                   | POUND INCLUDE QUOTE HEADER QUOTE
    """

# Error rule for syntax errors


def p_error(p):
    if p is not None:
        reglas.append("Syntax Error")

    else:
        print("Syntax Error!!")
        reglas.append("Syntax Error")  # añade el error a el arreglo

# def p_error(p):
#    if p:
#        print("Syntax error near '%s', line '%s'" % (p.value, p.lineno - 1))


def p_empty(p):
    "empty :"
    pass


# Build the parser
parser = yacc.yacc()

source_code = """
20.5
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
