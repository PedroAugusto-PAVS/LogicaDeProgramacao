from dataclasses import dataclass # importação da dataclass do módulo dataclasses
@dataclass #decorador para indicar que RegEmbarque terá o comportamento de uma dataclass

class Clientes: #identificador do tipo construído
  Conta: str
  Nome: str
  Saldo: float

#cliente = Clientes()

cadastro=[]

while True:
  print('###################################')
  print('1 - Cadastrar contas\n2 - Ver todas as contas de um cliente\n3 - Excluir conta com menor saldo')
  op=input('Opção: ')
  if op=='0':
    break
  elif op=='1':
    achou=False
    while True:
      print('===============================')
      conta = input('Conta: ')
      if conta == '0':
        break
      for i in range(len(cadastro)):
        if conta==cadastro[i].Conta:
          achou=True
          break
      if achou:
        print('Conta já cadastrada!')
        break
      else:
        cadastro.append(Clientes(conta,input('Cliente: '),float(input('Saldo: '))))

  elif op=='2':
    cliente=input('Cliente: ')
    achou=False
    for i in range (len(cadastro)):
      if cliente == cadastro[i].Nome:
        print(cadastro[i])
        achou=True
    if achou==False:
      print('Cliente não encontrado!')

  elif op=='3':
    menorSaldo=cadastro[0].Saldo
    enderecoMenorSaldo=0
    for i in range(len(cadastro)):
      if cadastro[i].Saldo < menorSaldo:
        menorSaldo=cadastro[i].Saldo
        enderecoMenorSaldo=i
    del(cadastro[i])
    print('Cadastro excluído com sucesso!')

  else:
    print('Opções válidas: 1, 2 ou 3!!')
