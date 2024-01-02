#num = int(input('digite um numero maior que dez'))

#if(num > 10):
    #print('voce digitou o numero: ', num)

#print('finalizando...')

#dividendo = float(input('digite um valor do dividend que seja numero maior de um: '))
#divisor = float(input('digite um valor divisor que seja um numero maior ue um: '))

#if(dividendo > 1 and divisor != 0 ):
    #quociente = dividendo/divisor
    #print('resultado da divisão: ', quociente)

#print('fim!')

#valor_compra = float(input('digite o valor da compra: '))
#valor_pago = float(input('digite o valor pago: '))

#if(valor_pago >= valor_compra):
    #troco = valor_pago - valor_compra
    #print('seu troco é: ',troco)
#else:
    #print('o valor pago é isuficiente para efeturar a comprar... ')

#print('finalizadando comprar...')

#nota = float(input('informe o valor da nota: '))

#if(nota >= 5):
    #print('aprovado(a)')
#elif(nota >= 0 and nota < 5 ):
    #print('recuperação')
#else:
    #print('reprovado(a)')

#print('fim!')

#idade = int(input('informe a idade: '))

#if(idade >= 60):
    #print('vc é idosa')
#elif(idade >= 18 and  idade < 60):
    #print('vc é aulto')
#elif(idade >= 12 and idade < 18):
    #print('vc é adolescente')
#else:
    #print('vc é criança')

#print('fim!')

gosto = input('infrome seu gosto culinario:\n[1]vegano\n[2]Carnivoro\n')

if gosto == '1':

    menu =  input('informe o que vc quer comer: \n[1]salada de frutas\n[2]suco natural\n[3]sorvete vegano')
    if menu == '1':
        print('saindo um salada de frutas')
    elif menu == '2':
        print('saindo um suco natural agora!')
    elif menu == '3':
        print('saindo um sorvete vegano bem geladinho')
    else:
        print('desculpa... não temos essa opção...')

elif gosto == '2':

    menu =  input('informe o que vc quer comer\n[1]chuc=rrasco\n[2]coca-cola\n[3]frango assado')
    if menu == '1':
        print('saindo um churrasquinho...')
    elif menu == '2':
        print('saindo uma coca-cola agora!')
    elif menu == '3':
        print('saindo um frano assado')
    else:
        print('desculpa... não temos essa opção...')

else: 
    print('desculpa por não conseguir atende-lo de acordo com seu gosto')

print('fim!')