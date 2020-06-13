from classes.contaPoupanca import ContaPoupanca
from classes.conta import Conta
from classes.contaCorrente import ContaCorrente

cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(10)
cp.sacar(5)
cp.sacar(5)
cp.sacar(1)

# Não pode instanciar classe abstrata
#conta = Conta(1111, 2222, 0)

print('###############')

contaC = ContaCorrente(agencia=1111, conta=3333, saldo=0, limite=500)
contaC.depositar(100)
contaC.sacar(250)
contaC.sacar(500)
