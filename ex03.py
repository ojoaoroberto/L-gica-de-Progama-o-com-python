#escrever algoritimo que expressa idade da pessoa em anos, meses e dias

idade = int(input('Qual sua idade? '))

meses = 12 * idade

dias = 365 * idade

print('Sua idade é {} e você tem {} meses de idade e {} dias' .format(idade, meses, dias))
