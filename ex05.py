#reajuste salarial

salario = int(input('Qual é seu sálario atual? '))
reajuste = float(input('Qual foi o reajuste? '))

total1 =  salario * reajuste / 100
total2 = total1 + salario

print('Seu sálario é {}R$ e o reajuste foi de {}%, Então seu salario atual é {}R$' .format(salario,reajuste,total2))