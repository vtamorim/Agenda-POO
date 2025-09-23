from templates.ManterServicoUI import ServicoUI
from templates.ManterClienteUI import ClienteUI
from templates.ManterHorarioUI import HorarioUI
import streamlit as st
class IndexUI:

    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Horário","Cadastro de Clientes","Cadastro de Serviços"])
        if op == "Cadastro de Serviços": ServicoUI.main()
        if op == "Cadastro de Clientes": ClienteUI.main()
        if op == "Cadastro de Horário": HorarioUI.main()
    def sidebar():
        IndexUI.menu_admin()

    def main():
        IndexUI.sidebar()

IndexUI.main()

