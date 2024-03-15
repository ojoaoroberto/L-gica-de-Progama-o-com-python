numeroConta =  int(input("Qual o número da sua conta? "))
saldo = float(input("Qual o seu saldo? "))
debito = float(input("Qual o seu debito? "))
credito = float(input("Qual vai ser o valor creditado? "))

dsc = saldo + credito - debito

if dsc >= 0:
    print("Seu saldo é de {} portanto ele é positivo!" .format(dsc))
else:
    print("Seu saldo é de {} portanto ele é negativo!".format(dsc))    
