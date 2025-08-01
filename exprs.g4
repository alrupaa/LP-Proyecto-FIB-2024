grammar exprs;

root : expr     //la etiqueta ya es root
     ;

expr : expr ('*'|'/') expr  #muldiv
     | expr ('+'|'-') expr  #sumres
     | NUM                  #numero
     ;

NUM : [0-9]+;
WS  : [ \t\n\r]+ -> skip;