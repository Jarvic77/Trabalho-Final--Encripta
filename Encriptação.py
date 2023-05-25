import string

def encode(key, texto):
    cifrado = ""
    for i in range(len(texto)):
        letra = texto[i]
        if letra.isspace():
            cifrado += letra
        elif letra.isupper():
            cifrado += chr((ord(letra) + key - 65) % 26 + 65) #desloca o valor numérico ASCII do caractere pela chave e subtrai 65: %26 para garantir que o valor permaneça entre 0 e 25, e adiciona 65 para obter o valor numérico ASCII do caractere codificado.
        else:
            cifrado += chr((ord(letra) + key - 97) % 26 + 97) #se nao for maiusculo
    return cifrado

def encodestrings(str):
    string1 = "ZSBTRQLAMUWDVPNCXGEIFY"
    string2 = "CBHDIGPXWJVQANETORYKZU"
    encoded = ""
    strup = str.upper()

    for index in range(len(str)):
        if strup[index].isspace():
            encoded += strup[index]
        elif index % 2 == 0:
            for i in range(len(string.ascii_uppercase)):
                if strup[index] == string.ascii_uppercase[i]:
                    encoded += string1[i]
        elif index % 2 != 0:
            for i in range(len(string.ascii_uppercase)):
                if strup[index] == string.ascii_uppercase[i]:
                    encoded += string2[i]
    return encoded


def decode(key, texto):
    decifrado = ""
    for i in range(len(texto)):
        letra = texto[i]
        if letra.isspace():
            decifrado += letra
        elif letra.isupper():
            decifrado += chr((ord(letra) - key - 65) % 26 + 65)
        else:
            decifrado += chr((ord(letra) - key - 97) % 26 + 97)
    return decifrado

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
        

#----- MENU -----
def menu():
    print("|---------------------------------|") 
    print("| 1 - Frase")
    print("| 2 - Codificar")
    print("| 3 - Codificar com 2 strings")
    print("| 4 - Descodificar")
    print("| 5 - Descodificar com 2 strings")
    print("| 6 - Histograma normal")
    print("| 7 - Histograma codificado")
    print("| 8 - Histograma codificado com 2 strings")
    print("| 9 - Novo deslocamento")
    print("| 0 - Sair")
    print("| ")
    opcao = int(input("| Introduza a opção: "))
    print("|---------------------------------|") 
    return opcao

#------DEFINIR AS VARIAVEIS GLOBAIS------
with open('palavra-passe.txt', 'r') as f: #lê o ficheiro que tem a passe
    texto = f.read()
alfabeto = "ABCDEFGHIJKLMANOPQRSTUVWXYZ"
deslocamento = (int(input("| Introduza quantas letras quer deslocar (1 - 25): ")))



opcao = menu()
while opcao != 0:
    if opcao == 1:
        print("| Frase: %s"%(texto))  
    elif opcao == 2:
        texto_cifrado = encode(deslocamento, texto)
        print("| Codificada: %s"%(texto_cifrado))
    elif opcao == 3:
        texto_cifrado_frases = encodestrings(texto)
        print("| Codificada com 2 strings: %s"%(texto_cifrado_frases))
    elif opcao == 4:
        texto_decifrado = decode(deslocamento, texto_cifrado)
        print("| Descodificada: ", texto_decifrado)
    elif opcao == 5:
        texto_decifrado_frases = decode(deslocamento, texto_cifrado_frases)
        print("| Descodificada com 2 strings: ", texto_decifrado_frases)
    elif opcao == 6:
        textominusculasjunto= ''.join(filter(str.isalpha, texto)) # Remover todos os caracteres que não são letras
        histogramatexto = frequenciahisto(textominusculasjunto)
        print("| ->Histograma frase<- ")
        print("| Frase: %s"%(texto))  
        mostrahistograma(histogramatexto)
    elif opcao == 7:
        texto_cifradominesculasjunto = ''.join(filter(str.isalpha, texto_cifrado))
        histogramatexto_cifrado = frequenciahisto(texto_cifradominesculasjunto)
        print("| ->Histograma frase codificada<- ")
        print("| Codificada: %s"%(texto_cifrado))
        mostrahistograma(histogramatexto_cifrado)
    elif opcao == 8:
        texto_cifradominesculasjunto_duasfrases= ''.join(filter(str.isalpha, texto_cifrado_frases)) # Remover todos os caracteres que não são letras
        histogramatexto_cifrado_duasfrases = frequenciahisto(texto_cifradominesculasjunto_duasfrases)
        print("| ->Histograma codificado com 2 strings<- ")
        print("| Codificada com 2 strings: %s"%(texto_cifrado_frases))
        mostrahistograma(histogramatexto_cifrado_duasfrases)
    elif opcao == 9:
        deslocamento = (int(input("| Introduza quantas letras quer deslocar (1 - 25): ")))
    else:
        print("| Opção inválida")
    opcao = menu()


