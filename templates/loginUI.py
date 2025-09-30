import streamlit as st
from views import View


class LoginUI:
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Email")
        senha = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            c = View.Cliente_Autenticar(email, senha)
            if c == None:
                st.error("Email ou senha incorretos.")
            else:
                st.session_state["usuario_id"] = c["id"]
                st.session_state["usuario_nome"] = c["nome"]
                st.rerun()