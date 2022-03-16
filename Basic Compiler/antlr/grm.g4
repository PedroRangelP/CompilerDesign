grammar grm;

program : expression+statement*;

expression:
  expression '+' expression #add
  | expression '*' expression #multiply
  | expression '/' expression #divide
  | expression '-' expression #substract
  | expression '<' expression #less
  | expression '>' expression #more
  | Number #number
  | Variable #variable
  ;

statement:
  'int' Variable #declaration
  | Variable '=' expression #assignation
  | 'if(' expression ')' (expression | statement) 'else' (expression | statement) #ifelse
  | 'print(' expression ')' #print
  ;

Number : [0-9]+;
Variable : [a-z]+;
WS : [ \t\n\r]+ -> skip ;