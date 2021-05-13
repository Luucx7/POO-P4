# -*- coding: utf-8 -*-
casos = int(input())  # Recebe a quantia de casos de teste (e converte em inteiro)
for i in range(casos):  # Executa o programa na quantia de vezes especificada
    entrada = input()  # Recebe o valor do caso de teste

    contemQ = entrada.__contains__("Q")  # Verifica se a entrada contém a carta, e a armazena o valor lógico na variável
    contemK = entrada.__contains__("K")
    contemJ = entrada.__contains__("J")
    contemA = entrada.__contains__("A")

    if contemA and contemJ and contemK and contemQ:  # Se todas as variáveis estão verdadeiras, a entrada possúi as quatro cartas
        print("Aaah muleke")  # Logo, theusin não perde pontos
    else:  # Se não, a entrada não contém todas as cartas, logo
        print("Ooo raca viu")  # Theusin provavelmente perderá pontos
