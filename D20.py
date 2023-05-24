from random import randint

continuar = 'sim'

while continuar == 'sim':
    rolagem = input('Qual dado quer rolar? (d4, d6, d8, d10, d12, d20, d100) ')

    if rolagem == 'd4':
        d4 = randint(1, 4)
        print(f'Você tirou {d4}')
    elif rolagem == 'd6':
        d6 = randint(1, 6)
        print(f'Você tirou {d6}')
    elif rolagem == 'd8':
        d8 = randint(1, 8)
        print(f'Você tirou {d8}')
    elif rolagem == 'd10':
        d10 = randint(1, 10)
        print(f'Você tirou {d10}')
    elif rolagem == 'd12':
        d12 = randint(1, 12)
        print(f'Você tirou {d12}')
    elif rolagem == 'd20':
        d20 = randint(1, 20)
        print(f'Você tirou {d20}')
    elif rolagem == 'd100':
        d100 = randint(1, 100)
        print(f'Você tirou {d100}')
    else:
        print('Opção inválida! Por favor, escolha um dado válido.')

    continuar = input('Deseja rolar novamente? (sim ou não) ')

print('Obrigado por jogar!')
