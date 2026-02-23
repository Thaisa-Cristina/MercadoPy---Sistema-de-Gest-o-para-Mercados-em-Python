# 🛒 MercadoPy - Sistema de Gestão de Mercado (Backend CLI)

Sistema backend de gerenciamento para mercados desenvolvido em **Python**, utilizando arquitetura baseada em separação de responsabilidades e persistência em arquivos.

Projeto focado em aplicação prática de:

- Programação Orientada a Objetos (POO)
- Arquitetura MVC
- Manipulação de arquivos
- Regras de negócio
- Estrutura modular
- Organização de backend

---

## 🎯 Objetivo do Projeto

Desenvolver um sistema backend completo para gestão de mercado, contemplando:

- Controle de categorias
- Controle de estoque
- Registro de vendas
- Relatórios
- Gestão de clientes, fornecedores e funcionários

O projeto foi desenvolvido com foco em consolidar fundamentos sólidos de backend.

---

## 🏗 Arquitetura

O sistema segue uma estrutura inspirada em MVC:

```
models.py      → Entidades e regras estruturais
dao.py         → Persistência em arquivos (Data Access Layer)
controller.py  → Regras de negócio
view.py        → Interface CLI
```

### 🔹 Models
Responsáveis por representar as entidades do sistema:

- Categoria
- Produto
- Estoque
- Venda
- Fornecedor
- Pessoa
- Funcionário

### 🔹 DAO (Data Access Object)
Camada responsável por:

- Persistência em arquivos `.txt`
- Leitura e escrita de dados
- Conversão entre texto e objetos

### 🔹 Controller
Contém:

- Validações
- Regras de negócio
- Processamento de vendas
- Relatórios
- Controle de estoque

---

## ⚙ Funcionalidades

### 📦 Categorias
- Cadastrar
- Alterar
- Remover
- Listar

### 🏬 Estoque
- Cadastrar produto
- Remover produto
- Visualizar estoque

### 💰 Vendas
- Registrar venda
- Atualizar estoque automaticamente
- Calcular total vendido
- Relatório de produtos mais vendidos
- Filtro por período de datas

### 👥 Gestão de Pessoas
- Cadastro de clientes
- Cadastro de fornecedores
- Cadastro de funcionários

---

## 🧠 Conceitos Aplicados

- Programação Orientada a Objetos
- Encapsulamento
- Separação de responsabilidades
- Arquitetura modular
- Manipulação de arquivos
- Estruturação de regras de negócio
- Processamento de dados

---

## 🗂 Estrutura do Projeto

```
MercadoPy/
│
├── controller.py
├── dao.py
├── models.py
├── view.py
│
├── categoria.txt
├── clientes.txt
├── estoque.txt
├── fornecedores.txt
├── funcionarios.txt
├── venda.txt
```

---

## ▶ Como Executar

Clone o repositório:

```bash
git clone https://github.com/seuusuario/MercadoPy.git
```

Entre na pasta:

```bash
cd MercadoPy
```

Execute o sistema:

```bash
python view.py
```

---

## 🚀 Melhorias Futuras

- Migrar persistência para banco de dados (SQLite ou PostgreSQL)
- Implementar camada de serviços
- Criar API REST com Flask ou FastAPI
- Criar testes automatizados
- Implementar autenticação de usuários
- Dockerização do projeto

---

## 📈 Aplicação para Portfólio

Este projeto demonstra:

✔ Organização backend  
✔ Aplicação de arquitetura MVC  
✔ Separação clara de responsabilidades  
✔ Controle de regras de negócio  
✔ Manipulação de dados estruturados  

Projeto ideal para demonstrar fundamentos sólidos em Python backend.

---

---

⭐ Caso tenha gostado do projeto, deixe uma estrela!
