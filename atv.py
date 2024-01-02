massa = float (input('informe sua massa em kg: '))
altura  = float (input('informe sua altura: '))

imc = massa/(altura**2)

print('imc é: ', imc)

atual = int(input('informe o ano atual: '))
nasc = int(input('qual é o seu ano de nascimento?' ))

print('suua idade é: ', atual - nasc)

em2035 = 2035 - nasc

print('vc terá em 2035 essa idade: ', em2035)

