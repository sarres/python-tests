# -*- coding:utf-8 -*-
# Autores: Fernando Nitsche Sarres <nandosarres at gmail dot com> & 
#          Ronald Andreu Kaiser <raios.catodicos at gmail dot com>
# Descrição: Imprime triângulos de tamanhos diferentes.


import sys


def imprimir_triangulo(numero):
    for item in range(1, 2*numero, 2):
        print (numero - 1)*' ' + item*'*'
        numero = numero - 1

if len(sys.argv) < 2:
    print "Qual o tamanho do triangulo?"
    exit(-1)

imprimir_triangulo(int(sys.argv[1]))
