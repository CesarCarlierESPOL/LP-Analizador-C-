import ply.lex as lex
reglas = []

# lista de tokens

# Cesar: Aumente tokens faltantes
tokens = [
    "FLOATINGPOINT",
    "INTEGER",
    "BOOLEAN",
    "LETTER",
    "STRING",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "MODULUS",
    "AND",
    "OR",
    "NOT",
    "EQUALS",
    "LESS",
    "GREATER",
    "LPAREN",
    "RPAREN",
    "HEADER",
    "IDENTIFIER",
    "COMMA",
    "SEMICOLON",
    "APOST",
    "QUOTE",
    "LBRACE",
    "RBRACE",
    "LBRACKET",
    "RBRACKET",
    "POUND",
    "COMMENT",
    "COMMENTBLOCK",
    "ISEQUAL",
    "EOF"
]

# Cesar: Reduje numero de palabras reservadas, utilizabamos toda la libreria de C++, que no ibamos a cubrir
reserved = {
    "int": "INT",
    "char": "CHAR",
    "float": "FLOAT",
    "bool": "BOOL",
    "if": "IF",
    "else": "ELSE",
    "do": "DO",
    "while": "WHILE",
    "for": "FOR",
    "return": "RETURN",
    "void": "VOID",
    "define": "DEFINE",
    "include": "INCLUDE",
    "cout": "COUT",
    "cin": "CIN",
    "using": "USING",
    "namespace": "NAMESPACE",
    "struct": "STRUCT"
}

tokens += list(reserved.values())

# Cesar: Ajustando la definicion de tokens para el cambio.
t_PLUS = r"\+"
t_MINUS = r"\-"
t_TIMES = r"\*"
t_DIVIDE = r"\/"
t_MODULUS = r"\%"
t_AND = r"\&\&"
t_OR = r"\|\|"
t_NOT = r"\!"
t_ISEQUAL = r"\=\="
t_LESS = r"\<"
t_GREATER = r"\>"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_COMMA = r"\,"
t_SEMICOLON = r"\;"
t_APOST = r"\'"
t_QUOTE = r"\""
t_LBRACE = r"\{"
t_RBRACE = r"\}"
t_LBRACKET = r"\["
t_RBRACKET = r"\]"
t_POUND = r"\#"
t_EQUALS = r"\="
t_EOF = r"\$"


# Cesar modifique para que esto funcione con los nuevos nombres
def t_COMMENT(t):
    r"\/\/.*"
    return t


def t_COMMENTBLOCK(t):
    r"\/\*(.|\n)*\*\/"
    return t


def t_HEADER(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*\.h"
    return t

def t_BOOLEAN(t):
    r"true|false"
    return t

def t_IDENTIFIER(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    t.type = reserved.get(t.value, "IDENTIFIER")  # Check for reserved words
    return t

def t_FLOATINGPOINT(t):
    r"\d+ \. \d+"
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r"\d+"
    t.value = int(t.value)
    return t

def t_LETTER(t):
    r"\'.\'"
    t.value = t.value.replace("", "")
    return t

def t_STRING(t):
    r"\".*\""
    return t



# Cesar: Regla para definir los numeros de linea
def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


# Regla para espacios y tabs
t_ignore = " \t"

# Regla para errores


def t_error(t):
    print("No es reconocido '%s'" % t.value[0])
    if t is not None:
        reglas.append("Error, no se encontro el token '%s'" % t.value[0])
    else:
        print("Syntax Error!!")
        reglas.append("Syntax Error")  # añade el error a el arreglo
    t.lexer.skip(1)


lexer = lex.lex()


def analizarLexico(data):
    lexer.lineno = 0
    reglas.clear()  # limpio los errores
    lexer.input(data)
    resultados = ""
    while True:
        tok = lexer.token()
        if not tok:
            break
        resultado = str(tok) + "\n"
        resultados = resultados + resultado
    return resultados, reglas

# def tokenize(data):
#    lexer.input(data)
