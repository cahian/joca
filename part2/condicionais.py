# # Ganhar ou perder vida
# vida = 100
#
# # if = se
# if vida == 0:  # **se** vida for igual a 0 então faça
#   print("Você morreu!")  # 2 espaços aqui é indentação
# if vida > 0:
#   print("Você está vivo, continue jogando!")

# # if = se
# # elif = senão se
# # else = senão

# if <condição>:
#   <ação>
# elif <condição>:
#   <ação>
# else:
#   <ação>



bateria = 200

if bateria <= 5:  # True ou False
  print("Sua bateria está muito fraca! O seu celular está prestes a desligar!")
elif bateria <= 15:  # True ou False
  print("Sua bateria está fraca! Coloque num carregador!")
elif bateria > 100:
  print('Procure um técnico especializado imediatamente para trocar a sua bateria!!!!!!')
else: # Always True
  print('Sua bateria está normal!!!')

print('Fim do programa!')


sinal = "-"

if sinal == "+":
    print("Soma")
elif sinal == "-":
    print("Subtração")
elif sinal == "*":
    print("Multiplicação")
elif sinal == "/":
    print("Divisão")
else:
    print("Operador inválido")