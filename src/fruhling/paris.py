'''
Created on 12/10/2016

@author: ernesto

https://www.hackerrank.com/contests/master/challenges/sparse-arrays?h_r=internal-search

'''
import logging
import sys

logger_cagada = None
nivel_log = logging.ERROR
#nivel_log = logging.DEBUG

class NodoTrie(object):
    VALOR_MINIMO = ord("A")
    VALOR_MAXIMO = ord("z")
    def __init__(self, caracter):
        self.caracter = caracter
        
        self.contador_palabra_completa = 0
        self.nodos = [None for _ in range(NodoTrie.VALOR_MINIMO, NodoTrie.VALOR_MAXIMO + 1)]
        
def mierda_esparcida_anadir_cacadena(raiz, cadena):
    nodo_actual = raiz
    for idx_car, caracter in enumerate(cadena):
        valor_car = ord(caracter) - NodoTrie.VALOR_MINIMO
        nodo_sig = nodo_actual.nodos[valor_car]
        if(not nodo_sig):
            nodo_sig = nodo_actual.nodos[valor_car] = NodoTrie(valor_car)
        
#        if(idx_car == len(cadena) - 1):
#            nodo_sig.contador_palabra_completa += 1
        nodo_actual = nodo_sig
    
    nodo_actual.contador_palabra_completa += 1

def mierda_esparcida_buscacadena(raiz, cadena):
    nodo_actual = raiz
    for idx_car, caracter in enumerate(cadena):
        valor_car = ord(caracter) - NodoTrie.VALOR_MINIMO
        nodo_sig = nodo_actual.nodos[valor_car]
        if(not nodo_sig):
            return 0
        nodo_actual = nodo_sig
    
    return nodo_actual.contador_palabra_completa
    
def mierda_esparcida_main():
    raiz_trie = NodoTrie(0)
    linea = sys.stdin.readline()
    num_cad = int(linea)
    
    for _ in range(0, num_cad):
        cadenita = sys.stdin.readline().strip()
        logger_cagada.debug("anadiendo %s al trie" % cadenita)
        mierda_esparcida_anadir_cacadena(raiz_trie, cadenita)
        
    linea = sys.stdin.readline()
    num_queries = int(linea)
    
    for _ in range(0, num_queries):
        cadenita = sys.stdin.readline().strip()
        logger_cagada.debug("buscando %s en el trie" % cadenita)
        conta_caca = mierda_esparcida_buscacadena(raiz_trie, cadenita)
        logger_cagada.debug("se encontro %u veces" % conta_caca)
        print("%u" % conta_caca)
        

if __name__ == '__main__':
    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
    logging.basicConfig(level=nivel_log, format=FORMAT)
    logger_cagada = logging.getLogger("asa")
    logger_cagada.setLevel(nivel_log)
    
    mierda_esparcida_main()
