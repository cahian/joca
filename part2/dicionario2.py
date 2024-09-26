loud = {
	'Lszinn': 26,
	'Bradoock': 29,
	'Babi': 22,
}

fluxo = {
	'Nobru': 26,
	'Freitas': 22,
	'Dak': 28,
}

youtubers = {}
# Maneira 1:
youtubers = {**loud, **fluxo}

print('Loud:', loud)
print('Fluxo:', fluxo)
print('Maneira 1: Youtubers:', youtubers)
# Maneira 2:
youtubers = {}
youtubers.update(loud)
youtubers.update(fluxo)
print('Maneira 2: Youtubers:', youtubers)

# print('Operador in:', 'Nobru' in youtubers)
# print('Operador in:', 'Gaules' in youtubers)
# print('Operador in:', 'Babi' not in youtubers)
