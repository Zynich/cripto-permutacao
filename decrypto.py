arquivo = open("texto.txt", "r")


text = arquivo.readlines()

print('abaixo a frase cryptografada')
print(text)
#pega o array e converte para string
myString = " ".join(map(str,text))

print('Teste de string')
print(myString)

#chave
key = int(input("Entre com uma chave: \n"))

while (key <= 0) or (key > 3):
    key = int(input("A chave não pode ser igual a 0 ou menor ou maior que 3!\n \
    Tente novamente:"))
print("Chave: ", key)
 
sequence = []
for i in range(key):
    sequence.append(int(input("Entre com um número da sequência: \n")))
 
groups = [myString[i:i+key].ljust(key, "1") for i in range(0, len(myString), key)]
 

result = list()
for group in groups:
    output = ""
    for i in sequence:
        output += group[i-1]
    result.append(output)
 
#pega a string e remvoe todos os caracteres que nao fazem parte da frase
string = " ".join(map(str,result))
string = string.replace(" ", "")
string = string.replace("!", " ")
string = string.replace("*", " ")
print(string)
arquivo.close()

arquivo = open("textoNovo.txt", "w")

arquivo.writelines(string)
