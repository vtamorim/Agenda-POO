import streamlit as st
from views import View
import time


class AbrirContaUI:
    def main():
        st.header("Abrir Conta")
        nome = st.text_input("Nome")
        email = st.text_input("Email")
        fone = st.text_input("Fone")
        senha = st.text_input("Senha", type="password")
        if st.button("Inserir"):
            View.Cliente_inserir(nome, email, fone, senha)
            st.success("Conta criada com sucesso!")
            time.sleep(2)
            st.rerun()