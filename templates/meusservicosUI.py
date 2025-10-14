import streamlit as st
from views import View
import pandas as pd

class MeusServicosUI:
    def main():
        st.header("Meus Serviços Agendados")
        cliente_id = st.session_state.get("usuario_id")
        if not cliente_id:
            st.error("Usuário não autenticado!")
            return
        horarios = [h for h in View.horario_listar() if h.get_id_cliente() == cliente_id]
        if not horarios:
            st.info("Nenhum serviço agendado.")
            return
        dados = []
        for h in horarios:
            profissional = View.Profissional_listar_id(h.get_id_profissional()) if h.get_id_profissional() else None
            servico = View.Servico_listar_id(h.get_id_servico()) if h.get_id_servico() else None
            dados.append({
                "Data/Hora": h.get_data().strftime("%d/%m/%Y %H:%M"),
                "Profissional": profissional.get_nome() if profissional else "-",
                "Serviço": servico.get_descricao() if servico else "-",
                "Confirmado": "Sim" if h.get_confirmado() else "Não"
            })
        df = pd.DataFrame(dados)
        st.dataframe(df)
