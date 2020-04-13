prog: lex.yy.c y.tab.c
	gcc -g lex.yy.c y.tab.c -o prog
lex.yy.c: y.tab.c scanner.l
	lex scanner.l
y.tab.c: yacc.y
	yacc -d yacc.y
clean:
	rm -rf lex.yy.c y.tab.c y.tab.h prog y.output
