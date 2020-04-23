from classes import Escritor, Caneta, Maquina_De_Escrever

escritor1 = Escritor('Paulo')
caneta1 = Caneta('Bic')
maquina1 = Maquina_De_Escrever()


# ferramenta recebeu um objeto inteiro, maquina1
escritor1.ferramenta = maquina1
# Sendo assim, agora ferramenta possui maquina1 e pode acessar seus métodos
escritor1.ferramenta.escrever()
