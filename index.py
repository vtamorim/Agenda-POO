from templates.ManterClienteUI import ManterClienteUI
from templates.ManterServicoUI import ManterServicoUI
from templates.ManterHorarioUI import ManterHorarioUI
from templates.ManterProfissionalUI import ManterProfissionalUI
from templates.alterarsenhaUI import AlterarSenhaUI
import streamlit as st
from templates.abrircontaUI import AbrirContaUI
from templates.loginUI import LoginUI
from templates.login_P import LoginUI_P
from templates.perfilClienteUI import PerfilClienteUI
from templates.perfilProfissionalUI import PerfilProfissionalUI
from templates.agendarservicoUI import AgendarServicoUI
from templates.gerenciarangenda import GerenciarAgendaUI
from templates.meusservicosUI import MeusServicosUI
from templates.confirmarservicoUI import ConfirmarServicoUI
from templates.admin_notificacoes import admin_notificacoesUI
from templates.indisponibilizar import IndisponibilizarUI
from views import View

class IndexUI:
    def main():
        View.cliente_criar_admin()
        IndexUI.sidebar()
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Entrar no Sistema de profissionais", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Entrar no Sistema de profissionais": LoginUI_P.main()
        if op == "Abrir Conta": AbrirContaUI.main()
    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Agendar Serviço", "Meus Serviços"])
        if op == "Meus Dados": PerfilClienteUI.main()
        if op == "Agendar Serviço": AgendarServicoUI.main()
        if op == "Meus Serviços": MeusServicosUI.main()
    def menu_profissional():
        # Adicionado "Início" e "Indisponibilizar Horário" para profissionais
        op = st.sidebar.selectbox("Menu", ["Início", "Meus Dados", "gerenciar agenda","confirmar serviço","Indisponibilizar Horário"])
        if op == "Início":
            st.header("Área do Profissional")
            st.write("Bem-vindo(a). Use o menu lateral para acessar suas opções.")
        if op == "Meus Dados": PerfilProfissionalUI.main()
        if op == "gerenciar agenda": GerenciarAgendaUI.main()
        if op == "confirmar serviço": ConfirmarServicoUI.main()
        if op == "Indisponibilizar Horário":
            # importa o template ao ser selecionado para renderizar a UI
            IndisponibilizarUI.main()
    def menu_admin(): 
        # Adicionado item de Notificações de Indisponibilidade
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", 
                                            "Cadastro de Serviços", 
                                            "Cadastro de Horários", 
                                            "Cadastro de Profissionais",
                                            "Notificações de Indisponibilidade",
                                            "Alterar Senha"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        if op == "Cadastro de Profissionais": ManterProfissionalUI.main()
        if op == "Notificações de Indisponibilidade":
            # importa o template admin quando selecionado
            admin_notificacoesUI.main()
        if op == "Alterar Senha": AlterarSenhaUI.main()
    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()
    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante() 
        else:
            admin = st.session_state["usuario_nome"] == "admin"
            profissional = not admin and View.profissional_listar_id(st.session_state["usuario_id"]) is not None
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
            if admin: IndexUI.menu_admin()
            elif profissional: IndexUI.menu_profissional()
            else: IndexUI.menu_cliente()
            IndexUI.sair_do_sistema()


IndexUI.main()