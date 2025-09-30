import streamlit as st
from views import View
import time

class perfilClienteUI:
    def main():
        st.header("Perfil do Cliente")
        op = View.Cliente_listar_id(st.session_state["usuario_id"])
        nome = st.text_input("Seu nome", op.get_nome())
        email = st.text_input("Seu email", op.get_email())
        fone = st.text_input("Seu fone",op.get_fone())
        senha = st.text_input("Sua senha",op.get_senha(), type="password")
        if st.button("Atualizar"):
            id = op.get_id()
            View.Cliente_atualizar(id,nome,email,fone,senha)
            st.success("Deu certo")