def encode(key, str):
    encoded = ""
    for i in range(len(str)):
        char = str[i]
        if (char.isupper()):
            encoded += chr((ord(char) + key - 65) % 26 + 65)
        else:
            encoded += chr((ord(char) + key - 97) % 26 + 97)
    return encoded

def decode(key, str):
    decoded = ""
    for i in range(len(str)):
        char = str[i]
        if (char.isupper()):
            decoded += chr((ord(char) - key - 65) % 26 + 65)
        else:
            decoded += chr((ord(char) - key - 97) % 26 + 97)
    return decoded

def frequenciahisto(texto):
    texto = texto.lower()
    frequencia = {} # Contar a frequência de cada letra do alfabeto
    for letra in texto:
        if letra in frequencia:
            frequencia[letra] += 1 
        else:
            frequencia[letra] = 1
    return frequencia

def mostrahistograma(texto):
    for letra, freq in sorted(texto.items()): # percorre cada par chave-valor no dicionário frequencia. A função sorted() é usada para classificar as chaves do dicionário em ordem alfabética.
        print(f"| {letra}: {'*' * freq}") #linha print(f"{letra}: {'*' * freq}") imprime uma mensagem na tela para cada letra e as vezes que repete

#
#def encodestrings(texto, alfabeto):
#    chave1 = "ZSBTRQLAMUWDVPNCXGEIFY" #pares
#    chave2 = "CBHDIGPXWJVQANETORYKZU" #impares
   # texto = texto.upper()
  #  texto_cifrada = ""
  #  tamanho_texto = len(texto)
 #   tamanho_alfabeto = len(alfabeto)
#    for i in range(tamanho_texto):
#        letra = texto[i]
#        for f in range(tamanho_alfabeto):
#            if (letra == alfabeto[f] and i % 2 == 0):
#                texto_cifrada += chave1[f] #pares
#            elif(letra == alfabeto[f] and i % 2 != 0):
#                texto_cifrada += chave2[f] #impares
#            else:
#                texto_cifrada += ""
#    return texto_cifrada
#

#------DEFINIR AS VARIAVEIS GLOBAIS------
with open('palavra-passe.txt', 'r') as f: #lê o ficheiro que tem a passe
    texto = f.read()
alfabeto = "ABCDEFGHIJKLMANOPQRSTUVWXYZ"
deslocamento = (int(input("| Introduza quantas letras quer deslocar (1 - 25): ")))

#----- MENU -----
def menu():
    print("|---------------------------------|") 
    print("| 1 - Frase")
    print("| 2 - Codificar")
    print("| 3 - Descodificar")
    print("| 4 - Histograma normal")
    print("| 5 - Histograma codificado")
    print("| 6 - ")
    print("| 7 - Novo deslocamento")
    print("| 0 - Sair")
    print("| ")
    opcao = int(input("| Introduza a opção: "))
    print("|---------------------------------|") 
    return opcao

opcao = menu()
while opcao != 0:
    if opcao == 1:
        print("| Frase: %s"%(texto))  
    elif opcao == 2:
        texto_cifrado = encode(deslocamento, texto)
        print("| Codificada: %s"%(texto_cifrado))
    elif opcao == 3:
        texto_decifrado = decode(deslocamento, texto_cifrado)
        print("| Descodificada: ", texto_decifrado)
    elif opcao == 4:
        textominusculasjunto= ''.join(filter(str.isalpha, texto)) # Remover todos os caracteres que não são letras
        histogramatexto = frequenciahisto(textominusculasjunto)
        print("| ->Histograma frase<- ")
        print("| Frase: %s"%(texto))  
        mostrahistograma(histogramatexto)
    elif opcao == 5:
        texto_cifradominesculasjunto = ''.join(filter(str.isalpha, texto_cifrado))
        histogramatexto_cifrado = frequenciahisto(texto_cifradominesculasjunto)
        print("| ->Histograma frase codificada<- ")
        print("| Codificada: %s"%(texto_cifrado))
        mostrahistograma(histogramatexto_cifrado)
    elif opcao == 6:
        print("|")
    elif opcao == 7:
        deslocamento = (int(input("| Introduza quantas letras quer deslocar (1 - 25): ")))
    else:
        print("| Opção inválida")
    opcao = menu()


