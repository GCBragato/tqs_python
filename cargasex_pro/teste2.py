class arroz:
    def __init__(self,tamanho):
        self.tamanho = tamanho
        self.nome = "arroz"
        self.preco = 10.0

    def getNome(self):
        return self.nome

    def getPreco(self):
        return self.preco

rice = arroz(222)
print(rice.tamanho)