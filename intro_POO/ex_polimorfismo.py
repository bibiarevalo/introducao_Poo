class Passaro(object):

    def introducao(self):
        print('existem muitos tipos de passaros')

    def voar(self):
        print('A maioria dos passaros voam')

class Avestruz(Passaro):
    def voar(self):
        print('Avestruzes não voam')

class Pardal(Passaro):
    def voar(self):
        print('pardais voam')


avestruz = Avestruz()
pardal = Pardal()
passaro = Passaro()

passaro.introducao()
passaro.voar()
avestruz.introducao()
avestruz.voar()
pardal.introducao()
pardal.voar()
        