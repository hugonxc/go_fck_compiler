import argparse
from getch import getche

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Brainfuck filename")
parser.add_argument("-o", help="Filename to be generated")

args = parser.parse_args()

INPUT_FILENAME = args.filename
OUTPUT_FILENAME = args.o

def initialize(go_file):
    init_string = 'package main\n\nimport "fmt"\n\nfunc main() {\n'
    init_string += '\t//initialize vars\n\ta := make([]int, 1)\n\tvar i = 0\n\t_ = a\n\t_ = i\n\t_ = fmt.Print\n\n'
    init_string += '\t//Brainf_ck code\n'

    go_file.write(init_string)

def compiler():
    bf_file = open(INPUT_FILENAME, 'r')
    go_file = open(OUTPUT_FILENAME, 'w')

    initialize(go_file)

    for line in bf_file:
        for c in line:
            code = convert_bf_go(c)
            go_file.write(code)

    go_file.write("\n}")
    bf_file.close()
    go_file.close()


def convert_bf_go(char):
    code = ''

    if(char == '+'):
        code += '\ta[i]++\n'
    elif(char == "-"):
        code = '\ta[i]--\n'
    elif(char == ">"):
        code = '\ta = append(a,0)\n'
        code += '\ti++\n'
    elif(char == "<"):
        code = '\ti--\n'
    elif(char == '.'):
        code = '\tfmt.Println(string(a[i]))\n'
    elif(char == ','):
        code = '\tfmt.Scanf("%c\\n", &a[i])\n'
    elif(char == '['):
        code ='\tfor ; a[i] != 0; {\n'
    elif(char == ']'):
        code = '\t}\n'

    return code;

compiler()
