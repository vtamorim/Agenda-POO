from models.servico import Servico, ServicoDAO

class View:

    def Servico_inserir(descricao, valor):
        Servicos = Servico(0, descricao, valor)
        ServicoDAO.inserir(Servicos)

    def Servico_listar():
        return ServicoDAO.listar()
  
    def Servico_listar_id(id):
        return ServicoDAO.listar_id(id)

    def Servico_atualizar(id, descricao, valor):
        Servicos = Servico(id, descricao, valor)
        ServicoDAO.atualizar(Servicos)
    
    def Servico_excluir(id):
        Servicos = Servico(id, "", "")
        ServicoDAO.excluir(Servicos)    