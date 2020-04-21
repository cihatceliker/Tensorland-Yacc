from lex_file import *
from ply import yacc
from actor import Node
import actor

execute_list = []
def reset():
    global execute_list
    execute_list = []


def p_start(p):
    'start : statements'
    p[0] = execute_list


def p_statements(p):
    'statements : statements statement'
    execute_list.extend([p[1], p[2]])


def p_statement(p):
    'statements : statement'
    execute_list.append(p[1])


def p_statement_assign(p):
    '''
    statement : non_block_statement ';'
              | while_statement
              | if_statement
              | try_statement
              | function
              | COMMENT
    '''
    p[0] = p[1]


def p_non_block_statement(p):
    '''
    non_block_statement : assignment
                        | print_stmt
                        | function_call
    '''
    p[0] = p[1]


def p_function(p):
    '''
    function : ID '{' start '}'
    '''
    p[0] = Node(action='func_assign', params=[p[1], *p[3]])


def p_function_call(p):
    '''
    function_call : ID '(' ')'
    '''
    p[0] = Node(action='func', params=[p[1]])


def p_print_statement_exp(p):
    '''
    print_stmt : PRINT '(' expression ')'
    '''
    p[0] = Node(action='print', params=[p[1], p[3]])


def p_assignment(p):
    "assignment : ID '=' expression"
    p[0] = Node(action='assign', params=[p[1], p[3]])



def p_statement_expr(p):
    'statement : expression'
    p[0] = Node(action='get', params=[p[1]])


def p_expression_binop(p):
    '''
    expression : expression '+' primary_expression
               | expression '-' primary_expression
               | expression '/' primary_expression
               | expression '*' primary_expression
               | expression '<' primary_expression
               | expression '>' primary_expression
               | expression '^' primary_expression
               | expression EE  primary_expression
               | expression GTE primary_expression
               | expression LTE primary_expression
    '''
    p[0] = Node(action='binop', params=p[1:])


def p_expression_group(p):
    "expression : '(' expression ')'"
    p[0] = Node(action='get', params=[p[2]])


def p_while_statement(p):
    '''
    while_statement : WHILE expression '{' start '}'
    '''
    p[0] = Node(action='loop', params=[p[2], *p[4]])

def p_if_statement(p):
    '''
    if_statement : IF expression '{' start '}'
    '''
    p[0] = Node(action='if', params=[p[2], *p[4]])


def p_try_statement(p):
    '''
    try_statement : TRY '{' non_block_statement '}' EXCEPT '{' non_block_statement '}'
    '''
    p[0] = Node(action='try', params=[p[3], p[7]])


def p_expression(p):
    "expression : primary_expression"
    p[0] = p[1]


def p_primary_expression_id(p):
    "primary_expression : ID"
    p[0] = Node(action='get', params=[p[1]])


def p_primary_expression_number(p):
    '''
    primary_expression : NUMBER
               | STRING
               | TRUE
               | FALSE
    '''
    p[0] = p[1]


################################
def p_error(p):
    print("syntax error at ", p.value if p else None)

parser = yacc.yacc()

while True:
    try:
        s = input()
    except:
        break
    if not s:
        continue
    for ex in parser.parse(s):
        actor.resolve(ex)
    reset()