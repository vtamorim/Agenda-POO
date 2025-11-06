import json
from models.dao import DAO
class Profissional:
    def __init__(self, id, nome, especialidade, conselho, email, senha, disponivel):
        self.set_id(id)
        self.set_nome(nome)
        self.set_especialidade(especialidade)
        self.set_conselho(conselho)
        self.set_email(email)
        self.set_senha(senha)
        self.set_disponivel(disponivel)

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_especialidade(self): return self.__especialidade
    def get_conselho(self): return self.__conselho
    def get_email(self): return self.__email    
    def get_senha(self): return self.__senha
    def get_disponivel(self): return self.__disponivel

    def set_id(self, id): self.__id = id
    def set_nome(self, nome): self.__nome = nome
    def set_especialidade(self, especialidade): self.__especialidade = especialidade
    def set_conselho(self, conselho): self.__conselho = conselho
    def set_email(self, email): self.__email = email
    def set_senha(self, senha): self.__senha = senha
    def set_disponivel(self,disponivel): self.__disponivel = disponivel
    def to_json(self):
        dic = {"id":self.__id, "nome":self.__nome, "especialidade":self.__especialidade, "conselho":self.__conselho, "email":self.__email, "senha":self.__senha,"disponivel": self.__disponivel}
        return dic
    
    @staticmethod
    def from_json(dic):
        return Profissional(dic["id"], dic["nome"], dic["especialidade"], dic["conselho"], dic["email"], dic["senha"],dic["disponivel"])

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__especialidade} - {self.__conselho} - {self.__email} - {self.__senha} - {self.__disponivel}"

class ProfissionalDAO(DAO):
    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open("profissional.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Profissional.from_json(dic)
                    cls._objetos.append(obj)

        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("profissional.json", mode="w") as arquivo:
            json.dump(cls._objetos, arquivo, default = Profissional.to_json)