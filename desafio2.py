# Objetivo geral: Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária

# Criar Usuário (cliente): o programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro, número - bairro - cidade/sigla estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

# Cadastrar Conta bancária: O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fico "0001". O usuário pode ter mais de uma conta, mas uma conta pertence somente a um usuário.

# Opcional: função listar_contas()

from datetime import datetime

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[u] Cadastrar Usuário
[c] Cadastrar Conta Bancária
[l] Listar Contas

=> """

class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.num_saques = 0
        self.LIMITE_SAQUES = 3
        self.depositos = []
        self.saques = []

    def formatar_moeda(self, valor):
        return f"R${valor:.2f}"

    def deposito(self):
        vlr_deposito = float(input("Qual valor deseja depositar? R$"))
        if vlr_deposito > 0:
            self.saldo += vlr_deposito
            horario_deposito = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.depositos.append((vlr_deposito, horario_deposito))
            print(f"Muito bem, seu saldo atual é de {self.formatar_moeda(self.saldo)}")
        else:
            print("Valor de depósito deve ser positivo.")

    def saque(self):
        if self.num_saques < self.LIMITE_SAQUES:
            vlr_saque = float(input("Qual valor deseja sacar? R$"))
            if vlr_saque > self.saldo:
                print("Saldo insuficiente para saque. Tente outro valor.")
            elif vlr_saque > 500:
                print("Não é possível sacar essa quantia, limite de R$500.00. Tente novamente.")
            else:
                self.saldo -= vlr_saque
                horario_saque = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.saques.append((vlr_saque, horario_saque))
                self.num_saques += 1
                print(f"Muito bem, seu saldo atual é de {self.formatar_moeda(self.saldo)}")
        else:
            print("Limite diário de saques atingido.")

    def exibir_extrato(self):
        print(f"Saldo atual: {self.formatar_moeda(self.saldo)}")
        print("Depósitos:")
        for dep, horario in self.depositos:
            print(f" - {self.formatar_moeda(dep)} em {horario}")
        print("Saques:")
        for saq, horario in self.saques:
            print(f" - {self.formatar_moeda(saq)} em {horario}")

class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

usuarios = []
contas = []
numero_conta = 1

def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
    cpf = input("Digite o CPF (apenas números): ")
    
    for usuario in usuarios:
        if usuario.cpf == cpf:
            print("CPF já cadastrado. Tente novamente.")
            return
    
    endereco = input("Digite o endereço (logradouro, número - bairro - cidade/sigla estado): ")
    usuario = Usuario(nome, data_nascimento, cpf, endereco)
    usuarios.append(usuario)
    print(f"Usuário '{nome}' cadastrado com sucesso.")

def criar_conta():
    global numero_conta
    if not usuarios:
        print("Nenhum usuário cadastrado. Cadastre um usuário primeiro.")
        return
    cpf = input("Digite o CPF do usuário para cadastrar a conta: ")
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario.cpf == cpf:
            usuario_encontrado = usuario
            break
    if usuario_encontrado:
        contas.append({
            'agencia': '0001',
            'numero_conta': numero_conta,
            'usuario': usuario_encontrado,
            'conta': ContaBancaria()
        })
        print(f"Conta cadastrada com sucesso! Número da conta: {numero_conta}")
        numero_conta += 1
    else:
        print("Usuário não encontrado. Verifique o CPF.")

def listar_contas():
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    print("Contas cadastradas:")
    for conta in contas:
        print(f"Agência: {conta['agencia']}, Número da Conta: {conta['numero_conta']}, Usuário: {conta['usuario'].nome}")


conta = ContaBancaria()

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Selecionado: Depósito")
        conta_index = int(input("Digite o número da conta: ")) - 1
        if conta_index < len(contas):
            contas[conta_index]['conta'].deposito()
        else:
            print("Conta não encontrada.")

    elif opcao == "s":
        print("Selecionado: Sacar")
        conta_index = int(input("Digite o número da conta: ")) - 1
        if conta_index < len(contas):
            contas[conta_index]['conta'].saque()
        else:
            print("Conta não encontrada.")

    elif opcao == "e":
        print("Selecionado: Extrato")
        conta_index = int(input("Digite o número da conta: ")) - 1
        if conta_index < len(contas):
            contas[conta_index]['conta'].exibir_extrato()
        else:
            print("Conta não encontrada.")

    elif opcao == "u":
        print("Selecionado: Cadastrar Usuário")
        criar_usuario()

    elif opcao == "c":
        print("Selecionado: Cadastrar Conta Bancária")
        criar_conta()

    elif opcao == "l":
        print("Selecionado: Listar Contas")
        listar_contas()

    elif opcao == "q":
        break

    else:
        print("Opção inválida, por favor selecione novamente a opção desejada.")