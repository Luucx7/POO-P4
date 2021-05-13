# -*- coding: utf-8 -*-
casos = int(input())  # Recebe a quantia de casos de teste
for i in range(casos):  # Executa o programa na quantia de vezes especificada
    entrada = list(map(int, input().split()))  # Recebe uma linha de entrada, separa os valores, transforma em inteiro e transforma em lista

    soma = 0  # Variável inicial com os valores de soma
    quantiaFiltros = entrada[0]  # Variável com a quantia de filtros de linha, posição zero da lista (primeiro valor)
    for j in range(1, quantiaFiltros + 1):  # Executa um laço entre os valores, iniciando da posição 1 e encerrando na posição da quantia + 1 (pois o primeiro valor é reservado para a quantia)
        # irá executar na quantia de casos mas de forma diferente.
        soma += entrada[j]  # Soma o valor a variável com a soma

        # Subtrai um da quantia de filtros, pois um filtro estará na tomada, e subtrai a quantia de filtros da soma, pois os mesmos estarão conectados nos filtros subjacentes.
    print(soma - (quantiaFiltros - 1))  # Imprime o valor na tela
