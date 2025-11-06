from models.servico import Servico, ServicoDAO
from models.cliente import Cliente, ClienteDAO
from models.horario import Horario, HorarioDAO
from models.profissional import Profissional, ProfissionalDAO
import json
import uuid
from typing import List, Dict, Optional
from datetime import datetime
INDISP_PATH = "indisponiveis.json"
PROF_PATH = "profissional.json"
class View:

    def _read_json(path: str) -> List[Dict]:
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def _write_json(path: str, data: List[Dict]):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def _get_indisponiveis_ativas():
        """
        Retorna mapping prof_id -> {motivo, data} para indisponibilidades aprovadas
        cuja data ainda não passou.
        """
        indisps = View._read_json(INDISP_PATH)
        hoje = datetime.now().date()
        m = {}
        for i in indisps:
            if i.get("status") == "aprovado":
                try:
                    data_ind = datetime.fromisoformat(i.get("data")).date()
                except Exception:
                    # se não for ISO ou inválido ignora esse registro
                    continue
                if data_ind >= hoje:
                    pid = str(i.get("profissionalId"))
                    # guarda primeira indisponibilidade ativa encontrada
                    if pid not in m:
                        m[pid] = {"motivo": i.get("motivo"), "data": i.get("data")}
        return m

    def indisponibilizar_horario(profissional_id: str, motivo: str, data):
        """
        Registra uma indisponibilidade com status 'pendente'.
        'data' pode ser date ou string; será salvo em ISO date (YYYY-MM-DD).
        """
        indisps = View._read_json(INDISP_PATH)
        item = {
            "id": str(uuid.uuid4()),
            "profissionalId": str(profissional_id),
            "data": getattr(data, "isoformat", lambda: str(data))(),
            "motivo": motivo,
            "status": "pendente",  # pendente | aprovado | recusado
            "criadoEm": datetime.utcnow().isoformat() + "Z"
        }
        indisps.append(item)
        View._write_json(INDISP_PATH, indisps)
        return item

    def listar_indisponibilidades(status: Optional[str] = None) -> List[Dict]:
        indisps = View._read_json(INDISP_PATH)
        if status:
            return [i for i in indisps if i.get("status") == status]
        return indisps

    def aprovar_indisponibilidade(indisp_id: str) -> bool:
        indisps = View._read_json(INDISP_PATH)
        updated = False
        prof_id = None
        for i in indisps:
            if i.get("id") == indisp_id:
                i["status"] = "aprovado"
                updated = True
                prof_id = i.get("profissionalId")
                i["aprovadoEm"] = datetime.utcnow().isoformat() + "Z"
                break
        if updated:
            View._write_json(INDISP_PATH, indisps)
            if prof_id:
                View._set_profissional_oculto(prof_id, True)
        return updated

    def recusar_indisponibilidade(indisp_id: str) -> bool:
        indisps = View._read_json(INDISP_PATH)
        for i in indisps:
            if i.get("id") == indisp_id:
                i["status"] = "recusado"
                i["recusadoEm"] = datetime.utcnow().isoformat() + "Z"
                View._write_json(INDISP_PATH, indisps)
                return True
        return False

    def _set_profissional_oculto(profissional_id: str, oculto: bool):
        profs = View._read_json(PROF_PATH)
        changed = False
        for p in profs:
            # assumir que o arquivo profissional.json tem campo 'id' ou 'profissionalId'
            if str(p.get("id") or p.get("profissionalId")) == str(profissional_id):
                p["oculto"] = bool(oculto)
                changed = True
                break
        if changed:
            View._write_json(PROF_PATH, profs)
        return changed


    def cliente_inserir(nome, email, fone, senha):
        cliente = Cliente(0, nome, email, fone, senha)
        ClienteDAO.inserir(cliente)

    def cliente_listar():
        return ClienteDAO.listar()
  
    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)

    def cliente_atualizar(id, nome, email, fone, senha):
        cliente = Cliente(id, nome, email, fone, senha)
        ClienteDAO.atualizar(cliente)
    
    def cliente_excluir(id):
        cliente = Cliente(id, "", "", "", "")
        ClienteDAO.excluir(cliente)    

    def cliente_criar_admin():
        for c in View.cliente_listar():
            if c.get_email() == "admin":
                return
        View.cliente_inserir("admin", "admin", "fone", "1234")
    
    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()}
        return None
    
    def profissional_inserir(nome, especialidade, conselho, email, senha,disponivel):
        profissional = Profissional(0, nome, especialidade, conselho, email, senha,disponivel)
        ProfissionalDAO.inserir(profissional)

    def profissional_listar():
        return ProfissionalDAO.listar()
  
    def profissional_listar_id(id):
        return ProfissionalDAO.listar_id(id)

    def profissional_atualizar(id, nome, especialidade, conselho, email, senha,disponivel):
        profissional = Profissional(id, nome, especialidade, conselho, email, senha,disponivel)
        ProfissionalDAO.atualizar(profissional)
    
    def profissional_excluir(id):
        profissional = Profissional(id, "", "", "", "", "","")
        ProfissionalDAO.excluir(profissional) 
   
    def profissional_autenticar(email, senha):
        for p in View.profissional_listar():
            if p.get_email() == email and p.get_senha() == senha:
                return {"id": p.get_id(), "nome": p.get_nome()}
        return None

    def servico_listar():
        return ServicoDAO.listar()
    
    def servico_listar_id(id):
        return ServicoDAO.listar_id(id)

    def servico_inserir(descricao, valor):
        servico = Servico(0, descricao, valor)
        ServicoDAO.inserir(servico)

    def servico_atualizar(id, descricao, valor):
        servico = Servico(id, descricao, valor)
        ServicoDAO.atualizar(servico)

    def servico_excluir(id):
        servico = Servico(id, "", 0.0)
        ServicoDAO.excluir(servico)

    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)
        HorarioDAO.inserir(c)

    def horario_listar():
        return HorarioDAO.listar()

    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)
        HorarioDAO.atualizar(c)

    def horario_excluir(id):
        c = Horario(id, None)
        HorarioDAO.excluir(c)
    def horario_agendar_horario(id_profissional):
        r = []
        agora = datetime.now()
        for h in View.horario_listar():
            if h.get_data() >= agora and h.get_confirmado() == False and h.get_id_cliente() == None and h.get_id_profissional() == id_profissional:
                r.append(h)
        r.sort(key = lambda h : h.get_data()) 
        return r

    def listar_profissionais_publicos() -> List[Dict]:
        """
        Retorna apenas profissionais disponíveis e não ocultos.
        Filtra automaticamente profissionais indisponíveis.
        """
        profs = View._read_json(PROF_PATH)
        indisponiveis = View._get_indisponiveis_ativas()
        
        # Filtra profissionais que não estão ocultos nem indisponíveis
        resultado = []
        for p in profs:
            if not p.get("oculto", False):
                prof_id = str(p.get("id") or p.get("profissionalId"))
                p_copy = p.copy()
                
                # Adiciona apenas se estiver disponível
                if prof_id not in indisponiveis:
                    p_copy["disponivel"] = True
                    resultado.append(p_copy)
                    
        return resultado
    def listar_profissionais(incluir_ocultos: bool = False) -> List[Dict]:
        """
        Retorna todos os profissionais (ou filtra ocultos) anotados com disponibilidade.
        """
        profs = View._read_json(PROF_PATH)
        indisponiveis = View._get_indisponiveis_ativas()
        resultado = []
        for p in profs:
            if incluir_ocultos or not p.get("oculto", False):
                prof_id = str(p.get("id") or p.get("profissionalId"))
                p_copy = p.copy()
                if prof_id in indisponiveis:
                    p_copy["disponivel"] = False
                    p_copy["motivo_indisponibilidade"] = indisponiveis[prof_id]["motivo"]
                    p_copy["data_indisponibilidade"] = indisponiveis[prof_id]["data"]
                else:
                    p_copy["disponivel"] = True
                resultado.append(p_copy)
        return resultado
    def profissional_por_id(prof_id: str, incluir_oculto: bool = True) -> Optional[Dict]:
        """
        Retorna o profissional por id anotado com disponibilidade.
        """
        profs = View._read_json(PROF_PATH)
        indisponiveis = View._get_indisponiveis_ativas()
        for p in profs:
            if str(p.get("id") or p.get("profissionalId")) == str(prof_id):
                if not incluir_oculto and p.get("oculto", False):
                    return None
                p_copy = p.copy()
                pid = str(p_copy.get("id") or p_copy.get("profissionalId"))
                if pid in indisponiveis:
                    p_copy["disponivel"] = False
                    p_copy["motivo_indisponibilidade"] = indisponiveis[pid]["motivo"]
                    p_copy["data_indisponibilidade"] = indisponiveis[pid]["data"]
                else:
                    p_copy["disponivel"] = True
                return p_copy
        return None

    # se já existir a classe View, expõe essas funções como métodos estáticos para compatibilidade
    try:
        View  # verifica se View existe no módulo
    except NameError:
        View = None

    if View:
        # nomes compatíveis com usos atuais do projeto
        setattr(View, "listar_profissionais_publicos", staticmethod(lambda: listar_profissionais_publicos()))
        setattr(View, "listar_profissionais", staticmethod(lambda incluir=False: listar_profissionais(incluir)))
        setattr(View, "profissional_por_id", staticmethod(lambda pid, incluir=True: profissional_por_id(pid, incluir)))
        # compatibilidade com possível nome existente profissional_listar_id
        setattr(View, "profissional_listar_id", staticmethod(lambda pid: profissional_por_id(pid, incluir_oculto=True)))
