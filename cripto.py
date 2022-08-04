arquivo = open("texto.txt", "w")

# Frase: 
text = (input("Entre com uma frase: \n"))

# Chave de entrada:
key = int(input("Entre com uma chave: \n"))
while (key <= 0) or (key > 3):
    key = int(input("A chave não pode ser igual a 0 ou menor ou maior que 3!\n \
    Tente novamente:"))
print("Chave: ", key) 

# senha em sequencia:
sequence = []
num = 0
for i in range(key):
   sequence.append(int(input("Entre com um número da sequência: \n")))
   
 
# Substitui os espaços em branco por um caracter
text = text.replace(" ", "!")
 
# Divide os textos em grupos do tamanho do array definido na chave:
groups = [text[i:i+key].ljust(key, "!") for i in range(0, len(text), key)]
 
# Percorre os grupos e gera novos gruposs:
result = list()
for group in groups:
    output = ""
    for i in sequence:
        output += group[i-1]
    result.append(output)
 
print(result)
arquivo.writelines(result)
arquivo.close()



