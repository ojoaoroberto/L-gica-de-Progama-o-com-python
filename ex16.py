a = int(input("Digite um número "))
b = int(input("Digite um número "))
c = int(input("Digite um número "))


if (a < b + c ) and (b < a + c) and (c < a + b):
   print("é um triângulo")
else:
    print("Não é um triângulo") 