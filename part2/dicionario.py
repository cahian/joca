# Dicionarios armazenam mapeamentos de chaves para valores
empty_dict = {}
# Aqui está um dicionário preenchido
filled_dict = {"one": 1, "two": 2, "three": 3}
#              [1, 2, 3, 10, 12, 14, 13, 22]

# Lista:
jogadores_de_basquete = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                        #0  1  2  3  4  5  6  7  8   9
# jogadores_de_futebol = [11, 8, 13, 14, 16, 10, 7, 13, 3]

# Dicionario:
jogadores_de_futebol = {
	'Cristiano Ronaldo': 7,
	'Memphis Depay': 94,
	'Erling Haaland': 10,
}

# print(jogadores_de_futebol.keys())
# print(jogadores_de_futebol.values())

# print(jogadores_de_futebol['Memphis Depay'])

# print(jogadores_de_basquete[6])
# print(jogadores_de_futebol['Cristiano Ronaldo'])


freefire_players = {
	'Nobru': 'Loud',
	'Freitas': 'Fluxo',
	'Lszinn': 'Loud',
}
# print(freefire_players.keys())
# print(freefire_players.values())
# print(freefire_players['Freitas']) # chaves
# print(freefire_players.get('Freitas')) # get método
# print(freefire_players['Xuxa'])
print(freefire_players.get('Xuxa'))