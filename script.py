from shutil import move as move
import sys

def mover(o, d):
    move(o, d)

try:
    mover(sys.argv[1], sys.argv[2])
    print('O arquivo foi movido com sucesso.')
except:
    print('Um ou todos os parâmetros foram passados incorretamente.')
