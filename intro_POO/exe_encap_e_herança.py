class Animal (object):
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def emitir_som(self):
        print (f'O animal emite som!')

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, especie = "Cachoro")
        self.__raca = raca

    def obter_raca(self):
        return f'O cachorro é da raça {self.__raca}'
    
    def emitir_som(self):
        return "Au"

class Gato(Animal):
    def __init__(self, nome, pelagem):
        super().__init__(nome, "Gato")
        self.__pelagem = pelagem

    def emitir_som(self):
        return 'Miau'
    
    def obter_pelagem(self):
        return self.__pelagem

gato = Gato("Luana Carolina Vasconcelos Vegananis", "Parda")
print(gato.obter_pelagem())
print(gato.emitir_som())

cachorro = Cachorro("Nina Roberta Carla", "Caramelo")
print(cachorro.obter_raca())
print(cachorro.emitir_som())
        
