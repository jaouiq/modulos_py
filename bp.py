# faz as importações
import os
from modulo import *

# programa principal
if __name__ == '__main__':
    while True:
        print(f'{' '*20}CÁLCULOS{' '*20}\n')
        exibir_menu()
        opcao = input('Opção desejada: ')
        match opcao:
            case '1':
                b = float(input('Base do quadrilátero: '))
                h = float(input('Altura do quadrilátero: '))
                print(f'Área do quadrilátero: {calcular_quadrilatero(b,h)}')
                continue
            case '2':
                r = float(input('Raio do círculo: '))
                print(f'Área do círculo: {calcular_circulo(r)}')
                continue
            case '3':
                b = float(input('Base do triângulo: '))
                h = float (input('Altura do triângulo: '))
                print(f'Área do triângulo: {calcular_triangulo(b, h)}')
                continue
            case '4':
                b_menor = float(input('Base menor do trapézio: '))
                b_maior = float(input('Base maior do trapézio: '))
                h = float(input('Altura do trapézio: '))
                print(f'Área do trapézio: {calcular_trapezio(b_menor, b_maior, h)}')
                continue
            case '5':
                break
