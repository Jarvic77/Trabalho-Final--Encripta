def encode(passe):
    desloca = 3
    alfabeto = "ABCDEFGHIJKLMANOPQRSTUVWXYZ"
    passe_cifrada = ""
    passe = passe.upper()
    for letra in passe:
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            n_indice = (indice + desloca) % len(alfabeto)
            passe_cifrada += alfabeto[n_indice]       
        else:
            passe_cifrada += letra
    return passe_cifrada

def decode(passe):
    print("| ")

def frequenciaHisto(texto):
    frequencia = {} # Contar a frequência de cada letra do alfabeto
    for letra in texto:
        if letra in frequencia:
            frequencia[letra] += 1 
        else:
            frequencia[letra] = 1
    return frequencia

def mostraHistograma(texto):
    for letra, freq in sorted(texto.items()): # percorre cada par chave-valor no dicionário frequencia. A função sorted() é usada para classificar as chaves do dicionário em ordem alfabética.
        print(f"| {letra}: {'*' * freq}") #linha print(f"{letra}: {'*' * freq}") imprime uma mensagem na tela para cada letra e as vezes que repete


#------DEFINIR AS VARIAVEIS GLOVAIS------
with open('palavra-passe.txt', 'r') as f: #lê o ficheiro que tem a passe
    password = f.read()
cifrada = encode(password)
cifradaLower = cifrada.lower()
cifradaLowerEspaço = ''.join(filter(str.isalpha, cifradaLower))
passwordLower = password.lower() #converte a palavra-passe para minusculas
passowrdLowerEspaço = ''.join(filter(str.isalpha, passwordLower)) # Remover todos os caracteres que não são letras
#filter() é usada para verificar se é uma letra ou não. str.isalpha() verifica se é letra ou nao, se for é mantido. join() une os caracteres
histogramaCifrada = frequenciaHisto(cifradaLowerEspaço)
#------------

def opcao(op):
    if op == 1:
        print("| ")
        print("| --> Mostrar palavra-passe <--")
        print("| Palavra passe: %s"%(password))
        print("| ")
        menu()
    elif op == 2:
        print("| ")
        print("| --> Mostrar palavra-passe cifrada <--")
        print("| Palavra passe cifrada: %s"%(cifrada))
        print("| ")
        menu()
    elif op == 3:
        print("| ")
        print("| --> Mostrar histograma palavra-passe <--")
        print("| Palavra passe: %s"%(password))
        histogramaPassword = frequenciaHisto(passowrdLowerEspaço)
        mostraHistograma(histogramaPassword)
        print("")
        menu()
    elif op == 4:
        print("| ")
        print("| --> Mostrar histograma palavra-passe cifrada <--")
        print("| Palavra passe cifrada: %s"%(cifrada))
        histogramaCifrada = frequenciaHisto(cifradaLower)
        mostraHistograma(histogramaCifrada)
        menu()
    elif op == 0:
        exit()


def menu():
    print("| --------------------- MENU --------------------- ")
    print("| 1 - Mostrar palavra-passe")
    print("| 2 - Mostrar palavra-passe cifrada")
    print("| 3 - Mostrar histograma palavra-passe")
    print("| 4 - Mostrar histograma palavra-passe cifrada")
    print("| 0 - Sair")
    print("| ------------------------------------------------ ")
    escolha = int(input("| Escolha uma opção: "))
    print("| ------------------------------------------------ ")
    opcao(escolha)

menu()