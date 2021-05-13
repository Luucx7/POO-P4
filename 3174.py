# -*- coding: utf-8 -*-
quantia = int(input())  # Recebe a quantia de elfos

# Inicia as variáveis com as quantias de horas para cada tipo de brinquedo
horasBonecos = 0
horasArquitetos = 0
horasMusicos = 0
horasDesenhistas = 0

for i in range(quantia):  # Executa para a quantia de elfos
    entrada = list(input().split())  # Recebe e separa a entrada de caracteres, e depois transforma-a em lista

    if entrada[1] == "bonecos":  # Se a entrada é bonecos, soma as horas aos bonecos
        horasBonecos += int(entrada[2])
    if entrada[1] == "arquitetos":  # Se a entrada é de arquitetos, soma horas aos arquitetos
        horasArquitetos += int(entrada[2])
    if entrada[1] == "musicos":  # Soma as horas aos músicos.
        horasMusicos += int(entrada[2])
    if entrada[1] == "desenhistas":  # Soma as horas aos bonecos.
        horasDesenhistas += int(entrada[2])

# Divide as horas trabalhadas pelas horas necessárias para criar um brinquedo da categoria.
# Irá ignorar decimais.
brinquedosBonecos = horasBonecos // 8
brinquedosArquitetos = horasArquitetos // 4
brinquedosMusicos = horasMusicos // 6
brinquedosDesenhistas = horasDesenhistas // 12

# A soma dos brinquedos em todas as categorias será a quantia total de brinquedos, que será impressa.
print(brinquedosDesenhistas + brinquedosMusicos + brinquedosArquitetos + brinquedosBonecos)
