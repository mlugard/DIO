# Objetivo geral: Criar um sistema bancário com as oprações: sacar, depositar e visualizar extrato.

# Depósito: Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato

# Saque: O sistema deve permitir realizar 3 saques diários com limite máximo de R$500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mesagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

# Os valores devem ser exibidos utilizando o formato R$xxx.xx


from datetime import datetime

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
num_saques = 0
LIMITE_SAQUES = 3
depositos = []
saques = []

def formatar_moeda(valor):
    return f"R${valor:.2f}"

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Selecionado: Depósito")
        vlr_deposito = float(input("Qual valor deseja depositar? R$"))
        if vlr_deposito > 0:
            saldo += vlr_deposito
            horario_deposito = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            depositos.append((vlr_deposito, horario_deposito))
            print(f"Muito bem, seu saldo atual é de {formatar_moeda(saldo)}")
        else:
            print("Valor de depósito deve ser positivo.")

    elif opcao == "s":
        print("Selecionado: Sacar")
        if num_saques < LIMITE_SAQUES:
            vlr_saque = float(input("Qual valor deseja sacar? R$"))
            if vlr_saque > saldo:
                print("Saldo insuficiente para saque. Tente outro valor.")
            elif vlr_saque > 500:
                print("Não é possível sacar essa quantia, limite de R$500.00. Tente novamente.")
            else:
                saldo -= vlr_saque
                horario_saque = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                saques.append((vlr_saque, horario_saque))
                num_saques += 1
                print(f"Muito bem, seu saldo atual é de {formatar_moeda(saldo)}")
        else:
            print("Limite diário de saques atingido.")

    elif opcao == "e":
        print("Selecionado: Extrato")
        print(f"Saldo atual: {formatar_moeda(saldo)}")
        print("Depósitos:")
        for dep, horario in depositos:
            print(f" - {formatar_moeda(dep)} em {horario}")
        print("Saques:")
        for saq, horario in saques:
            print(f" - {formatar_moeda(saq)} em {horario}")
        
    elif opcao == "q":
        break

    else:
        print("Opção inválida, por favor selecione novamente a opção desejada.")