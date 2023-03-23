import requests
url_api = "http://localhost:3000/produtos"

def titulo(texto, sublinhado="-"):
    print()
    print(texto)
    print(sublinhado*30)

def incluir():
    titulo("Inclusão de Produtos")
    descricao = input("Descrição..: ")
    marca =     input("Marca.....: ")
    quant =   int(input("Quantidade.: "))
    preco = float(input("Preço R$...: "))

    produto = {"descricao": descricao, "marca": marca, "quant": quant, "preco": preco}
    response = requests.post(url_api, json=produto)

    if response.status_code == 201:
        print("Ok. Produto cadastrado com sucesso")
        novo_produto = response.json()
        print(f"Código: {novo_produto['id']}")
   

def listar():
    titulo("Lista de produtos: ")
    response = requests.get(url_api)
    produtos = response.json()
    print("Cód. Descrição do produto......... Marca....... Quant...... Preço......")
    for prod in produtos:
        print(f"{prod['id']:4d}", end=" ")
        print(f"{prod['descricao']:30}",end=" ")
        print(f"{prod['marca']:15}", end=" ")
        print(f"{prod['quant']:6d}", end=" ")
        print(f"{prod['preco']:9.2f}")
    

def alterar():
    titulo("Alteração de Produto")
    id = int(input("Código do produto: "))
    response = requests.get(url_api+"/"+str(id))
    produtos = response.json()
    #if produtos['id'] > 0:
     #   print("A porra do id ta errado ")
        
       
    print(f"Informe os dados apenas dos atributos a serem alterados. Sem alteração => enter")

    print(f"Descrição: {produtos['descricao']}")
    descricao = input("Descricao...:")

    print(f"Marca: {produtos['marca']}")
    marca = input("Marca...:")

    print(f"Quantidade: {produtos['quant']}")
    quant = input("Quantidade...:")

    print(f"Preço: {produtos['preco']}")
    preco = input("Preço...:")

    desc_alt =  descricao if descricao != "" else produtos['descricao']
    marca_alt =  marca if marca != "" else produtos['marca']
    quant_alt =  quant if quant != "" else produtos['quant']
    preco_alt = preco if preco != "" else produtos['preco']

    alt_produto = {"descricao": desc_alt, "marca": marca_alt, "quant": quant_alt, "preco": preco_alt} 
    response2 = requests.put(url_api +"/"+str(id), json=alt_produto)
    if response2.status_code == 200:
        print("deu certo!")
    else:
        print("F:", response2.status_code)



def excluir():
    pass

def pesquisar():
    pass

def estatistica():
    pass

while True:
    titulo("Cadastro de produtos - consome API")
    print("1. Inclusão de produto")
    print("2. Listagem dos produtos")
    print("3. Alterção de produto")
    print("4. Exclusão de produto")
    print("5. Pesquisa por código")
    print("6. Dados estatísticos")
    print("7. Finalizar")
    opcao = int(input("Informe sua opção: "))
    if opcao == 1:
        incluir()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        alterar()
    elif opcao == 4:
        excluir()
    elif opcao == 5:
        pesquisar()
    elif opcao == 6:
        estatistica()
    else:
        break