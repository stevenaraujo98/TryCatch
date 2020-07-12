import ply.yacc as sintaxis
import lexico
tokens = lexico.tokens

def p_sentencias(p):
    '''sentencias : asignacion
    | imprimir
    | declaracion
    | iter SEMICOLON
    | if
    | while
    | for
    | condicion'''

def p_imprimir(p):
    'imprimir : CONSOLE WRITELINE LPAREN valor RPAREN SEMICOLON'

"""
def p_metodos(p):
    '''metodos : CONTAINS
        | REPLACE
        | ADD
        | REMOVE
        | ITEM
        | SUBSTRING
        | CONSOLE READLINE'''
"""
def p_valor(p):
    '''valor : TRUE
        | FALSE
        | SSTRING
        | DSTRING
        | NEW coleccion LESS tipo GREATER LPAREN RPAREN
        | tupla
        | expresion'''
    
def p_if(p):
    '''if : IF LPAREN condicion RPAREN LLLAVE sentencias RLLAVE
    | IF LPAREN condicion LPAREN LLLAVE sentencias RLLAVE else'''

def p_tupla(p):
   'tupla : LPAREN contenido  RPAREN'

def p_contenido(p):
    'contenido : valor'

def p_contenido_item(p):
    'contenido : ID DOTS valor'
    
def p_contenido_coma(p):
    'contenido : contenido COMMA contenido'

def p_for(p):
    'for : FOR LPAREN inicio SEMICOLON condicion SEMICOLON iter RPAREN LLLAVE sentencias RLLAVE '

def p_ini_for(p):
    '''inicio : ID
        | factor
    '''

def p_iter(p):
    '''iter : incremento
        | decremento
    '''

def p_incremento(p):
    '''incremento : INCRE ID
        | ID INCRE
        | ID PLUS TOASSIGN term
    '''
def p_decremento(p):
    '''decremento : DECRE ID
        | ID DECRE
        | ID MINUS TOASSIGN term
    '''

def p_while(p):
    'while : WHILE LPAREN condicion RPAREN LLLAVE sentencias RLLAVE '

def p_else(p):
    'else : ELSE LLLAVE sentencias RLLAVE'

def p_declaracion(p):
    'declaracion : coleccion LESS tipo GREATER asignacion'
def p_declaracion(p):
    'declaracion : tipo ID SEMICOLON'
def p_declaracion_ini(p):
    'declaracion : tipo asignacion'

def p_coleccion(p):
    ''' coleccion : LIST
        | HASHSET
    '''
def p_tipo(p):
    '''tipo : VAR
        | BOOL
        | FLOAT
        | INT
        | STRING
    '''

def p_asignacion(p):
    'asignacion : ID TOASSIGN valor SEMICOLON'
def p_expresion_suma(p):
    'expresion : expresion PLUS expresion'
def p_expresion_resta(p):
    'expresion : expresion MINUS expresion'
def p_expresion_producto(p):
    'expresion : expresion BY expresion'
def p_expresion_division(p):
    'expresion : expresion DIV expresion'
def p_expresion_iter(p):
    'expresion : iter'
def p_expression_term(p):
    'expresion : term'

def p_expression_paren(p):
    'expresion : LPAREN expresion RPAREN'
def p_compare(p):
    '''compare : LESS
        | GREATER
        | DEQUALS
        | NOTEQUALS
        | GREATEREQUALS
        | LESSEQUAL'''
def p_condicion(p):
    '''condicion : expresion compare expresion
        | TRUE
        | FALSE
    '''
def p_condicion_oper(p):
    '''condicion : NOT condicion
        | condicion AND condicion
        | condicion OR condicion
        | LPAREN condicion RPAREN
    '''

def p_term_factor(p):
    '''term : INTEGER
        | DECIMAL
        | ID
    '''

def p_float(p):
    'factor : FLOAT ID TOASSIGN DECIMAL'
def p_entero(p):
    'factor : INT ID TOASSIGN INTEGER'
def p_var(p):
    '''factor : VAR ID TOASSIGN INTEGER
        | VAR ID TOASSIGN DECIMAL
    '''

# Error generado
def p_error(p):
    print(p)
    print("Error de sintaxis:")
# Construir parser

parser = sintaxis.yacc()

while True:
    try:
        s = input('<c#>')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)