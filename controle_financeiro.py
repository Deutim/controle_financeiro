
import json

cadastrar = 1
saldo = 2
extrato = 3
sair = 0

# Tentando carregar as transações do arquivo JSON
try:
    with open("transacoes.json", "r") as arquivo:
        lista_transacao = json.load(arquivo)
except FileNotFoundError:
    lista_transacao = []

escolhendo_operacao = -1

while escolhendo_operacao != 0:

    print("""
    ========== CONTROLE FINANCEIRO ==========
      
    1 - Cadastrar 
    2 - Saldo
    3 - Extrato
    0 - Sair
      
    =========================================
    """)
 
    escolhendo_operacao = int(input("Selecione a operação desejada: "))

    if escolhendo_operacao == 1:
        tipo_transacao = input("Selecione o tipo de transação (R para Receita, D para Despesa): ").upper()
        descricao = input("Descreva a transação: ")
        valor = float(input("Digite o valor da transação: "))

        if tipo_transacao == "D":
            valor = -valor

        transacao_item = {
            "descricao": descricao,
            "valor": valor
        }

        lista_transacao.append(transacao_item)

        # Salvar no arquivo JSON a cada nova transação
        with open("transacoes.json", "w") as arquivo:
            json.dump(lista_transacao, arquivo, indent=4)

        print("Transação registrada com sucesso!")

    elif escolhendo_operacao == 2:
        saldo_total = sum(t["valor"] for t in lista_transacao)
        print(f"Saldo total: {saldo_total}")

    elif escolhendo_operacao == 3:
        if not lista_transacao:
            print("Nenhuma transação registrada no momento!")
        else:
            for t in lista_transacao:
                print(f'Descrição: {t["descricao"]} | Valor: {t["valor"]}')

    elif escolhendo_operacao == 0:
        print("Saindo do sistema, até logo!")
        break

    else:
        print("Operação inválida, tente novamente!")