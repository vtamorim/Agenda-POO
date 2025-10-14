import streamlit as st
from views import View

class ConfirmarServicoUI:
    def main():
        st.header("Confirmar Serviços Agendados")
        profissional_id = st.session_state.get("usuario_id")
        if not profissional_id:
            st.error("Usuário não autenticado!")
            return
        horarios = [h for h in View.horario_listar() if h.get_id_profissional() == profissional_id and h.get_id_cliente() and not h.get_confirmado()]
        if not horarios:
            st.info("Nenhum serviço pendente de confirmação.")
            return
        op = st.selectbox("Selecione o serviço para confirmar", horarios, format_func=lambda h: f"{h.get_data().strftime('%d/%m/%Y %H:%M')} - Cliente: {View.Cliente_listar_id(h.get_id_cliente()).get_nome()} - Serviço: {View.Servico_listar_id(h.get_id_servico()).get_descricao()}")
        if st.button("Confirmar Serviço"):
            View.horario_atualizar(op.get_id(), op.get_data(), True, op.get_id_cliente(), op.get_id_servico(), op.get_id_profissional())
            st.success("Serviço confirmado com sucesso!")
            st.rerun()
