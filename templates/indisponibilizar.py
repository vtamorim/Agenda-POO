import streamlit as st
from views import View
import time
class IndisponibilizarUI:
    def main():
      st.header("Indisponibilizar Horário")
      op = View.profissional_listar_id(st.session_state["usuario_id"])
      nome = st.text_input("Nome", op.get_nome(), disabled=True)
      motivo = st.text_input("Motivo da indisponibilidade")
      data = st.date_input("Data da indisponibilidade")
      if st.button("Indisponibilizar"):
        # chamar função que salva no JSON (usa views.indisponibilizar_horario)
        View.indisponibilizar_horario(op.get_id(), motivo, data)
        st.success("Aguarde a confirmação da indisponibilidade pelo administrador")
        time.sleep(2)
        st.rerun()