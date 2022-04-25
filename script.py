from shutil import move as move
import sys

def mover(o, d):
    move(o, d)
    print('arquivo movido com sucesso.')

try:
    mover(sys.argv[1], sys.argv[2])
except:
    print('um dos parâmetros foi passado incorretamente.')