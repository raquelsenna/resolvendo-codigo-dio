def main():
  n1 = float(input("Nota 1: "))
  n2 = float(input("Nota 2: "))
  n3 = float(input("Nota 3: "))

  media_notas(n1, n2, n3)


def media_notas(nota1, nota2, nota3):
  media = (nota1 + nota2 + nota3) / 3

  print(f"Média: {round(media, 2)}")


main()