from templates.ManterServicoUI import ServicoUI
from templates.ManterClienteUI import ClienteUI
import streamlit as st
class IndexUI:

    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes","Cadastro de Serviços"])
        if op == "Cadastro de Serviços": ServicoUI.main()
        if op == "Cadastro de Clientes": ClienteUI.main()
    def sidebar():
        IndexUI.menu_admin()

    def main():
        IndexUI.sidebar()

IndexUI.main()

