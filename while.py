#num = 0 

#while(num <= 10):
    #print(num)
    #num = num + 1 

#num = 10 

#while(num >= 0):
    #print(num)
    #num = num - 1


#n = 1

#while(n <= 10):
    #if(n%2 == 0):
        #print(n)
    #n+=1

#num = float(input('digite um numero maior que 1: '))

#while(num <= 1):
    #num = float(input('valor invalido, digite um numero maior que 1!'))
#print('voce digitou o valor', num)


h = int(input('informe o horario que deseja marcar, entre 6h e 18h '))

while(h < 6 or h > 18):
    h = int(input('horario invalido, ente 6h e 18h'))

print('sua consulta foi marcada para', h)

 
