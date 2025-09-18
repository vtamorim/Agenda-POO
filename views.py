from models.servico import Servico, ServicoDAO

class View:

    def Servico_inserir(nome, email, fone):
        Servicos = Servico(0, nome, email, fone)
        ServicoDAO.inserir(Servicos)

    def Servico_listar():
        return ServicoDAO.listar()
  
    def Servico_listar_id(id):
        return ServicoDAO.listar_id(id)

    def Servico_atualizar(id, nome, email, fone):
        Servicos = Servico(id, nome, email, fone)
        ServicoDAO.atualizar(Servicos)
    
    def Servico_excluir(id):
        Servicos = Servico(id, "", "", "")
        ServicoDAO.excluir(Servicos)    