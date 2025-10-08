import streamlit as st
from views import View
import time

class perfilProfissionalUI:
    def main():
        st.header("Perfil do Profissional")
        op = View.Profissional_listar_id(st.session_state["usuario_id"])
        nome = st.text_input("Seu nome", op.get_nome())
        especialidade = st.text_input("Sua especialidade", op.get_especialidade())
        conselho = st.text_input("Seu conselho", op.get_conselho())
        email = st.text_input("Seu e-mail", op.get_email())
        senha = st.text_input("Sua senha", op.get_senha(), type="password")
        if st.button("Atualizar"):
            id = op.get_id()
            View.Profissional_atualizar(id, nome, especialidade, conselho, email, senha)
            st.success("Dados atualizados com sucesso!")
            time.sleep(2)
            st.rerun()
