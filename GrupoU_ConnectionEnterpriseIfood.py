#cadastro de restaurantes
#os dados estão organizados em ['Nome', distancia, nota]
restaurantes = [['Teste1', 1.5, 5.0], ['Teste2', 1.5, 5.0], ['Teste2', 0.2, 3.0], ['O Mineiro', 3.7 , 4.2], ['Amor aos pedacos', 1.2 , 4.3], ['We Cofee', 0.8, 4.5], ['Lamen Kazu', 0.7, 4.8], ['Mr. Pretzels', 1.1, 4.7], ['Brigadeiria', 1.2, 4.7], ['Teste0', 1.5, 6.0]]


#função para ordenar os itens
def func_ordenar_selecao(lista):
    tamanho_lista = len(lista)-1
    ordenado = False
    while not ordenado:  #Repetir enquanto ordenado estiver diferente de = True
        ordenado = True  #Interrompe o loop quando todos estão organizados
        
        for i in range(0, tamanho_lista):
            if lista[i][2] > lista[i+1][2]:
                ordenado = False
                lista[i], lista[i+1] = lista[i+1], lista[i]
            elif lista[i][2] == lista[i+1][2] and lista[i][1] < lista[i+1][1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]

    return list(reversed(lista))

print(func_ordenar_selecao(restaurantes))