import streamlit as st
from views import View
from datetime import datetime
from templates._profissional_helper import ProfissionalHelper

class AgendarServicoUI:
    def main():
        st.header("Agendar Serviço")
        
        # Lista todos os profissionais
        profissionais = View.listar_profissionais_publicos()
        
        def on_select(prof):
            st.session_state['profissional_selecionado'] = prof.get('id')
            st.success("Profissional selecionado para agendamento!")

        for prof in profissionais:
            ProfissionalHelper.render_prof_card(st, prof, select_callback=on_select)

        # Adiciona alguns estilos para melhorar a aparência
        st.markdown("""
        <style>
        .stAlert {
            padding: 10px;
            border-radius: 4px;
            margin-bottom: 10px;
        }
        </style>
        """, unsafe_allow_html=True)
        if 'profissional_selecionado' in st.session_state:
            prof_id = st.session_state['profissional_selecionado']
            st.subheader("Selecione o serviço e o horário")

            servicos = View.servico_listar()
            servico = st.selectbox("Serviço", servicos, format_func=lambda s: s.get_descricao())

            horarios_disponiveis = View.horario_agendar_horario(prof_id)
            horario = st.selectbox(
                "Horário disponível",
                horarios_disponiveis,
                format_func=lambda h: h.get_data().strftime("%d/%m/%Y %H:%M")
            )

            if st.button("Agendar serviço"):
                View.horario_atualizar(
                    horario.get_id(),
                    horario.get_data(),
                    False,  # ainda não confirmado
                    st.session_state["usuario_id"],  # cliente logado
                    servico.get_id(),
                    prof_id
                )
                st.success("Serviço agendado com sucesso!")
                st.session_state.pop("profissional_selecionado")
                st.rerun()