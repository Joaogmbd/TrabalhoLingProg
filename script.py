from shutil import move as move
import sys

def mover(o, d):
    move(o, d)

try:
    mover(sys.argv[1], sys.argv[2])
    print('O arquivo movido com sucesso.')
except:
    print('Um dos parâmetros foi passado incorretamente.')
