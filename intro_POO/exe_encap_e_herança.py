class Animal (object):
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def emitir_som(self):
        print (f'O animal emite som!')

class Cachorro(Animal):
    def __init__(self, nome, especie, raca):
        Animal.__init__(nome, especie)
        self.__raca = 'salsicha'

    def obter_raca(self, .__raca):
        print(f'O cachorro é da raça {self.__raca}')    