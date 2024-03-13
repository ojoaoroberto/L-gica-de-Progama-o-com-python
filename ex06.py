#venda de carros

salario = int(input('Qual é seu salário? '))
cv = int(input('Quantos carros você vendeu? '))
comissao_por_cv = 200
por = cv * comissao_por_cv
vendas = por * 5 / 100
total = salario + por + vendas

print('Seu salário sem comissoes {}, carros vendidos {}, comissão por carro vendido {}, comissão de 5% em vendas efetuadas {} e seu salário ao todo {}'.format(salario,cv,por,vendas,total))

