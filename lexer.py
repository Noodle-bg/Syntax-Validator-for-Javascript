import ply.lex as lex

# Define tokens
tokens = (
    'VAR', 'LET', 'CONST',
    'IDENTIFIER', 'ASSIGN', 'SEMICOLON',
    'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN','RELATION','RCURLY','LCURLY',
    'IF','ELSE','WHILE','FOR','IN'
)

# Define token regular expressions
t_VAR = r'var'
t_LET = r'let'
t_CONST = r'const'
t_ASSIGN = r'=|\+=|-='
t_SEMICOLON = r';'
t_NUMBER = r'\d+'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_RELATION = r'==|!=|>=|<=|>|<'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCURLY = r'{'
t_RCURLY = r'}'
t_IF = r'if'
t_ELSE = r'else'
t_WHILE=r'while'
t_FOR=r'for'
t_IN=r'in'

# Ignored characters (whitespace and tabs)
t_ignore = ' \t\n'


def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check for reserved words
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
reserved = {
    'let': 'LET',
    'var': 'VAR',
    'const': 'CONST',
    'if':'IF',
    'else':'ELSE',
    'while':'WHILE',
    'for':'FOR',
    'in':'IN'
}
