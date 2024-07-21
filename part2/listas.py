# (is vs. ==) is checks if two variables refer to the same object, but == checks
# if the objects pointed to have the same values.
# a = [1, 2, 3, 4]  # Point a at a new list, [1, 2, 3, 4]
# b = a             # Point b at what a is pointing to
# b is a            # => True, a and b refer to the same object
# b == a            # => True, a's and b's objects are equal
# b = [1, 2, 3, 4]  # Point b at a new list, [1, 2, 3, 4]
# b is a            # => False, a and b do not refer to the same object
# b == a            # => True, a's and b's objects are equal

# "This is a string."
# 'This is also a string.'


# "Hello " + "world!"  # => "Hello world!"
# "Hello " "world!"    # => "Hello world!"
# "Hello world!"
# print("H" "e" "l" "l" "o" " " "w" "o" "r" "l" "d" "!")  # => "Hello world!"
# print("!" " " " " " " " " " " " " " " " " " " " " " " " " " " "?")

# print("Hello world!"[0])  # => 'H'
# 'H' = 0
# 'e' = 1
#
# 'r' = 8
#
# 'd' = 10

# print("Hello world!"[2])  # => 'l'
# print("Hello world!"[57])  # => IndexError
# print("Hello world!lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll"[57])  # => 'l'

# print("Hello world!"[-1])  # => '!'
# print("Hello world!"[-5])  # => 'o'
# print("Hello world!"[5])  # => ' '
# print("Hello world!"[-8])  # => 'o'
# print("Hello world!"[- 3])  # => 'l'
# print("Hello world!"[+ 3])  # => 'l'
# print("Hello world!"[3])  # => 'l'
# print("Hello world!"[* 3])  # => TypeError
# print("Hello world!"[<numero>])

# print("Hello world!"[0:5]) # => 'Hello'
# print("Hello world!"[<inicio>:<fim não incluído>])
# # O último não conta!
# print("Hello world!"[0:4])
# print("Hello world!"[6:11]) # => 'world'

# try:
# 	print("Hello world!"[57])  # => IndexError
# except IndexError:
# 	print("Hello Joca!")

# len => length => comprimento ou tamanho
# print(len("This is a string"))  # => 16

# Começa contando do 0!
# print("This is a string"[5:7])
# print("This is a string")
# print("This is a string"[0:16])
# Não é do 1!

# print(len("Joca Aula 1"))
# print("Joca Aula 1")
# print("Joca Aula 1"[0:11])

# print(len("Olá Joca!!!"))
# print("Joca Aula 1")
# print("Joca Aula 1"[0:11])


#
# name = "Reiko"
# f"She said her name is {name}."  # => "She said her name is Reiko"
# f"{name} is {len(name)} characters long."  # => "Reiko is 5 characters long."
#
# None
#
# "etc" is None  # => False
# None is None   # => True
#