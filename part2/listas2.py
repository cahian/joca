# variáveis
# var1 = 2

# listas
jogador = [10, 11, 17, 8, 5]
# print(jogador)
# print(jogador[3])
jogador.append(1)  # append = adiciona um item no final da lista
# print(jogador)
jogador.append(14)
jogador.append(21)
# print(jogador)
jogador.append(30)
jogador.append(3)
jogador.append(9)
# print(jogador) # [10, 11, 17, 8, 5, 1, 14, 21, 30, 3, 9]
jogador.pop()  # pop = remove o último item da lista
# print(jogador) # [10, 11, 17, 8, 5, 1, 14, 21, 30, 3]
jogador.pop()  # pop = remove o último item da lista
jogador.pop()  # pop = remove o último item da lista
jogador.pop()  # pop = remove o último item da lista
jogador.pop()  # pop = remove o último item da lista
# print(jogador) # [10, 11, 17, 8, 5, 1]
del jogador[2]  # remove o item da lista
# print(jogador)
del jogador[-1]  # remove o item da lista
# print(jogador) # [10, 11, 8, 5]
jogador.append(12) # append = adiciona um item no final da lista
jogador.pop()      # pop = remove o último item da lista
jogador.append(16)
jogador.pop()
del jogador[0]     # del = remove o nth item da lista

# print(jogador)  # [11, 8, 5]
jogador.append(13)
jogador.append(14)
jogador.append(15)
jogador.pop()
del jogador[2]
# print(jogador)  # [11, 8, 13, 14]

# jogador
# [11, 8, 13, 14]
#  0   1  2   3
# jogador[1:3]
# [8, 13]

# print(jogador[1:3])
jogador.append(16)
jogador.append(10)
jogador.append(7)
jogador.append(13)
jogador.append(1 + 2)


# [11, 8, 13, 14, 16, 10, 7, 13, 3]
#   0  1   2   3   4   5  6   7  8
# [4:7] = [16, 10, 7]
# [1:] = [8, 13, 14, 16, 10, 7, 13, 3]
# [7:] = [13, 3]
# [4:] = [16, 10, 7, 13, 3]


print(jogador) # [11, 8, 13, 14, 16, 10, 7, 13, 3]
# print(jogador[4:7])
# print(jogador[1:])
# print(jogador[7:])
print(jogador[4:])
# print(jogador[:3])
# print(jogador[::2])
# print(jogador[::-1])


# You can start with a prefilled list
# other_li = [4, 5, 6]
#
# # Add stuff to the end of a list with append
# li.append(1)    # li is now [1]
# li.append(2)    # li is now [1, 2]
# li.append(4)    # li is now [1, 2, 4]
# li.append(3)    # li is now [1, 2, 4, 3]
# # Remove from the end with pop
# li.pop()        # => 3 and li is now [1, 2, 4]
# # Let's put it back
# li.append(3)    # li is now [1, 2, 4, 3] again.
#
# # Access a list like you would any array
# li[0]   # => 1
# # Look at the last element
# li[-1]  # => 3
#
# # Looking out of bounds is an IndexError
# li[4]  # Raises an IndexError
#
# # You can look at ranges with slice syntax.
# # The start index is included, the end index is not
# # (It's a closed/open range for you mathy types.)
# li[1:3]   # Return list from index 1 to 3 => [2, 4]
# li[2:]    # Return list starting from index 2 => [4, 3]
# li[:3]    # Return list from beginning until index 3  => [1, 2, 4]
# li[::2]   # Return list selecting elements with a step size of 2 => [1, 4]
# li[::-1]  # Return list in reverse order => [3, 4, 2, 1]
# # Use any combination of these to make advanced slices
# # li[start:end:step]
#
# # Make a one layer deep copy using slices
# li2 = li[:]  # => li2 = [1, 2, 4, 3] but (li2 is li) will result in false.
#
# # Remove arbitrary elements from a list with "del"
# del li[2]  # li is now [1, 2, 3]
#
# # Remove first occurrence of a value
# li.remove(2)  # li is now [1, 3]
# li.remove(2)  # Raises a ValueError as 2 is not in the list
#
# # Insert an element at a specific index
# li.insert(1, 2)  # li is now [1, 2, 3] again
#
# # Get the index of the first item found matching the argument
# li.index(2)  # => 1
# li.index(4)  # Raises a ValueError as 4 is not in the list
#
# # You can add lists
# # Note: values for li and for other_li are not modified.
# li + other_li  # => [1, 2, 3, 4, 5, 6]
#
# # Concatenate lists with "extend()"
# li.extend(other_li)  # Now li is [1, 2, 3, 4, 5, 6]
#
# # Check for existence in a list with "in"
# 1 in li  # => True
#
# # Examine the length with "len()"
# len(li)  # => 6