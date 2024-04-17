class Pessoa(object):
    def __init__(self,nome,id_numero):
        self.nome = nome 
        self.id_numero = id_numero

    def mostrar(self):
        print(self.nome)
        print(self.id_numero)

    def detalhar_pessoa(self):
        print(f'Meu nome é {self.nome}')
        print(f'Meu cpf é {self.id_numero}')

class Empregado(Pessoa):
    def __init__(self, nome, id_numero,salario,setor):
        Pessoa.__init__(nome, id_numero)
        self.salario = salario 
        self.setor = setor 

    def detalhar(self):
       print(f'meu nome é {self.nome} e meu salario é {self.salario}')

empregado_1 = Empregado('Paulinho','123','1200','Logistica')


empregado_1.detalhar()
empregado_1.detalhar_pessoa()
