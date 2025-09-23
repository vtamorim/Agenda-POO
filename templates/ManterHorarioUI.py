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
    def inserir():
        clientes= viewsc.View.Cliente_listar()
        servicos = views.View.Servico_listar()

        data = st.text_input("Informe a data e horário do serviço",datetime.now().strftime("%d/%m/%Y %H:%M"))
        confirmado = st.checkbox("Confirmado")

        cliente= st.selectbox("Informe o cliente", clientes, index = None)

        servico = st.selectbox("Informe o serviço", servicos, index = None)

        if st.button("Inserir"):
            id_cliente = None
            id_servico = None
            if cliente is not None:
                id_cliente = cliente.get_id()
            if servico is not None:
                id_servico = servico.get_id()
            View.horario_inserir(datetime.strptime(data,"%d/%m/%Y %H:%M"), confirmado, id_cliente, id_servico)
            st.success("Horário inserido com sucesso")
    def atualizar():
        horarios = View.horario_listar()
        if len(horarios) == 0: st.write("Nenhum horário cadastrado")
        else:
            clientes = viewsc.View.Cliente_listar()
            servicos= views.View.Servico_listar()
            op = st.selectbox("Atualização de Horários",horarios)
            data = st.text_input("Informe um nova data e um novo serviço",op.get_data().strftime("%d/%m/%Y %H:%M"))
            confirmado = st.checkbox("Nova Confirmação", op.get_confirmado())
            id_cliente = None if op.get_id_cliente() in [0,None] else op.get_id_cliente()
            id_servico = None if op.get_id_servico() in [0,None] else op.get_id_servico()
            cliente = st.selectbox(
                "Informe o novo cliente",
                clientes,
                next(
                    (i for i, c in enumerate(clientes) if c.get_id() == id_cliente),
                    None
                )
            )

            servico = st.selectbox(
                "Informe o novo serviço",
                servicos,
                next(
                    (i for i, s in enumerate(servicos) if s.get_id() == id_servico),
                    None
                )
            )

            if st.button("Atualizar"):
                id_cliente = None
                id_servico = None

                if cliente != None:
                    id_cliente = cliente.get_id()

                if servico != None:
                    id_servico = servico.get_id()

                View.horario_atualizar(
                    op.get_id(),
                    datetime.strptime(data, "%d/%m/%Y %H:%M"),
                    confirmado,
                    id_cliente,
                    id_servico
                )

                st.success("Horário atualizado com sucesso")
    def excluir():
        horarios = View.horario_listar()

        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            op = st.selectbox("Exclusão de Horários", horarios)

            if st.button("Excluir"):
                View.horario_excluir(op.get_id())
                st.success("Horário excluído com sucesso")

                time.sleep(2)
                st.rerun()
