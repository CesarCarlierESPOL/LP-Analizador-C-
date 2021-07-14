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
    assignment : IDENTIFIER EQUALS expression
                | IDENTIFIER PLUS EQUALS expression
                | IDENTIFIER MINUS EQUALS expression
    """

    
def p_function_call(p):
    """
    function_call : IDENTIFIER LPAREN RPAREN
                  | IDENTIFIER LPAREN expression RPAREN
                  | IDENTIFIER LPAREN elements RPAREN
    """


def p_elements(p):
    """
    elements : COMMA expression
             | COMMA expression elements
    """

def p_number(p):
    """
    number : INTEGER
           | FLOATINGPOINT
    """
def p_array_usage(p):
    """
    array_usage : IDENTIFIER LBRACKET elements RBRACKET
                | IDENTIFIER LBRACKET expression RBRACKET
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
               | assignment
               | array_usage
               | function_call
               | math_expression
               | conditional_expression
    """

def p_type(p):
    """
    type : BOOL
        | INT
        | FLOAT
        | CHAR
        | VOID
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
while nextTerm <= n {
        cout << nextTerm << ", ";
        t1 = t2;
        t2 = nextTerm;
        nextTerm = t1 + t2;
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
