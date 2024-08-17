produtos = []
totalProdutos = 0

def adicionarProduto():

  global totalProdutos
  nome = input("Digite o nome do produto: ")
  quantidade = int(input("Digite a quantidade: "))
  valor = float(input("Digite o valor unitário: "))
  total = quantidade * valor
  produtos.append({"produto": nome, "valor": valor, "quantidade": quantidade, "total": total})
  totalProdutos += total
  print(f"Produto {nome} adicionado com sucesso!")

def visualizarLista():

  global totalProdutos
  if not produtos:
    print("A lista de compras está vazia.")
  else:
    print("\nLista de Produtos:")
    for i, produto in enumerate(produtos):
      print(f"{i+1}. {produto['produto']} - Valor Unitário: R$ {produto['valor']:.2f} - Quantidade: {produto['quantidade']} - Total: R$ {produto['total']:.2f}")
    print(f"\nValor total da compra: R$ {totalProdutos:.2f}")

def atualizarProduto():

  global totalProdutos
  nomeProduto = input("Digite o nome do produto que deseja atualizar: ")
  produtoEncontrado = False
  for i, produto in enumerate(produtos):
    if produto['produto'] == nomeProduto:
      produtoEncontrado = True
      print(f"\nProduto encontrado: {produto['produto']}")
      print("Atualize as informações:")
      novoNome = input(f"Novo nome (deixe em branco para manter {produto['produto']}): ")
      novaQuantidade = int(input(f"Nova quantidade (deixe em branco para manter {produto['quantidade']}): "))
      novoValor = float(input(f"Novo valor unitário (deixe em branco para manter R$ {produto['valor']:.2f}): "))

      if novoNome:
        produto['produto'] = novoNome
      if novaQuantidade:
        produto['quantidade'] = novaQuantidade
        produto['total'] = produto['quantidade'] * produto['valor']
      if novoValor:
        produto['valor'] = novoValor
        produto['total'] = produto['quantidade'] * produto['valor']

      totalProdutos -= produto['total']
      totalProdutos += produto['quantidade'] * produto['valor']

      print("Produto atualizado com sucesso!")
      break
  if not produtoEncontrado:
    print("Produto não encontrado na lista.")

def removerProduto():

  global totalProdutos
  nomeProduto = input("Digite o nome do produto que deseja remover: ")
  produtoEncontrado = False
  for i, produto in enumerate(produtos):
    if produto['produto'] == nomeProduto:
      produtoEncontrado = True
      totalProdutos -= produto['total']
      del produtos[i]
      print("Produto removido com sucesso!")
      break
  if not produtoEncontrado:
    print("Produto não encontrado na lista.")

while True:
  print("\n--- Menu ---")
  print("1. Adicionar Produto")
  print("2. Ver Lista de Produtos")
  print("3. Atualizar Produto")
  print("4. Remover Produto")
  print("5. Encerrar Programa")

  opcao = input("Digite a opção desejada: ")

  if opcao == '1':
    adicionarProduto()
  elif opcao == '2':
    visualizarLista()
  elif opcao == '3':
    atualizarProduto()
  elif opcao == '4':
    removerProduto()
  elif opcao == '5':
    print("Encerrando o programa...")
    break
  else:
    print("Opção inválida!")
