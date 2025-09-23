import streamlit as st
import pandas as pd
from viewhor import View
import time
import viewsc
import views
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
        if len(horarios) == 0: st.write("Nenhum Cadastro Registrado")
        else:
            dic = []
            for obj in horarios:
                cliente = viewsc.View.Cliente_listar_id(obj.get_id_cliente())
                servico = views.View.Servico_listar_id(obj.get_id_servico())
                if cliente != None: cliente = cliente.get_nome()
                if servico != None: servico = servico.get_nome()
                dic.append({"id": obj.get_id(), "data": obj.get_data(),"confirmado":obj.get_confirmado(),"cliente" : cliente,"servico" : servico})
            df = pd.DataFrame(dic)
            st.dataframe(df)