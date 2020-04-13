%{
void yyerror (char *s);
int yylex();
#include <stdio.h>     /* C declarations used in actions */
#include <stdlib.h>
%}

%token COMMENT PRINT EXIT IF ELSE WHILE BREAK TRY RANDOM ADD SUB DIV MULT POW REM DOT
%token EXCEPT OPEN_SCOPE CLOSE_SCOPE RETURN STRING CHAR CONST BOOLEAN OB CB
%token TYPE NUMBER IDENTIFIER LT GT LTE GTE EE OR AND NOT EQ OP CP SCOL COL ST

%start stmts

%%
stmts : stmts stmt | stmt

stmt : non_block_stmt SCOL | block_stmt SCOL | COMMENT

non_block_stmt : return_stmt
        | assignment_stmt 
        | function_call_stmt 
        | print_stmt 
        | BREAK
        | EXIT {exit(EXIT_SUCCESS);}

print_stmt : PRINT expression {/*printf("Printing %d\n", $3);*/}

return_stmt : RETURN expression

assignment_stmt : left_hand_side EQ right_hand_side

left_hand_side : TYPE IDENTIFIER 
        | TYPE CONST IDENTIFIER
        | IDENTIFIER
        | IDENTIFIER tensor_access

right_hand_side : expression
        | function_call_stmt

function_call_stmt : IDENTIFIER parameters

parameters : OP parameter_list CP
        | OP CP

parameter_list : primary_expression COL parameter_list
        | primary_expression

block_stmt : if_stmt 
        | while_stmt 
        | function_decl
        | exception_handling

while_stmt : WHILE expression body

function_decl : TYPE IDENTIFIER parameters body

body : OPEN_SCOPE stmts CLOSE_SCOPE

if_stmt : if_header
        | if_header ELSE body

if_header : IF expression body

exception_handling : TRY body EXCEPT body

expression : OP expression CP 
        | primary_expression
        | expression operators primary_expression

primary_expression : IDENTIFIER
        | CONST IDENTIFIER 
        | primitive_type
        | tensor_decl

tensor_access : OB dimension_list CB

tensor_decl : ST dimension_list ST
        | RANDOM ST dimension_list ST

dimension_list : dimension COL dimension_list
        | dimension

dimension : IDENTIFIER
        | CONST IDENTIFIER
        | NUMBER

operators : ADD | SUB | DIV | MULT | POW | REM | DOT | LT | GT | LTE | GTE | EE | OR | AND | NOT

primitive_type : NUMBER | BOOLEAN | STRING

%%


int main (void) {
	return yyparse();
}

void yyerror (char *s) {fprintf (stderr, "%s\n", s);} 