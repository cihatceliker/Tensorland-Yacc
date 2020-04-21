tokens = (
    'ID', 'NUMBER', 'PRINT', 'COMMENT', 'TRUE', 'FALSE',
    'STRING', 'WHILE', 'LTE', 'GTE', 'EE', 'IF', 'TRY', 'EXCEPT'
)

literals = ['=', '+', '-', '*', '/', '(', ')', '{', '}', '<', '>', ';', '^', '%']

t_ID = r'§[a-zA-Z_][a-zA-Z0-9_]*'
t_COMMENT = r'>>.*'
t_STRING = r'\".*\"'
t_PRINT = r'print'
t_WHILE = r'while'
t_LTE = r'<='
t_GTE = r'>='
t_EE = r'=='
t_IF = r'if'
t_TRY = r'try'
t_EXCEPT = r'except'

def t_TRUE(t):
    r'true'
    t.value = True
    return t

def t_FALSE(t):
    r'false'
    t.value = False
    return t

def t_NUMBER(t):
    r'[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?'
    t.value = float(t.value)
    return t

t_ignore = ' \t\n'

def t_error(t):
    print("unexpected character '%s' skipped" % t.value)
    t.lexer.skip(1)

from ply import lex
lexer = lex.lex()
