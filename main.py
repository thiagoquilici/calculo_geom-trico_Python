# programa que executa cálculos geométricos

# função
def calcular_retangulo(base, altura):
    area = base * altura
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
opcao = input('Escolha a figura (retângulo, triângulo ou círculo): ')

if opcao == 'retângulo':
    base = float(input('Informe a base do retângulo: '))
    altura = float(input('Informe a altura do retângulo: '))
    print(f'Área do retângulo: {calcular_retangulo(base, altura)}')
elif opcao == 'triângulo':
    base = float(input('Informe a base do triângulo: '))
    altura = float(input('Informe a altura do triângulo: '))
    print(f'Área do triângulo: {calcular_triangulo(base, altura)}')
elif opcao == 'círculo':
    raio = float(input('Informe o raio do círculo: '))
    print(f'Área do círculo: {calcular_circulo(raio)}')
else:
    print('Opção inválida. Escolha entre retângulo, triângulo ou círculo.')