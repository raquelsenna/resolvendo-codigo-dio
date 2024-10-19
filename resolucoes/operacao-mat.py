def main():
  n1 = float(input("Número 1 -> "))

  n2 = float(input("Número 2 -> "))

  oper = input("Qual operação: [+, -, /, *, **, %] -> ")

  calculadora(n1, n2, oper)


def calculadora(num1, num2, oper):
  if oper == "+":
    print(num1 + num2)
  elif oper == "-":
    print(num1 - num2)
  elif oper == "/":
    print(num1 / num2)
  elif oper == "*":
    print(num1 * num2)
  elif oper == "**":
    print(num1 ** num2)
  elif oper == "%":
    print(num1 % num2)


main()
