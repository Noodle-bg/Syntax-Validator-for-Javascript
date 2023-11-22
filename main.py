import ply.yacc as yacc
from lexer import lexer
from parser import parser

data = ""
print("Enter your code (Finish input with 'finish'): ")

while True:
    line = input()
    if line.strip() == "finish":
        break
    data += line + "\n"

lexer.input(data)
parsed = parser.parse(data, lexer=lexer)

if parsed == None:
    print("Accepted")
