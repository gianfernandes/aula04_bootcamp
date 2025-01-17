#Armazenar informações de um livro (título, autor e ano de publicação) e imprimir cada informação
campos_livro: list = ["Titulo", "Autor", "Ano"]
livro: dict = dict.fromkeys(campos_livro)

print("######### Informações do livro #########")

livro["Titulo"] = input("> Insira o título do livro: ")
livro["Autor"] = input("> Insira o autor do livro: ")
livro["Ano"] = int(input("> Em que ano esse livro foi publicado? "))

print(f"O livro informado é: {livro['Titulo']}")
print(f"Foi escrito pelo(a) escritor(a): {livro['Autor']}")
print(f"Lançado no ano: {livro['Ano']}")