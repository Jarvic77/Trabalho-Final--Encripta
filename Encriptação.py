import string

def encode(key, str):
    encoded = ""
    for i in range(len(str)):
        char = str[i]
        if char.isspace() or not char.isalpha():
            encoded += char
        elif char.isupper():
            encoded += chr((ord(char) + key - 65) % 26 + 65) #desloca o valor numérico ASCII do caractere pela chave e subtrai 65: %26 para garantir que o valor permaneça entre 0 e 25, e adiciona 65 para obter o valor numérico ASCII do caractere codificado.
        else:
            encoded += chr((ord(char) + key - 97) % 26 + 97) #se nao for maiusculo
    return encoded

def decode(key, str):
    decoded = ""
    for i in range(len(str)):
        char = str[i]
        if char.isspace() or not char.isalpha():
            decoded += char
        elif char.isupper():
            decoded += chr((ord(char) - key - 65) % 26 + 65)
        else:
            decoded += chr((ord(char) - key - 97) % 26 + 97)
    return decoded


def strencode(str):
    string1 = "ZSBTRQLAMUWDVPNCXGEIFY"
    string2 = "CBHDIGPXWJVQANETORYKZU"
    encoded = ""
    strup = str.upper()
    for index in range(len(str)):
        if strup[index].isspace() or not strup[index].isalpha():
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

def strdecode(str):
    string1 = "ZSBTRQLAMUWDVPNCXGEIFY"
    string2 = "CBHDIGPXWJVQANETORYKZU"
    decoded = ""
    strup = str.upper()
    for index in range(len(str)):
        if strup[index].isspace() or strup[index].isalpha():
            decoded += strup[index]
        elif index % 2 == 0:
            for i in range(len(string.ascii_uppercase)):
                if strup[index] == string1[i]:
                    decoded += string.ascii_uppercase[i]
        elif index % 2 != 0:
            for i in range(len(string.ascii_uppercase)):
                if strup[index] == string2[i]:
                    decoded += string.ascii_uppercase[i]
    return decoded

def frequenciahistograma(str):
    strlow = str.lower()
    freq = {} # Contar a frequência de cada letra do alfabeto
    for char in strlow:
        if char in freq:
            freq[char] += 1 
        else:
            freq[char] = 1
    return freq

def mostrahistograma(str):
    for char, freq in sorted(str.items()): # percorre cada par chave-valor no dicionário frequencia. A função sorted() é usada para classificar as chaves do dicionário em ordem alfabética.
        print(f"| {char}: {'*' * freq}") #linha print(f"{letra}: {'*' * freq}") imprime uma mensagem na tela para cada letra e as vezes que repete
        
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
    op = int(input("| Introduza a opção: "))
    print("|---------------------------------|") 
    return op

#------DEFINIR AS VARIAVEIS GLOBAIS------
with open('palavra-passe.txt', 'r') as f: #lê o ficheiro que tem a passe
    text = f.read()
deslocamento = (int(input("| Introduza quantas letras quer deslocar (1 - 25): ")))

op = menu()
while op != 0:
    if op == 1:
        print("| Frase: %s"%(text))  
    elif op == 2:
        encoded_text = encode(deslocamento, text)
        print("| Codificada: %s"%(encoded_text))
    elif op == 3:
        encoded_strings = strencode(text)
        print("| Codificada com 2 strings: %s"%(encoded_strings))
    elif op == 4:
        decoded_text = decode(deslocamento, encoded_text)
        print("| Descodificada: ", decoded_text)
    elif op == 5:
        decoded_strings = strdecode(encoded_strings)
        print("| Descodificada com 2 strings: ", decoded_strings)
    elif op == 6:
        text_nospace = ''.join(filter(str.isalpha, text)) # Remover todos os caracteres que não são letras
        histograma_text = frequenciahistograma(text_nospace)
        print("| ->Histograma frase<- ")
        print("| Frase: %s"%(text))  
        mostrahistograma(histograma_text)
    elif op == 7:
        encoded_nospace = ''.join(filter(str.isalpha, encoded_text))
        histograma_encoded = frequenciahistograma(encoded_nospace)
        print("| ->Histograma frase codificada<- ")
        print("| Codificada: %s"%(encoded_text))
        mostrahistograma(histograma_encoded)
    elif op == 8:
        encoded_strings_nospace= ''.join(filter(str.isalpha, encoded_strings)) # Remover todos os caracteres que não são letras
        histograma_encoded_strins = frequenciahistograma(encoded_strings_nospace)
        print("| ->Histograma codificado com 2 strings<- ")
        print("| Codificada com 2 strings: %s"%(encoded_strings))
        mostrahistograma(histograma_encoded_strins)
    elif op == 9:
        deslocamento = (int(input("| Introduza quantas letras quer deslocar (1 - 25): ")))
    else:
        print("| Opção inválida")
    op = menu()


