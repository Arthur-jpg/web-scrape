lista = ['Azul', 'Vermelho', 'Roxo']
lista2 = ['Azul', 'Preto']

for i in range(len(lista2)):
    if lista2[i] in lista:
        print('Sim')
        print(lista2[i])
    else:
        print('No')