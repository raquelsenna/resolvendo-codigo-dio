palavra = input("Palavra: ")

ver_palavra = palavra[::-1]

if palavra.upper() == ver_palavra.upper():
  print("É Palíndromo!")
else:
  print("Não é Palíndromo!")