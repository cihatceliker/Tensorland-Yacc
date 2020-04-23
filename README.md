# Tensorland-Yacc

Member : Cihat Emre Çeliker - 20160808028

## Updated Name : tlang

## Explanation of the Syntax

On the lex part of the project, the syntax was very fancy since we only needed to analyze tokens, but now, since we need the functionality, anything that can be discarded is discarded.

Scopes starts with 'do' and ends with 'stop'. Only the non-block statements needed to end with semicolon to distinguish to allow writing multiple statements on the same line. Functions don't take parameters. The general syntax is pretty standard. 

Every variable starts with '§'. In my case, it's Alt+S. The idea behind this choice was to able to see every defined identifier when '§' typed. Most of the IDE's have this feature.

If I were to write this in the standard Lex-Yacc, I would need couple hundred extra lines just to be able to keep the variables in a hash table, so I would just make the variables defined as chars and keep them on an array with the size of 26 or 52.

Using Python Lex-Yacc allowed me to focus more on the relevant part to the course.  

[Link to the Python Lex-Yacc project](https://github.com/dabeaz/ply)

If you have Python 3.6 or greater, it can be install easily using this:
```
pip install ply
```
You can run the program with a statement by statement execution if you don't specify an input file:
```bash
python yacc_file.py
```
You can test the while loop in a statement by statement execution mode, using following:
```
§i = 0;
while (§i < 10) do §i = §i + 1; print(§i); stop
```
Using this, you can see the output of the example program:
```bash
python yacc_file.py < input.tn
```
The example program finds the nth fibonacci number. The output of the example program(input tn file) is:
```
5.0625
True
"dividing by zero"
3.54224848179262e+20
"its a big number"
```

## Updated Grammar
```
start : statements

statements : statements statement
           | statement

statement : non_block_statement ';'
          | while_statement
          | if_statement
          | try_statement
          | function
          | COMMENT
          | expression

non_block_statement : assignment
                    | print_stmt
                    | function_call

function : ID 'do' start 'stop'

function_call : ID '()'

print_stmt : 'print' '(' expression ')'

assignment : ID '=' expression

expression : expression '+' primary_expression
           | expression '-' primary_expression
           | expression '/' primary_expression
           | expression '*' primary_expression
           | expression '<' primary_expression
           | expression '>' primary_expression
           | expression '^' primary_expression
           | expression '==' primary_expression
           | expression '>=' primary_expression
           | expression '<=' primary_expression
           | primary_expression
           | '(' expression ')'

while_statement : 'while' expression 'do' start 'stop'

if_statement : 'if' expression 'do' start 'stop'

try_statement : 'try' 'do' non_block_statement 'stop' 'except' 'do' non_block_statement 'stop'

primary_expression : ID
                   | NUMBER
                   | STRING
                   | 'true'
                   | 'false'

NUMBER  : [-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?
ID      : §[a-zA-Z_][a-zA-Z0-9_]*
COMMENT : >>.*
STRING  : \".*\"
```