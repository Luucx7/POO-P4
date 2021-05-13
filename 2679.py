# -*- coding: utf-8 -*-
i = int(input())  # Recebe o valor de entrada e converte em inteiro
if i % 2 == 0:  # Se a entrada dividio por dois for zero, o número é par, logo
    print(i + 2)  # O próximo número par é ele mesmo mais dois.
else:
    print(i + 1) # Se o número é impar, o próximo número (entrada + 1) será par,
