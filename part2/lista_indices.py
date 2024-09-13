jogador = [11, 8, 13, 14, 16, 10, 7, 13, 3]
          # 0  1   2   3   4   5  6  7   8
					#                              -1



# jogador[inicio:fim:passo]
# jogador[:fim:passo] = ele começa da posição 0 = jogador[0:fim:passo]
# jogador[inicio::passo] = ele termina na última posição = jogador[0:-1:passo]
# jogador[inicio:fim:] = ele considera que eu tô pegando os valores de
#                        1 em 1 = jogador[inicio:fim:1]


## passo
# jogador = [11, 8, 13, 14, 16, 10, 7, 13, 3]

# pegar os valores de 1 em 1
print(jogador[::]) # [11, 8, 13, 14, 16, 10, 7, 13, 3]
# jogador[::1] = jogador[::] = jogador
print(jogador) # [11, 8, 13, 14, 16, 10, 7, 13, 3]

# pegar os valores de 2 em 2
print(jogador[::2]) # [11, 13, 16, 7, 3]

# pegar os valores de 1 em 1 ao contrário
print(jogador[::1]) # [11, 8, 13, 14, 16, 10, 7, 13, 3]
print(jogador[::-1]) # [3, 13, 7, 10, 16, 14, 13, 8, 11]

## passo (exercicios)

# jogadores de basquete
basquete = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
          # 0  1  2  3  4  5  6  7  8   9

# pegue os valores de 3 em 3
print(basquete[::3]) # [1, 4, 7, 10]

# acessar fora do alcance da lista
print(basquete[17]) # IndexError