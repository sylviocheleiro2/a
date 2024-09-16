# # print("Entrada Numerica")

# # while True:
# #     try:
# #         n1 = int(input("Digite o numero 1: "))
# #         n2 = int(input("Digite o numero 2: "))
# #         a = n1 + n2
# #     except ValueError:
# #         pass
# #         print("Erro de valor, verifique o numero e tente novamente")
# #     else:
# #         print(f"A soma dos valores de {n1} + {n2} é igual a {a}")


# def abrir_arquivos(filename):
#     try:
#         with open(file=filename, mode="r") as file:
#             conteudo = file.read()
#             animais = conteudo.split()
#     except FileNotFoundError:
#         print("Erro ao encontrar arquivo")

#     else:
#         for animal in animais:
#             print(animal)


# abrir_arquivos("cat.txt")

# Nome do arquivo e parâmetros
nome_arquivo = "little_women.txt"
titulo_capitulo2 = "CHAPTER TWO: A MERRY CHRISTMAS"
palavra_a_contar = "mother"
palavra_a_contar2 = "Mother"
fim_capitulo2 = "CHAPTER THREE"

try:
    with open(nome_arquivo, "r", encoding="UTF-8") as file:
        conteudo = file.read()

        # Encontrar o início do Capítulo 2
        inicio_capitulo = conteudo.find(titulo_capitulo2)
        if inicio_capitulo == -1:
            print("Capítulo não encontrado.")
        else:
            # Encontrar o início do próximo capítulo
            inicio_fim_capitulo = conteudo.find(
                fim_capitulo2, inicio_capitulo + len(titulo_capitulo2))
            if inicio_fim_capitulo == -1:
                inicio_fim_capitulo = len(conteudo)

            # Extrair o texto do Capítulo 2
            texto_capitulo = conteudo[inicio_capitulo:inicio_fim_capitulo]

            # Contar a ocorrência da palavra
            contagem = texto_capitulo.lower().split().count(palavra_a_contar.lower())
            contagem2 = texto_capitulo.lower().split().count(palavra_a_contar2.lower())
            print(contagem2)
            print(f"A palavra '{palavra_a_contar}' aparece {
                  contagem} vezes no {titulo_capitulo2}.")

except FileNotFoundError:
    print("Arquivo não encontrado.")
