from models.servico import Servico, ServicoDAO
from models.cliente import Cliente, ClienteDAO
from models.horario import Horario, HorarioDAO
from models.profissional import Profissional,ProfissionalDAO
from datetime import datetime
class View:
    def Profissional_CriarAdmin():
        for p in View.Profissional_listar():
            if p.get_email() == "admin":
                return
        View.Profissional_inserir("admin", "Administrador", "Admin", "0000", "admin", "1234")
    # Métodos de Serviço
    def Servico_inserir(descricao, valor):
        Servicos = Servico(0, descricao, valor)
        ServicoDAO.inserir(Servicos)

    def Servico_listar():
        r = ServicoDAO.listar()
        r.sort(key = lambda obj: obj.get_descricao())
        return r

    def Servico_listar_id(id):
        return ServicoDAO.listar_id(id)

    def Servico_atualizar(id, descricao, valor):
        Servicos = Servico(id, descricao, valor)
        ServicoDAO.atualizar(Servicos)

    def Servico_excluir(id):
        Servicos = Servico(id, "", "")
        ServicoDAO.excluir(Servicos)

    # Métodos de Cliente
    def Cliente_inserir(nome, email, fone,senha):
        Clientes = Cliente(0, nome, email, fone , senha)
        ClienteDAO.inserir(Clientes)

    def Cliente_listar():
        r = ClienteDAO.listar()
        r.sort(key = lambda obj: obj.get_nome())
        return r

    def Cliente_listar_id(id):
        return ClienteDAO.listar_id(id)

    def Cliente_atualizar(id, nome, email, fone,senha):
        Clientes = Cliente(id, nome, email, fone,senha)
        ClienteDAO.atualizar(Clientes)

    def Cliente_excluir(id):
        Clientes = Cliente(id, "", "", "","")
        ClienteDAO.excluir(Clientes)

    def Cliente_CriarAdmin():
        for c in View.Cliente_listar():
            if c.get_email() == "admin": return
        View.Cliente_inserir("admin", "admin", "fone", "1234")

    @staticmethod
    def Cliente_Autenticar(email, senha):
        for c in View.Cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()}
        return None
    # Métodos de Horário
    def horario_inserir(data, confirmado, id_cliente, id_servico,id_profissional):
        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)
        HorarioDAO.inserir(c)

    def horario_listar():
        r = HorarioDAO.listar()
        r.sort(key = lambda obj: obj.get_data())
        return r

    def horario_atualizar(id, data, confirmado, id_cliente, id_servico,id_profissional):
        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)
        HorarioDAO.atualizar(c)

    def horario_excluir(id):
        c = Horario(id, None)
        HorarioDAO.excluir(c)
    

    def Profissional_inserir(nome, especialidade, conselho, email, senha):
        Profissionals = Profissional(0, nome, especialidade, conselho, email, senha)
        ProfissionalDAO.inserir(Profissionals)

    def Profissional_listar():
        r = ProfissionalDAO.listar()
        r.sort(key = lambda obj: obj.get_nome())
        return r

    def Profissional_listar_id(id):
        return ProfissionalDAO.listar_id(id)

    def Profissional_atualizar(id, nome, especialidade, conselho, email, senha):
        Profissionals = Profissional(id, nome, especialidade, conselho, email, senha)
        ProfissionalDAO.atualizar(Profissionals)
    @staticmethod
    def Profissional_Autenticar(email, senha):
        for p in View.Profissional_listar():
            if p.get_email() == email and p.get_senha() == senha:
                return {"id": p.get_id(), "nome": p.get_nome()}
        return None

    def Profissional_excluir(id):
        Profissionals = Profissional(id, "", "", "")
        ProfissionalDAO.excluir(Profissionals)
    

    def horario_agendar_horario(id_profissional):
        r = []
        agora = datetime.now()

        for h in View.horario_listar():
            if (
                h.get_data() >= agora and
                h.get_confirmado() == False and
                h.get_id_cliente() is None and
                h.get_id_profissional() == id_profissional
            ):
                r.append(h)

        r.sort(key=lambda h: h.get_data())
        return r