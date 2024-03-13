#calcular porcentsgem de votos

totaL = int(input('Qtd de habitantes? '))
VB = int(input('Qtd de votos brancos? '))
VN = int(input('Qtd de votos nulos? '))
VV = int(input('Qtd de votos válidos? '))

PB = VB * 100/totaL 
PN = VN * 100/totaL
PV = VV * 100/totaL

print('Quantidade de habitantes {} e a porcentagem de votos validos foi {} %, e votos nulos foi {} %n e votos brancos foi {}'.format(totaL, PV, PN, PB))