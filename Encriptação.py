frequencia = {}

def encode(passe, desloca):
    print("| ")


def decode(passe, desloca):
    print("| ")


with open('palavra-passe.txt', 'r') as f:
    password = f.read()

passwordmin = password.lower() #converte a palavra-passe para minusculas

# A função filter() é usada para iterar sobre cada caractere do conteúdo do arquivo e verificar se ele é uma letra ou não. A função str.isalpha() é passada como 
#argumento para filter() para testar se o caractere atual é uma letra. Se o caractere for uma letra, ele é mantido na sequência de caracteres filtrados.
#Em seguida, a função join() é usada para unir todos os caracteres filtrados novamente em uma string. A string vazia '' é usada como separador entre os caracteres, 
#o que significa que os caracteres filtrados são simplesmente concatenados sem nenhum espaço ou outro caractere de separação. 

# Remover todos os caracteres que não são letras
texto = ''.join(filter(str.isalpha, passwordmin))

# Contar a frequência de cada letra do alfabeto
frequencia = {}
for letra in texto:
    if letra in frequencia:
        frequencia[letra] += 1
    else:
        frequencia[letra] = 1

print("| ")
print ("| --> Palavra passe: %s"%(password))
print("| ")

#O loop for letra, freq in sorted(frequencia.items()): percorre cada par chave-valor no dicionário frequencia. A função sorted() 
#é usada para classificar as chaves do dicionário em ordem alfabética.
#------
#A última linha print(f"{letra}: {'*' * freq}") imprime uma mensagem na tela para cada letra, que inclui a letra e
#uma sequência de asteriscos * cujo comprimento é igual à frequência da letra. O resultado final é um histograma de 
#letras com cada letra e o número de ocorrências representado por um número correspondente de asteriscos.
print("| --> Histograma de Letras <--")
for letra, freq in sorted(frequencia.items()):
    print(f"| {letra}: {'*' * freq}")
print("| ")