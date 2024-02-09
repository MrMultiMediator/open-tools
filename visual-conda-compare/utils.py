import math
import sys

def write_top(filename, n_envs):
    with open(filename, 'w') as g:
        g.write('<!doctype html>\n<html>\n<head>\n')
        g.write('<meta name="viewport" content="width=device-width, initial-scale=1">\n')
        g.write('<style>\n* {\n  box-sizing: border-box;\n}\n\n')
        g.write('.row {\n    display: flex;\n}\n\n')
        g.write('.column {\n    flex: ')
        g.write(f'{math.floor(100/n_envs)}%;\n')
        g.write('    padding: 10px;\n}\n')
        g.write('</style>\n</head>\n<body>\n<div class="row">\n')

def write_bottom(filename):
    with open(filename, 'a') as g:
        g.write('</div>\n</body>\n</html>\n')

if __name__ == '__main__':
    write_top(sys.argv[1], int(sys.argv[2]))