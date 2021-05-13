# -*- coding: utf-8 -*-
#
# Função que verifica se certo caractere é maiúsculo ou não (pra ficar mais limpo o código)
def isUpper(entrada: chr):
    if char == " ":  # Vai que ele identifica espaço como maiúsculo...
        return False
    return entrada == entrada.upper()  # Se a entrada é igual a entrada na versão maiúscula, ela é maiúscula.


# Arrays com as teclas de cada a número
TECLA_2 = ["a", "b", "c"]
TECLA_3 = ["d", "e", "f"]
TECLA_4 = ["g", "h", "i"]
TECLA_5 = ["j", "k", "l"]
TECLA_6 = ["m", "n", "o"]
TECLA_7 = ["p", "q", "r", "s"]
TECLA_8 = ["t", "u", "v"]
TECLA_9 = ["w", "x", "y", "z"]

# Lista com as teclas por número, na ordem dos números
# dummy é ignorado pois 1 não faz nada, mas existe para existir corretamente as posições.
DICT_TECLAS = [[" "], ["dummy"], TECLA_2, TECLA_3, TECLA_4, TECLA_5, TECLA_6, TECLA_7, TECLA_8, TECLA_9]

casos = int(input())  # Recebe a quantia de entradas e transforma em inteiro

for i in range(casos):  # Executa o código na quantia de vezes especificada
    texto = input()  # Recebe a entrada de texto

    # Variáveis de controle
    # Iniciadas com valores impossíveis (ou que não deveriam) ser tratados.
    digitar = ""  # Os valores que deverão ser digitados para escrever o texto especificado
    lastChar = '!'  # Último caractere tratado
    lastNum = -1  # Último número do caractere tratado

    isFirst = True  # Resolve um bug MUITO específico que fazia a resposta dar "Wrong answer (0%)"

    for char in texto.__iter__():  # Laço executado para cada caractere do texto inserido
        upperCase = False  # Variável informando se o caractere está em maiúsculo

        # Verifica se é um espaço
        if char == " ":
            digitar = digitar + "0"  # Adiciona zero se for um espaço, e define as variáveis de controle.
            lastChar = " "
            lastNum = 0
            continue  # Continua para o próximo caractere

        # Verifica se é caixa-alta
        if isUpper(char):
            digitar = digitar + "#"  # Adiciona o caractere de caixa alta se sim
            upperCase = True  # Marca a variável indicando que é caixa-alta

        # Temporário antes de ser armazenado na variável de controle, para não quebrar as verificações
        tempNum = -1
        tempChar = '@'

        # Procura nas listas de teclas
        for j in range(10):
            if j == 1: # Se for a tecla um, pula
                continue

            v = DICT_TECLAS[j]  # Teclas a serem buscadas

            if v.__contains__(char.lower()):  # Teclas buscadas contém tecla?

                for k in range(len(v)):  # Laço entre as teclas
                    if v[k].lower() == char.lower():  # Se a tecla da lista, transformada em minúsculo, é igual ao caractere atual, transformado em minúsculo
                        num = j  # J equivale ao número que deve ser teclado

                        # Verifica se o último caractere inserido pertencia a mesma tecla, caso não seja maiúscula e nem a primeira (primeira por causa do BUG grotesco)
                        if DICT_TECLAS[lastNum].__contains__(char) and not upperCase and not isFirst:
                            digitar = digitar + "*"  # Adiciona o * de espera caso não seja maiúscula, primeira e seja a mesma tecla do caractere anterior.

                        # Adiciona a tecla, transforma J (o valor da tecla) em string, e K sendo a posição da letra na tecla (+1 pois ela se inicia em zero)
                        # A tecla é multiplicada pela posição na mesma, sendo pelo menos um.
                        digitar = digitar + (str(j) * (k + 1))

                        # Variáveis temporárias, se definir as de controle agora irá quebrar o programa.
                        tempChar = char
                        tempNum = j
                        # Não quebrei os laços múltiplos pois eu sinceramente não sei fazer isso em Python
            else:
                continue  # Não quero valores impossíveis nas variáveis de controle (segurança)

        # Armazena na variável de controle
        lastChar = tempChar
        lastNum = tempNum
        if isFirst:
            isFirst = False  # Mais coisas relacionadas ao bug louco.

    print(digitar)  # Imprime o que deve ser teclado para este caso de teste
