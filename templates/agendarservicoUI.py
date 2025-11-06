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