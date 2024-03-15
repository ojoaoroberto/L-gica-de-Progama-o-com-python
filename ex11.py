nota1 = float(input("Qual foi sua primeira nota? "))
nota2 = float(input("Qual foi sua segunda nota? "))

media = nota1 + nota2 
resultado = media/2

if resultado > 7:
    print("Parábens você foi aprovado(a).")
elif resultado == 7:
    print("Você foi aprovado! Mas foi por pouco.")    
else:
    print("Você foi reprovado!")

