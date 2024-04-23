def func_deposito(saldo, valor, extrato, /):
  saldo = saldo + valor
  extrato = extrato + f'+ R$ {valor}\n'
  print(f'Você depositou R$ {valor}.')

  return saldo, extrato


def func_saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
  if numero_saques == limite_saques:
    print('Você já atingiu o limite diário de saques (3 saques).')
  elif valor > saldo:
    print('Você não possui saldo suficiente para realizar este saque.')
  elif valor <= limite:
    saldo = saldo - valor
    numero_saques = numero_saques + 1
    extrato = extrato + f'- R$ {valor}\n'
    print(f'Você sacou R$ {valor}.')
  else:
    print('O valor do seu saque é maior do que o permitido (R$ 500.00).')

  return saldo, extrato, numero_saques


def func_extrato(saldo, /, *, extrato):
  if extrato == f'Saldo inicial = R$ {saldo}\n':
    print('Não foram realizadas movimentações.')
  else:
    print(extrato + f'Saldo atual: R$ {saldo}')

  return saldo, extrato

def func_cadastrar_usuario(lista_clientes, cpf):
  for cliente in lista_clientes:
    if cliente['cpf'] == cpf:
      print('Não foi possível cadastrar o usuário: Já existe um usuário com este CPF.')
      return 1

  nome = input('Informe seu nome: ')
  nascimento = input('Informe sua data de nascimento: ')
  endereco = input('Informe seu endereco (logradouro, nº - bairro - cidade/sigla do estado): ')

  lista_clientes.append({'nome': nome, 'data de nascimento': nascimento, 'cpf': cpf, 'endereco': endereco})
  print('Usuário cadastrado com sucesso!')

def func_criar_conta(lista_contas, lista_clientes, cpf, conta):
  if cpf not in [cliente['cpf'] for cliente in lista_clientes]:
    print('O CPF informado não está cadastrado no sistema de clientes.')
    return 1

  lista_contas.append({'agencia': '0001', 'conta': conta, 'cpf': cpf})
  print('Conta criada com sucesso!')

  return True

def main():
  saldo = 0.0
  LIMITE = 500.0
  extrato = f'Saldo inicial: R$ {saldo}\n'
  numero_saques = 0
  LIMITE_SAQUES = 3
  clientes = []
  contas = []
  conta = 1

  print('Bem-vindo ao Python Bank!')

  while True:
    escolha = input('''
    Escolha uma opção:
    [D] Depósito.
    [S] Saque.
    [E] Extrato.
    [C] Cadastrar usuário.
    [A] Criar conta.
    [0] Sair.
    ''')

    if escolha.upper() == 'D':
      deposito = float(input('Indique o valor a ser depositado: '))
      saldo, extrato = func_deposito(saldo, deposito, extrato)

    elif escolha.upper() == 'S':
      saque = float(input('Indique o valor a ser sacado: '))
      saldo, extrato, numero_saques = func_saque(saldo=saldo, valor=saque, extrato=extrato, limite=LIMITE, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

    elif escolha.upper() == 'E':
      func_extrato(saldo, extrato=extrato)

    elif escolha.upper() == 'C':
      cpf = input('Para prosseguir, informe seu CPF: ')
      func_cadastrar_usuario(clientes, cpf)

    elif escolha.upper() == 'A':
      cpf = input('Para prosseguir, informe seu CPF: ')
      if func_criar_conta(contas, clientes, cpf, conta) == True:
        conta = conta + 1

    elif escolha == '0':
      break

    else:
      print('Escolha inválida.')

main()
