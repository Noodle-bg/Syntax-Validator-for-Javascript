import ply.yacc as yacc
from lexer import tokens

def p_statements(p):
    '''statements : statement statements
                  | statement'''
def p_statement(p):
    '''
    statement : assignment_statement
              | declaration_statement
              | if_statement
              | while_statement
              | for_in_statement
    '''

def p_assignment_statement(p):
    '''
    assignment_statement : VAR IDENTIFIER ASSIGN expression SEMICOLON
                         | CONST IDENTIFIER ASSIGN expression SEMICOLON
                         | LET IDENTIFIER ASSIGN expression SEMICOLON
                         | IDENTIFIER ASSIGN expression SEMICOLON
                         | IDENTIFIER ASSIGN expression
                         | VAR IDENTIFIER ASSIGN expression
                         | CONST IDENTIFIER ASSIGN expression
                         | LET IDENTIFIER ASSIGN expression
    '''

def p_declaration_statement(p):
    '''
    declaration_statement : VAR IDENTIFIER SEMICOLON
                          | LET IDENTIFIER SEMICOLON
    '''

def p_expression(p):
    '''
    expression : NUMBER
               | IDENTIFIER
               | expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | LPAREN expression RPAREN
    '''

def p_condition(p):
    '''
    condition : expression RELATION expression
              | LPAREN condition RPAREN
    '''

def p_if_statement(p):
    '''
    if_statement : IF LPAREN condition RPAREN LCURLY statements RCURLY
                 | IF LPAREN condition RPAREN statements
                 | IF LPAREN condition RPAREN LCURLY statements RCURLY else_statement
    '''
def p_else_statement(p):
    '''
    else_statement : ELSE LCURLY statements RCURLY
                   | ELSE if_statement
    '''
def p_while_statement(p):
    '''
    while_statement : WHILE LPAREN condition RPAREN LCURLY statements RCURLY
                    | WHILE LPAREN condition RPAREN statements
    '''
def p_for_in_statement(p):
    '''
    for_in_statement : FOR LPAREN LET IDENTIFIER IN IDENTIFIER RPAREN LCURLY statements RCURLY
                     | FOR LPAREN LET IDENTIFIER IN IDENTIFIER RPAREN statements
                     | FOR LPAREN VAR IDENTIFIER IN IDENTIFIER RPAREN LCURLY statements RCURLY
                     | FOR LPAREN VAR IDENTIFIER IN IDENTIFIER RPAREN statements 
                     | FOR LPAREN CONST IDENTIFIER IN IDENTIFIER RPAREN LCURLY statements RCURLY
                     | FOR LPAREN CONST IDENTIFIER IN IDENTIFIER RPAREN statements  
    '''
def p_error(p):
    if p:
        print(f"Syntax error at token '{p.value}'")
    exit(1)

parser = yacc.yacc()
  