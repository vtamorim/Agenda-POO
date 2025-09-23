import streamlit as st
import pandas as pd
from viewhor import View
import time
from datetime import datetime

class HorarioUI:
    def main():
        st.header("Cadastro de Horários")
        tab1, tab2, tab3, tab4  = st.tabs(["Listar", "Inserir",

        "Atualizar", "Excluir"])
        with tab1: HorarioUI.listar()
        with tab2: HorarioUI.inserir()
        with tab3: HorarioUI.atualizar()
        with tab4: HorarioUI.excluir()
    def listar():
        horarios = View.horario_listar()
        