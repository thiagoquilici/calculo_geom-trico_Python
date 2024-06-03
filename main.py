# programa que executa cálculos geométricos

# função
def calcular_trapezio(base_maior, base_menor, altura):
    area = base_maior + base_menor * altura / 2
    return area


# função
def calcular_triangulo(base, altura):
    area = base * altura / 2
    return area



# função
def calcular_circulo(raio):
    area = 3.14 * raio **2
    return area


# programa principal
opcao = input('Escolha a figura (trapézio, triângulo ou círculo): ')

if opcao == 'trapézio':
    base_maior = float(input('Informe a base maior do trapézio: '))
    base_menor = float(input('Informe a base menor do trapézio: '))
    altura = float(input('Informe a altura do trapézio: '))
    print(f'Área do trapézio: {calcular_trapezio(base_maior, base_menor, altura)}')
elif opcao == 'triângulo':
    base = float(input('Informe a base do triângulo: '))
    altura = float(input('Informe a altura do triângulo: '))
    print(f'Área do triângulo: {calcular_triangulo(base, altura)}')
elif opcao == 'círculo':
    raio = float(input('Informe o raio do círculo: '))
    print(f'Área do círculo: {calcular_circulo(raio)}')
else:
    print('Opção inválida. Escolha entre trapézio, triângulo ou círculo.')