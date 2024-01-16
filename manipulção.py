#arquivo = open('python.txt','r')
#frase = arquivo.readline()
#print(type(arquivo))
#print(frase)
#print(type(frase))
#arquivo.close()

#texto = arquivo.readlines()
#print(texto)
#print(texto[0])
#print(texto[1])

#print(type(texto))
#print(type(texto[0]))

#arquivo.close()

#arquivo = open('python.txt','w') #escreve algo no doc

#frase = 'sou uma desenvolvedora'
#arquivo.write(frase)
#arquivo.close()#fecha o doc editado

#arquivo = open('python.txt','r')#abre novamente, so que agora editadp
#print( arquivo.readline() )
#arquivo.close()#fecha o editado

arquivo = open('python.txt','a')

frase = '\nterei sucesso na mminha jornada!'
arquivo.write(frase)
arquivo.close()#fechou o editado para abrir ele

#(não tem como ler um arquivo editado sem antes fecha-lo e abrir ele novamente)

arquivo = open('python.txt', 'r')
for linha in arquivo.readlines(): #ele vai ler todas as linhas
    print(linha)
arquivo.close()





