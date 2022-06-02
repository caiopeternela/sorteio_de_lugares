import random

def sorteio_de_lugares():
    nome = ['Ana Carolina', 'Ana Clara', 'Beatriz', 
                'Breno', 'Bruna', 'Cainã', 'Caio', 'Clara', 
                'Daniel Alves', 'Daniel Dantas', 'David', 
                'Edinaildo', 'Eliel', 'Evandro', 'Fabricio', 
                'Felipe', 'Fernanda', 'Gabriel', 'Gabriela', 
                'Gislane', 'Glória', 'Ingrid', 'João', 'Laura', 
                'Lorrana', 'Lucas', 'Lucca', 'Marcela', 'Marcelo', 
                'Marcos Ornellas', 'Marcos Viana', 'Marília', 'Rafael', 
                'Roberto', 'Ronald', 'Sara', 'Tábata', 'Victor Magalhẽs', 'Victor Prata']

    lugar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 
                23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

    print(f'\nStatus: {len(nome)} participantes e {len(lugar)} lugares.\n')
    for i in range(len(nome)):
        lugar_escolhido = random.choice(lugar)
        print(f'{nome[i]} - {lugar_escolhido}')
        lugar.remove(lugar_escolhido)
        i+=1
    print('\nO lugar de número {} ficou sobrando.\n'.format(*lugar))

sorteio_de_lugares()