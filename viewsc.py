from models.cliente import Cliente, ClienteDAO

class View:

    def Cliente_inserir(nome, email, fone):
        Clientes = Cliente(0, nome, email, fone)
        ClienteDAO.inserir(Clientes)

    def Cliente_listar():
        return ClienteDAO.listar()
  
    def Cliente_listar_id(id):
        return ClienteDAO.listar_id(id)

    def Cliente_atualizar(id, nome, email, fone):
        Clientes = Cliente(id, nome, email, fone)
        ClienteDAO.atualizar(Clientes)
    
    def Cliente_excluir(id):
        Clientes = Cliente(id, "", "", "")
        ClienteDAO.excluir(Clientes)    