def encode(text, key):
    text = text.upper()

    encoded_text = ""

    for char in text:
        if char.isalpha() and char.isupper():   #ver se é maiuscula
            encoded_char = chr((ord(char) - 65 + key) % 26 + 65)
        else:
            # Mantém o caractere original
            encoded_char = char

        # Adiciona o caractere codificado à frase codificada
        encoded_text += encoded_char

    return encoded_text


def decode(encoded_text, key):
    decoded_text = ""

    # Percorre cada caractere da frase codificada
    for char in encoded_text:
        # Verifica se o caractere é uma letra maiúscula
        if char.isalpha() and char.isupper():
            # Aplica o deslocamento inverso à letra
            decoded_char = chr((ord(char) - 65 - key) % 26 + 65)
        else:
            # Mantém o caractere original
            decoded_char = char

        # Adiciona o caractere descodificado à frase descodificada
        decoded_text += decoded_char

    return decoded_text
def main():
    text = input("Digite a frase a ser codificada: ")
    key = int(input("Digite o deslocamento para a codificação: "))

    encoded_text = encode(text, key)
    print("Frase codificada: ", encoded_text)

    decoded_text = decode(encoded_text, key)
    print("Frase descodificada: ", decoded_text)
    
