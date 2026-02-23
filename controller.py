from models import Categoria, Estoque, Produtos, Fornecedor, Pessoa, Funcionario, Venda
from dao import DaoCategoria, DaoVenda, DaoEstoque, DaoFornecedor, DaoPessoa, DaoFuncionario
from datetime import datetime


# =========================
# CATEGORIA
# =========================

class ControllerCategoria:

    def cadastraCategoria(self, novaCategoria):
        categorias = DaoCategoria.ler()

        for i in categorias:
            if i.categoria == novaCategoria:
                print("Categoria já existe")
                return

        DaoCategoria.salvar(novaCategoria)
        print("Categoria cadastrada com sucesso")

    def removerCategoria(self, categoriaRemover):
        categorias = DaoCategoria.ler()
        novaLista = []

        existe = False

        for i in categorias:
            if i.categoria == categoriaRemover:
                existe = True
            else:
                novaLista.append(i)

        if not existe:
            print("Categoria não existe")
            return

        with open("categoria.txt", "w") as arq:
            for i in novaLista:
                arq.write(i.categoria + "\n")

        print("Categoria removida com sucesso")

    def alterarCategoria(self, categoriaAntiga, categoriaNova):
        categorias = DaoCategoria.ler()
        existe = False

        for i in categorias:
            if i.categoria == categoriaNova:
                print("Categoria nova já existe")
                return

        for i in categorias:
            if i.categoria == categoriaAntiga:
                i.categoria = categoriaNova
                existe = True

        if not existe:
            print("Categoria antiga não encontrada")
            return

        with open("categoria.txt", "w") as arq:
            for i in categorias:
                arq.write(i.categoria + "\n")

        print("Categoria alterada com sucesso")

    def mostrarCategoria(self):
        categorias = DaoCategoria.ler()

        if not categorias:
            print("Categoria vazia")
            return

        for i in categorias:
            print(f"Categoria: {i.categoria}")


# =========================
# ESTOQUE
# =========================

class ControllerEstoque:

    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        estoque = DaoEstoque.ler()
        categorias = DaoCategoria.ler()

        if not any(c.categoria == categoria for c in categorias):
            print("Categoria inexistente")
            return

        if any(e.produto.nome == nome for e in estoque):
            print("Produto já existe")
            return

        produto = Produtos(nome, preco, categoria)
        DaoEstoque.salvar(produto, quantidade)
        print("Produto cadastrado com sucesso")

    def removerProduto(self, nome):
        estoque = DaoEstoque.ler()
        novaLista = []
        existe = False

        for i in estoque:
            if i.produto.nome == nome:
                existe = True
            else:
                novaLista.append(i)

        if not existe:
            print("Produto não encontrado")
            return

        with open("estoque.txt", "w") as arq:
            for i in novaLista:
                arq.write(f"{i.produto.nome}|{i.produto.preco}|{i.produto.categoria}|{i.quantidade}\n")

        print("Produto removido com sucesso")

    def mostrarEstoque(self):
        estoque = DaoEstoque.ler()

        if not estoque:
            print("Estoque vazio")
            return

        for i in estoque:
            print("---------------")
            print(f"Nome: {i.produto.nome}")
            print(f"Preço: {i.produto.preco}")
            print(f"Categoria: {i.produto.categoria}")
            print(f"Quantidade: {i.quantidade}")


# =========================
# VENDA
# =========================

class ControllerVenda:

    def cadastrarVenda(self, nomeProduto, vendedor, comprador, quantidadeVendida):
        estoque = DaoEstoque.ler()
        novaLista = []

        existe = False
        quantidade_ok = False
        valorCompra = 0

        for i in estoque:
            if i.produto.nome == nomeProduto:
                existe = True

                if int(i.quantidade) >= int(quantidadeVendida):
                    quantidade_ok = True
                    i.quantidade = int(i.quantidade) - int(quantidadeVendida)

                    valorCompra = int(quantidadeVendida) * int(i.produto.preco)

                    venda = Venda(
                        Produtos(i.produto.nome, i.produto.preco, i.produto.categoria),
                        vendedor,
                        comprador,
                        quantidadeVendida
                    )

                    DaoVenda.salvar(venda)

            novaLista.append(i)

        if not existe:
            print("Produto não existe")
            return

        if not quantidade_ok:
            print("Quantidade insuficiente")
            return

        with open("estoque.txt", "w") as arq:
            for i in novaLista:
                arq.write(f"{i.produto.nome}|{i.produto.preco}|{i.produto.categoria}|{i.quantidade}\n")

        print("Venda realizada com sucesso")
        print(f"Valor total: {valorCompra}")

    def relatorioProdutos(self):
        vendas = DaoVenda.ler()
        contador = {}

        for v in vendas:
            nome = v.itensVendido.nome
            qtd = int(v.quantidadeVendida)

            if nome in contador:
                contador[nome] += qtd
            else:
                contador[nome] = qtd

        ordenado = sorted(contador.items(), key=lambda x: x[1], reverse=True)

        print("Produtos mais vendidos:")
        for i, (nome, qtd) in enumerate(ordenado, 1):
            print(f"{i}º - {nome} | Quantidade: {qtd}")

    def mostrarVenda(self, dataInicio, dataTermino):
        vendas = DaoVenda.ler()

        dataInicio = datetime.strptime(dataInicio, "%d/%m/%Y")
        dataTermino = datetime.strptime(dataTermino, "%d/%m/%Y")

        total = 0

        for v in vendas:
            dataVenda = datetime.strptime(v.data, "%d/%m/%Y")

            if dataInicio <= dataVenda <= dataTermino:
                print("--------------")
                print(f"Produto: {v.itensVendido.nome}")
                print(f"Cliente: {v.comprador}")
                print(f"Vendedor: {v.vendedor}")
                print(f"Data: {v.data}")
                print(f"Quantidade: {v.quantidadeVendida}")

                total += int(v.itensVendido.preco) * int(v.quantidadeVendida)

        print(f"Total vendido: {total}")


# =========================
# FORNECEDOR
# =========================

class ControllerFornecedor:

    def cadastrarFornecedor(self, nome, cnpj, telefone, categoria):
        fornecedores = DaoFornecedor.ler()

        for f in fornecedores:
            if f.cnpj == cnpj:
                print("CNPJ já existe")
                return

        DaoFornecedor.salvar(Fornecedor(nome, cnpj, telefone, categoria))
        print("Fornecedor cadastrado com sucesso")


# =========================
# CLIENTE
# =========================

class ControllerCliente:

    def cadastrarCliente(self, nome, telefone, cpf, email, endereco):
        clientes = DaoPessoa.ler()

        for c in clientes:
            if c.cpf == cpf:
                print("CPF já cadastrado")
                return

        DaoPessoa.salvar(Pessoa(nome, telefone, cpf, email, endereco))
        print("Cliente cadastrado com sucesso")


# =========================
# FUNCIONARIO
# =========================

class ControllerFuncionario:

    def cadastrarFuncionario(self, clt, nome, telefone, cpf, email, endereco):
        funcionarios = DaoFuncionario.ler()

        for f in funcionarios:
            if f.cpf == cpf or f.clt == clt:
                print("Funcionário já cadastrado")
                return

        DaoFuncionario.salvar(Funcionario(clt, nome, telefone, cpf, email, endereco))
        print("Funcionário cadastrado com sucesso")