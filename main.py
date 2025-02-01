# abre e lê um arquivo texto, retorna o conteúdo
def read_book(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return (file_contents)
    
# conta a qtd de palavras na string
def count_words(texto):
    word_count = 0
    words = texto.split()
    for word in words:
        word_count+=1

    return (word_count)

# conta qtd de cada caracter no texto
def conta_char(texto):
    contador_dict = {}

    #converte o texto todo para lowercase
    texto_lc = texto.lower()
    # vai de char em char na string
    for char in texto_lc:
        # print(char)        
        # se char não é chave no dict, adiciona e conta 1
        if char not in contador_dict:
            contador_dict[char] = 1
        else:
            contador_dict[char] += 1        
    #print(contador_dict)

    return contador_dict

# produz um relatório
def mostra_report(contagem, dict_contagem, arquivo):
    print(f"--- Begin report of {arquivo} ---")
    print(F"{contagem} words found in the document")
    for entrada in dict_contagem:
        if (entrada in {"a", "b","c","d","e","f","g","h","i","j","k","l","m","n","t","u","v","w","x","y","z"}):
            print(f"The '{entrada}' character was found {dict_contagem[entrada]} times")
    return None


# passa o caminho para o arquivo, chama a função que lê e imprime o conteúdo
def main():
    path_to_file = "books/frankenstein.txt"
    file_content = read_book(path_to_file)
    # print(file_content)
    # print(count_words(file_content))
    # print(conta_char(file_content))
    contagem_words = count_words(file_content)
    relatorio_dict = conta_char(file_content)
    mostra_report(contagem_words, relatorio_dict, path_to_file)

main()
