%{
#include "y.tab.h"
void yyerror (char *s);
int yylex();
%}

BOOLEAN true|false
VOID void
TYPE num|bool|string|char|tensor
COMMENT >>.*[.*\n]*
NUMBER [-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?
IDENTIFIER [a-zA-Z][a-zA-Z_0-9]*

%%
{COMMENT} {return COMMENT;}

print {return PRINT;}
exit {return EXIT;}

if {return IF;}
else {return ELSE;}
while {return WHILE;}
break {return BREAK;}
try {return TRY;}
except {return EXCEPT;}
do {return OPEN_SCOPE;}
stop {return CLOSE_SCOPE;}
return {return RETURN;}
random {return RANDOM;}

or {return OR;}
and {return AND;}
not {return NOT;}
\+ {return ADD;}
\- {return SUB;}
\/ {return DIV;}
\* {return MULT;}
\^ {return POW;}
\% {return REM;}
\@ {return DOT;}
\, {return COL;}
\; {return SCOL;}
\( {return OP;}
\) {return CP;}
\= {return EQ;}
\< {return LT;}
\> {return GT;}
\<\= {return LTE;}
\>\= {return GTE;}
\=\= {return EE;}
\| {return ST;}
\[ {return OB;}
\] {return CB;}
\".*\" {return STRING;}
\'.*\' {return CHAR;}
\§ {return CONST;}
{BOOLEAN} {return BOOLEAN;}
{TYPE} {return TYPE;}
{NUMBER} {return NUMBER;}
{IDENTIFIER} {return IDENTIFIER;}

[ \n] {;}
[ \r\t]+ {;}
. {ECHO; yyerror ("unexpected character");}
%%
int yywrap (void) {return 1;}

