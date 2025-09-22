from templates.ServicoUI import ServicoUI
import streamlit as st
class IndexUI:

    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Serviços"])
        if op == "Cadastro de Serviços": ServicoUI.main()

    def sidebar():
        IndexUI.menu_admin()

    def main():
        IndexUI.sidebar()

IndexUI.main()

