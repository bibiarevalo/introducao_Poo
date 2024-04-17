class Base(object):
    def __init__(self):
        self.a = 'Senai'
        self.__b = 'São Jose'
    
    def imprime_b(self):
        print('Chamando membro privado da classe base')
        print(self.__b)


class Derivada(Base):

    def __init__(self):
        Base.__init__(self)


obj_1 = Base()
print(obj_1.a)
obj_2 = Derivada()
obj_2.imprime_b()