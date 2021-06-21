import ply.lex as lex

# lista de tokens
tokens = (
    'NUMBERS', 'FLOAT',
    'OPMAS', 'OPMENOS', 'OPMULTIPLICAR', 'OPDIVISOR', 'OPIGUAL',
    'LPAREN', 'RPAREN', 'SEMICOLON', 'CADENA'
)

reserved = {
    'while': 'WHILE',
    'else': 'ELSE',
    'if': 'IF',
    'for': 'FOR',
    'switch': 'SWITCH',
    'case': 'CASE',
    'do': 'DO',
    'break': 'BREAK',
    'return': 'RETURN',
    'int': 'INT',
    'float': 'FLOAT',
    'double': 'DOUBLE',
    'continue': 'CONTINUE',
    'struct': 'STRUCT',
    'union': 'UNION',
    'char': 'CHAR',
    'alignas': 'ALIGNAS',
    'alignof': 'ALIGNOF',
    'and': 'AND',
    'and_eq': 'AND_EQ',
    'asm': 'ASM',
    '__abstract': '__ABSTRACT',
    'delete': 'DELETE',
    'this': 'THIS',
    'auto': 'AUTO',
    'bitand': 'BITAND',
    'constinit': 'CONSTINIT',
    'continue': 'CONTINUE',
    'co_await': 'CO_AWAIT',
    'co_return': 'CO_RETURN',
    'co_yield': 'CO_YIELD',
    'decltype': 'DECLTYPE',
    'default': 'DEFAULT',
    'long': 'LONG',
    'mutable': 'MUTABLE',
    'namespace': 'NAMESPACE',
    'new': 'NEW',
    'noexcept': 'NOEXCEPT',
    'not': 'NOT',
    'static_assert': 'STATIC_ASSERT',
    'static_cast': 'STATIC_CAST',
    'struct': 'STRUCT',
    'switch': 'SWITCH',
    'template': 'TEMPLATE',
    'this': 'THIS',
    'dinamic_cast': 'DINAMIC_CAST',
    'const_cast': 'CONST_CAST',
    'new': 'NEW',
    'return': 'RETURN',
    'noreturn': 'NORETURN',
    'thread_local': 'THREAD_LOCAL',
    'bitor': 'BITOR',
    'bool': 'BOOL',
    'catch': 'CATCH',
    'char8_t': 'CHAR8_T',
    'char16_t': 'CHAR16_T',
    'char32_t': 'CHAR32_T',
    'class': 'CLASS',
    'compl_b': 'COMPL_B',
    'concept': 'CONCEPT',
    'const': 'CONST',
    'const_cast': 'CONST_CAST',
    'consteval': 'CONSTEVAL',
    'constexpr': 'CONTEXPR',
    'delete': 'DELETE',
    'do': 'DO',
    'dynamic_cast': 'DYNAMIC_CAST',
    'enum': 'ENUM',
    'explicit': 'EXPLICIT',
    'export': 'EXPORT',
    'extern': 'EXTERN',
    'false': 'FALSE',
    'goto': 'GOTO',
    'inline': 'INLINE',
    'not_eq': 'NOT_EQ',
    'nullptr': 'NULLPTR',
    'operator': 'OPERATOR',
    'or_eq': 'OR_EQ',
    'private': 'PRIVATE',
    'protected': 'PROTECTED',
    'public': 'PUBLIC',
    'register': 'REGISTER',
    'reinterpret_cast': 'REINTERPRET_CAST',
    'requires': 'REQUIRES',
    'short': 'SHORT',
    'signed': 'SIGNED',
    'sizeof': 'SIZEOF',
    'static': 'STATIC',
    'throw': 'THROW',
    'try': 'TRY',
    'typedef': 'TYPEDEF',
    'typeid': 'TYPEID',
    'typename': 'TYPENAME',
    'union': 'UNION',
    'unsigned': 'UNSIGNED',
    'using': 'USING',
    'virtual': 'VIRTUAL',
    'void': 'VOID',
    'volatile': 'VOLATILE',
    'wchar_t': 'wchar_t',
    'xor': 'XOR',
    'xor_eq': 'XOR_EQ',
    '!': '!',
    '#': '#',
    '%': '%',

}
# Regular expression rules for simple tokens
t_OPMAS = r'\+'
t_OPMENOS = r'-'
t_OPMULTIPLICAR = r'\*'
t_OPDIVISOR = r'/'
t_OPIGUAL = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_OPMODULO = r'%'


def t_NUMBERS(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_FLOAT(t):
    r'(\d*\.\d+)|(\d+\.\d*)'
    t.value = float(t.value)
    return t


def t_CADENA(t):
    r'[A-z]+'
    t.value = str(t.value)
    return t

# Define a rule so we can track line numbers


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
23+2.5;
hola;
 '''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
