
from templates.ManterServicoUI import ServicoUI
from templates.ManterClienteUI import ClienteUI
from templates.ManterHorarioUI import HorarioUI
from templates.ManterProfissionalUI import ProfissionalUI
from templates.loginUI import LoginUI
from templates.abrircontaUI import AbrirContaUI
from templates.perfilClienteUI import perfilClienteUI
from views import View



import streamlit as st
class IndexUI:

    def menu_admin():
        op = st.sidebar.selectbox("Menu", [
            "Cadastro de Horário",
            "Cadastro de Clientes",
            "Cadastro de Serviços",
            "Cadastro de Profissional",
            "Meus Dados"
        ])
        if op == "Cadastro de Serviços": ServicoUI.main()
        if op == "Cadastro de Clientes": ClienteUI.main()
        if op == "Cadastro de Horário": HorarioUI.main()
        if op == "Cadastro de Profissional": ProfissionalUI.main()
        if op == "Meus Dados":
            from templates.perfilProfissionalUI import perfilProfissionalUI
            perfilProfissionalUI.main()

    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema",
        "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados"])
        if op == "Meus Dados":
            if st.session_state.get("usuario_tipo") == "Profissional":
                from templates.perfilProfissionalUI import perfilProfissionalUI
                perfilProfissionalUI.main()
            else:
                perfilClienteUI.main()

    def sair_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()
    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            is_admin_prof = (
                st.session_state.get("usuario_tipo") == "Profissional"
                and st.session_state.get("usuario_nome") == "admin"
            )
            st.sidebar.write("Bem vindo(a), " + st.session_state["usuario_nome"] )
            if is_admin_prof:
                IndexUI.menu_admin()
            else:
                IndexUI.menu_cliente()
            IndexUI.sair_sistema()
    def main():
        View.Cliente_CriarAdmin()
        IndexUI.sidebar()

IndexUI.main()

