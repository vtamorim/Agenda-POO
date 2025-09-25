from models.servico import Servico, ServicoDAO
from models.cliente import Cliente, ClienteDAO
from models.horario import Horario, HorarioDAO

class View:
    # Métodos de Serviço
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

    # Métodos de Cliente
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

    # Métodos de Horário
    def horario_inserir(data, confirmado, id_cliente, id_servico):
        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        HorarioDAO.inserir(c)

    def horario_listar():
        return HorarioDAO.listar()

    def horario_atualizar(id, data, confirmado, id_cliente, id_servico):
        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        HorarioDAO.atualizar(c)

    def horario_excluir(id):
        c = Horario(id, None)
        HorarioDAO.excluir(c)