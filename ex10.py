num1 = int(input('Digite o primeriro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print('Número {} é maior que o número {}.'.format(num1,num2))
elif num1 == num2 :
    print('Os dois números são iguais.')
else:
    print('Número {} é maior que o número {}'.format(num2,num1))    