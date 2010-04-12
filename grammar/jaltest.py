# bvwelch 23 jan, '10

# this program tests the JAL grammar, and was derived from
# an example found here: http://www.antlr.org/wiki/display/ANTLR3/Example

import sys
import antlr3
import antlr3.tree

# the lexer and parser are generated by Antlr, like this:
#    java -cp antlr-3.1.2.jar org.antlr.Tool jal.g 

from jalLexer import *
from jalParser import *

f = open('a.jal')
char_stream = antlr3.ANTLRInputStream(f)
lexer = jalLexer(char_stream)
tokens = antlr3.CommonTokenStream(lexer)

#print "dumping our lexer tokens"
#for x in tokens.getTokens():
    #print x.getLine(), x.getText()
#print "done with lexer tokens"
#exit(1)

print "setting up parser"
parser = jalParser(tokens)
print "calling parser"
r = parser.program()
print "back from parser"
#exit(1)

# this is the root of the AST
root = r.tree

nodes = antlr3.tree.CommonTreeNodeStream(root)
nodes.setTokenStream(tokens)

print "dumping our parser/tree nodes"
for x in nodes:
    print x.toString()
print "done with parser/tree nodes"

exit()
