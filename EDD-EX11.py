class Pessoa:

    def __init__(self):
        pass


    def setNome(self, nome):
        self.nome = nome

    def setIdade(self, idade):
        self.idade = idade

    def setPeso(self, peso):
        self.peso = peso

    def setSexo(self, sexo):
        self.sexo = sexo

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade

    def getPeso(self):
        return self.peso

    def getSexo(self):
        return self.sexo

    def imprimir(self):
        return "Nome: " + str(self.getNome()) + "| Idade : " + self.getIdade() + "| Peso: " + self.getPeso() + "| Sexo: " + self.getSexo()


def inserirNaFila(fila):
     nome = (input("Informe o nome: "))
     string = nome
     string = Pessoa()
     string.setNome(nome)
     string.setIdade(input("Digite a idade: "))
     string.setPeso(input("Digite o peso: "))
     string.setSexo(input("Digite o Sexo: "))
     fila.append(string)
     print("\n" + string.getNome()+" inserida no final da fila com sucesso\n")


def excluirdaFila(fila):
    if len(fila) == 0:
        print("Fila vazia")
    else:
        print("\n" + str(fila[0].getNome()) + " foi excluído com sucesso\n")
        del fila[0]



def imprimirFila(fila):
    if filaEstaVazia(fila):
        print("Fila vazia")
    else:
        print("\n===== Fila: =====\n")
        for numeroTmp in fila:
            print(numeroTmp.imprimir())



def tamanhoFila(fila):
    if (len(fila) == 0):
        return 0
    else:
        return len(fila)



def filaEstaVazia(fila):
    statusFila = (tamanhoFila(fila) == 0)
    return statusFila


print("===== Aplicação que simula uma fila ====")

fila = []
opcao = 1

while opcao != 0:
    opcao = int(input("\n1 - Inserir\n" +
                      "2 - Excluir\n" +
                      "3 - Imprimir\n" +
                      "4 - Informar tamanho da fila\n" +
                      "5 - Informar se a fila esta vazia\n" +
                      "6 - Pesquisar posição por nome\n" +
                      "0 - Sair\n" +
                      "Informe uma opção: "))
    if opcao == 1:

        inserirNaFila(fila)
    elif opcao == 2:
        excluirdaFila(fila)
    elif opcao == 3:
        imprimirFila(fila)
    elif opcao == 4:
        print(f"\nTamanho Fila: {tamanhoFila(fila)}")
    elif opcao == 5:
        if(filaEstaVazia(fila) == True):
            print(f"Fila esta fazia")
        else:
            print(f"\nFila não esta fazia e possui: {tamanhoFila(fila)} elemento(s)")
    elif opcao == 6:
        nomepesq = input("Digite o nome: ")
        x = 0
        if (filaEstaVazia(fila) == True):
            print("Fila esta fazia")
        else:
            p = 0
            for i in fila:
                x += 1
                if i.getNome() == nomepesq:
                    p = x

            if p != 0:
                print('Essa pessoa é a ' + str(p) + "ª da fila")
            else:
                print("Essa pessoa não esta na fila")

    elif opcao == 0:
        print("===== Fim ===== ")
    else:
        print("Opção inválida")