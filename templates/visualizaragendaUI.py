import streamlit as st
from views import View
import pandas as pd

class VisualizarAgendaUI:
    def main():
        st.header("Visualizar Minha Agenda")
        profissional_id = st.session_state.get("usuario_id")
        if not profissional_id:
            st.error("Usuário não autenticado!")
            return
        horarios = [h for h in View.horario_listar() if h.get_id_profissional() == profissional_id]
        if not horarios:
            st.info("Nenhum horário cadastrado.")
            return
        dados = []
        for h in horarios:
            cliente = View.Cliente_listar_id(h.get_id_cliente()) if h.get_id_cliente() else None
            servico = View.Servico_listar_id(h.get_id_servico()) if h.get_id_servico() else None
            dados.append({
                "Data/Hora": h.get_data().strftime("%d/%m/%Y %H:%M"),
                "Cliente": cliente.get_nome() if cliente else "Disponível",
                "Serviço": servico.get_descricao() if servico else "-",
                "Confirmado": "Sim" if h.get_confirmado() else "Não"
            })
        df = pd.DataFrame(dados)
        st.dataframe(df)
