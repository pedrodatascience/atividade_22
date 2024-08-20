#importação biblioteca
import cinematica as cn 


while True:
    #mostra menu na tela
    cn.mostrar_menu()

    opcao = input('Opcao do usuário: ')

    match opcao:
        case '1':
            m = float(input('Informa a massa em kg: '.replace(',','.')))
            h = float(input('Informa a altura em metros: '.replace(',', '.')))
            print(f'\nEnergia potencial: {cn.calcular_ep(m, h):,.2f} Joules.\n')
            continue
        
        case '2':
            m = float(input('Informa a massa em kg: '.replace(',', '.')))
            v = float(input('Informa a velocidade em m/s: '.replace(',', '.')))
            print(f'\nEnergia cinética: {cn.calcular_ec(m, v):,.2f} Joules.\n')

        case '3':
            print('Programa encerrado.')
            break
        case _:
            print('\nVocê inseriu número incorreto. \nDigite número de 1 a 3, Por favor!!\n')
            continue

        

