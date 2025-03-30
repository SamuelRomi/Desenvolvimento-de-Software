import uuid

class Pessoa:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

class Cliente:
    def __init__(self, pessoa):
        self.pessoa = pessoa
        self.id_cliente = str(uuid.uuid4())

class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def calcular_total(self):
        return self.produto.preco * self.quantidade

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []

    def adicionar_item(self, produto, quantidade):
        item = ItemPedido(produto, quantidade)
        self.itens.append(item)
        return "Item adicionado ao carrinho"

    def calcular_total(self):
        total = 0
        for item in self.itens:
            total += item.calcular_total()
        return total 

class Menu:
    def __init__(self):
        self.clientes = {} #Chave é o cpf
        self.produtos = {} #Chave é o nome
        self.pedidos = []

    def cadastrar_cliente(self, nome, cpf, email):
        pessoa = Pessoa(nome, cpf, email)
        cliente = Cliente(pessoa)
        self.clientes[cpf] = cliente
        print(f"\n[✔️] Cliente {nome} cadastrado com sucesso!\n")

    def cadastrar_produto(self, nome, preco, estoque):
        produto = Produto(nome, preco, estoque)
        self.produtos[nome] = produto
        print(f"\n[✔️] Produto {nome} cadastrado com sucesso!\n")

    def criar_pedido(self, cpf):
        if cpf not in self.clientes:
            print(f"\n[❌] Cliente com CPF {cpf} não encontrado!\n")
            return
        cliente = self.clientes[cpf]
        pedido = Pedido(cliente)
        
        while True:
            print("\nDeseja adicionar um item ao pedido?")
            print("1. Sim")
            print("2. Não, finalizar pedido")
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                print("\nProdutos disponíveis:")
                for produto in self.produtos.values():
                    print(f"{produto.nome} - R${produto.preco:.2f} (Estoque: {produto.estoque})")
                
                produto_escolhido = input("\nDigite o nome do produto que deseja adicionar: ")
                
                if produto_escolhido not in self.produtos:
                    print("\n[❌] Produto inválido!")
                    break

                produto = self.produtos[produto_escolhido]
                
                try:    
                    quantidade = int(input(f"\nDigite a quantidade de {produto.nome} que deseja adicionar: "))
                    
                    if quantidade <= 0:
                        print("\n[❌] A quantidade precisa ser maior que 0!")
                        continue
                    
                    if quantidade > produto.estoque:
                        print("\n[❌] Estoque insuficiente!")
                        continue
                    
                    item = ItemPedido(produto, quantidade)
                    pedido.adicionar_item(produto, quantidade)
                    produto.estoque -= quantidade  # Reduzir o estoque
                    print(f"\n[✔️] {quantidade} unidade(s) de {produto.nome} adicionada(s) ao pedido!")
                except ValueError:
                    print("\n[❌] Por favor, insira um número válido para a quantidade.")
            elif opcao == "2":
                break
            else:
                print("\n[❌] Opção inválida, tente novamente!")

        self.pedidos.append(pedido)
        print(f"\n[✔️] Pedido criado para o cliente {cliente.pessoa.nome}!\n")
        return pedido


    def listar_pedidos(self):
        if not self.pedidos:
            print("\n[❌] Nenhum pedido registrado ainda.\n")
            return
        print("\n[📜] Pedidos Registrados:\n")
        for pedido in self.pedidos:
            print(f"Cliente: {pedido.cliente.pessoa.nome}")
            print("Itens:")
            for item in pedido.itens:
                print(f"  - Produto: {item.produto.nome}")
                print(f"    Preço: R${item.produto.preco:.2f}")
                print(f"    Quantidade: {item.quantidade}")
            print(f"Total: R${pedido.calcular_total():.2f}")
            print("-" * 40)

    def exibir_menu(self):
        while True:
            print("\n===================================")
            print("       SISTEMA DE E-COMMERCE       ")
            print("===================================")
            print("1. Cadastrar Cliente")
            print("2. Cadastrar Produto")
            print("3. Criar Pedido")
            print("4. Listar Pedidos")
            print("5. Sair")
            print("===================================")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                nome = input("Nome: ")
                cpf = input("CPF: ")
                email = input("Email: ")
                self.cadastrar_cliente(nome, cpf, email)
            elif opcao == "2":
                nome = input("Nome do Produto: ")
                preco = float(input("Preço do Produto: "))
                estoque = int(input("Estoque do Produto: "))
                self.cadastrar_produto(nome, preco, estoque)
            elif opcao == "3":
                cpf = input("CPF do Cliente: ")
                self.criar_pedido(cpf)
            elif opcao == "4":
                self.listar_pedidos()
            elif opcao == "5":
                print("\n[👋] Saindo... Até logo!")
                break
            else:
                print("\n[❌] Opção inválida, tente novamente.\n")

if __name__ == "__main__":
    menu = Menu()
    menu.exibir_menu()
