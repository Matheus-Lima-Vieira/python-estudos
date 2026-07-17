import re
'''
1 - Adicionar produto
2 - Listar produtos
3 - Buscar produto
4 - Atualizar quantidade
5 - Remover produto
6 - Sair
'''
#Lista para testes

lista = [
    ["Mouse", 10, 89.90],
    ["Teclado", 5, 199.90],
    ["Monitor", 3, 899.90]
]

#lista = []
while True:
    print("==== ESTOQUE ====")
    selecao = input("1 - Adicionar produto\n" \
                    "2 - Listar produtos\n" \
                    "3 - Buscar produto\n" \
                    "4 - Alterar produto\n" \
                    "5 - Remover produto\n" \
                    "6 - Sair\n")
    if selecao == "1":
        while True:
            print("==== ESTOQUE ====")
            produto = re.sub(r'[^a-zA-Zá-úÁ-Ú]', ' ', input("Qual produto deseja adicionar?\n")).strip().title()
            quantidade = int(re.sub('[^0-9]', '', (input("Qual a quantidade desse produto?\n"))))
            #preco = float(re.sub('[^0-9]', '', (input("Qual o valor do produto?\n"))))
            preco = float(input("Qual o valor do produto? \n"))
            lista.append([produto, quantidade, preco])
            opcao = input("Deseja adicionar mais um produto? Sim / Não\n").strip().lower()
            if opcao != "sim":
                break
    elif selecao == "2":
        print("==== ESTOQUE ====")
        if not lista:
            print("Nenhum produto cadastrado")
        else:
            for estoque in lista:
                #print(lista)
                print((f"Item: {estoque[0]}\n") + 
                      (f"Quantidade: {estoque[1]} \n") +  
                      (f"Preço: {estoque[2]}\n"))
    elif selecao == "3":
        print("==== ESTOQUE ====")
        busca = input("Qual produto deseja procurar? \n").strip().title()
        busca_produto = False
        for produto in lista:
            if busca == {produto[0]}:
                busca_produto = True
                print(("\n Produto encontrado! \n") +
                     (f"Produto: {produto[0]}") +
                     (f"Quantidade: {produto[1]}") +
                     (f"Preço: {produto[2]}"))
                break
        if not busca:
            print("Produto não encontrado!")
    elif selecao == "4":
        print("==== ESTOQUE ====")
        print("Qual produto deseja alterar?\n")
        for produto in lista:
            print(f"Nome: {produto[0]}")
        alterar = input().strip().title()
        #Aqui vai buscar o produto digitado
        busca_produto = False
        for produto in lista:
            if alterar == produto[0]:
                busca_produto = True
                break
        if not busca_produto:
            print("Produto não encontrado!")
        #Novo submenu
        subselecao = input(("O que deseja alterar?\n") +
                           ("1 - Alterar o nome\n") +
                           ("2 - Alterar a quantidade\n") +
                           ("3 - Alterar preço\n"))
        if subselecao == "1":
            print("==== ESTOQUE ====")
            subnome = input("Qual o novo nome do produto?\n")
        #Aqui vai pegar o nome buscado na lista e alterar
        elif subselecao == "2":
            print("==== ESTOQUE ====")
            subquantidade = input("Qual a nova quantidade?\n")
        #Aqui vai pegar a quantidade produto buscado na lista e alterar
        elif subselecao =="3":
            print("==== ESTOQUE ====")
            subpreco = input("Qual o novo preço?\n")
            #Aqui vai pegar preco do produto buscado na lista e alterar