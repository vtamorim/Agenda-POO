import streamlit as st
from views import View


class LoginUI:
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Email")
        senha = st.text_input("Senha", type="password")
        tipo_usuario = st.radio("Tipo de usuário", ("Cliente", "Profissional"))
        if st.button("Entrar"):
            if tipo_usuario == "Cliente":
                # Impede login como admin cliente, a menos que exista um cliente admin de verdade
                if email == "admin" and senha == "1234":
                    from views import View
                    admin_cliente = None
                    for c in View.Cliente_listar():
                        if c.get_email() == "admin" and c.get_senha() == "1234":
                            admin_cliente = c
                            break
                    if not admin_cliente:
                        st.error("O admin não pode entrar como cliente.")
                        return
                c = View.Cliente_Autenticar(email, senha)
            else:
                c = View.Profissional_Autenticar(email, senha)
            if c == None:
                st.error("Email ou senha incorretos.")
            else:
                st.session_state["usuario_id"] = c["id"]
                st.session_state["usuario_nome"] = c["nome"]
                st.session_state["usuario_tipo"] = tipo_usuario
                st.rerun()