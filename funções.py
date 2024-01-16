#lado = float(input('digite o lado do quadrado em metros'))

#def calcula_area():
#    area = lado*lado
#    return area #precisa disso para ser uma função de retorno

#fluxo principal
#resultado = calcula_area() ou ...
#print('a area  di quadrado de lado',lado, 'm é', calcula_area(), 'm²')

#convertendo para cm²
#resultado = calcula_area()*10000
#print('a area  di quadrado de lado',lado, 'm é', resultado, 'cm²')

#n = int(input('digite um numero: '))

#def testa_valor():
#    if n > 0:
#        return 1 
    
#    elif n == 0:
#        return 0 
#    print('numero negativo')
#    return -1

#testa_valor() #fluxo principal: o python vai ler o input primeiro, depois o fluxo principal e nessa função vai ir para o def

#funções com parametros#

#def le_numero():
#    num = float(input('digite o lado do quadrado'))
#    return num
#def calcula_area_quadrado(lado): #isso é um parametro, dentro do () é o argumento do parametro
#    area = lado*lado
#    return area

#valor = le_numero()#fluxo principal
#resultado = calcula_area_quadrado(valor)
#print('a area do quadrado é:', resultado)

#def le_notas():
#    nota1 = float(input('digite a primeira nota: '))
#    nota2 = float(input('digite a segunda nota: '))
#    nota3 = float(input('digite a terceira nota: '))
#    return [nota1, nota2, nota3] #transformou em uma lista []

#def calcula_media(n1, n2, n3):
#    media = (n1 + n2 + n3)/3
#    return media

#nt1, nt2, nt3 = le_notas()
#resultado = calcula_media(nt1, nt2, nt3)#o PYTHON vai pegar as n1 n2 e  n3 mesmo que elas sejam diferentes de nt1 nt2 e nt3
#print('mediia: ',resultado)

#def calcula_media():
#    n1, n2, n3 = le_notas()
#    media = (n1 + n2 +n3)/3
#    return media

#resultado = calcula_media
#print('media: ', resultado)

#EU QUE RESOLVI O PROBLEMA DO CODIGO!

def calcula_media(qtd_notas):
    total = 0
    contador = 0

    while (contador < qtd_notas):
        total += float(input('digite a nota: '))
        total += float(input('digite a nota: '))
       
        return total/qtd_notas

def verifica_aprovacao(media, faltas, nome):
    print('Media: ', media, 'Faltas: ', faltas)
    if media  >= 5 and faltas <= 4:
        print('estudante', nome, 'APROVADO(A)')
    elif media < 5 and faltas <= 4:
        print('estudante', nome, 'RECUPERAÇÃO')
    else:
        print('estudante', nome, 'REPROVADO(A)')

    
e = input('digite o nome do estudante: ')
f = int(input('quantas faltas o estudante teve: '))
n = int(input('quantas notas deseja inserir: '))
m = calcula_media(n)

verifica_aprovacao(m, f, e)