import streamlit as st
from views import View

class AlterarSenhaUI:
    def main():
        st.header("Alterar Senha do Admin")
        usuario_id = st.session_state.get("usuario_id")
        usuario_tipo = st.session_state.get("usuario_tipo")
        if not usuario_id or usuario_tipo != "Cliente":
            st.error("Apenas o usuário Admin pode alterar a senha por aqui.")
            return
        admin = View.Cliente_listar_id(usuario_id)
        if not admin or admin.get_email() != "admin":
            st.error("Apenas o usuário Admin pode alterar a senha por aqui.")
            return
        nova_senha = st.text_input("Nova senha", type="password")
        confirmar = st.text_input("Confirme a nova senha", type="password")
        if st.button("Alterar Senha"):
            if not nova_senha or nova_senha != confirmar:
                st.error("As senhas não coincidem ou estão em branco.")
            else:
                View.Cliente_atualizar(admin.get_id(), admin.get_nome(), admin.get_email(), admin.get_fone(), nova_senha)
                st.success("Senha alterada com sucesso!")
