
# conta_bancaria.py

# Função para criar uma conta bancária
def cria_conta(numero, titular, saldo, limite):
    conta = {
        'numero': numero,
        'titular': titular,
        'saldo': saldo,
        'tipo_conta': 'Conta Corrente',  # Você pode definir o tipo de conta aqui
        'limite': limite
    }
    return conta

# Função para depositar em uma conta
def deposita(conta, valor):
    conta['saldo'] += valor

# Função para sacar de uma conta
def saca(conta, tipo_conta, valor):
    if tipo_conta == 'Conta Corrente':
        if valor <= conta['saldo'] + conta['limite']:
            conta['saldo'] -= valor
        else:
            print('Saldo insuficiente.')
    elif tipo_conta == 'Conta Poupança':
        if valor <= conta['saldo']:
            conta['saldo'] -= valor
        else:
            print('Saldo insuficiente.')
    else:
        print('Tipo de conta inválido.')

# Função para imprimir o extrato de uma conta
def extrato(conta):
    print(f'Número da conta: {conta["numero"]}')
    print(f'Saldo atual: R${conta["saldo"]:.2f}')

# Exemplo de uso
if __name__ == "__main__":
    minha_conta = cria_conta('12345-6', 'João', 1000.0, 500.0)
    
    deposita(minha_conta, 200.0)
    extrato(minha_conta)
    
    saca(minha_conta, 'Conta Corrente', 300.0)
    extrato(minha_conta)
    
    saca(minha_conta, 'Conta Poupança', 800.0)
    extrato(minha_conta)