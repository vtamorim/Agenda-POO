import streamlit as st
import time
from views import View

class AlterarSenhaUI:
    def main():
        st.header("Alterar Senha (Admin)")

        admin = View.cliente_listar_id(st.session_state["usuario_id"])
        if admin is None or admin.get_email() != "admin":
            st.warning("Apenas o administrador pode alterar a senha aqui.")
            return

        st.text_input("Nome", admin.get_nome(), disabled=True)
        st.text_input("E-mail (não pode ser alterado)", admin.get_email(), disabled=True)

        nova_senha = st.text_input("Informe a nova senha", type="password")

        if st.button("Alterar Senha"):
            if nova_senha.strip() == "":
                st.error("Por favor, informe uma nova senha válida.")
            else:
                View.cliente_atualizar(
                    admin.get_id(),
                    admin.get_nome(),
                    admin.get_email(),
                    admin.get_fone(),
                    nova_senha
                )
                st.success("Senha alterada com sucesso!")
                time.sleep(2)
                st.rerun()