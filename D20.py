import random

d4 = random.randint(1, 4)
d6 = random.randint(1, 6)
d8 = random.randint(1, 8)
d10 = random.randint(1, 10)
d12 = random.randint(1, 12)
d20 = random.randint(1, 20)
d100 = random.randint(1, 100)

continuar = 'sim'

while continuar == 'sim':
    rolagem = input('Qual dado quer rolar? (d4, d6, d8, d10, d12, d20, d100) ')

    if rolagem == 'd4':
        print(f'Você tirou {d4}')
    elif rolagem == 'd6':
        print(f'Você tirou {d6}')
    elif rolagem == 'd8':
        print(f'Você tirou {d8}')
    elif rolagem == 'd10':
        print(f'Você tirou {d10}')
    elif rolagem == 'd12':
        print(f'Você tirou {d12}')
    elif rolagem == 'd20':
        print(f'Você tirou {d20}')
    elif rolagem == 'd100':
        print(f'Você tirou {d100}')
    else:
        print('Opção inválida! Por favor, escolha um dado válido.')

    continuar = input('Deseja rolar novamente? (sim ou não) ')

print('Obrigado por jogar!')
