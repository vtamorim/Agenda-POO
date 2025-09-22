import streamlit as st
import pandas as pd
from views import View
import time

class ServicoUI:
    def main():
        st.header("Cadastro de Servicos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ServicoUI.listar()
        with tab2: ServicoUI.inserir()
        with tab3: ServicoUI.atualizar()
        with tab4: ServicoUI.excluir()

    def listar():
        Servicos = View.Servico_listar()
        if len(Servicos) == 0: st.write("Nenhum Servico cadastrado")
        else:
            list_dic = []
            for obj in Servicos: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        descricao = st.text_input("Informe o descricao")
        valor = st.text_input("Informe o valor")
        if st.button("Inserir"):
            View.Servico_inserir(descricao, valor)
            st.success("Servico inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        Servicos = View.Servico_listar()
        if len(Servicos) == 0: st.write("Nenhum Servico cadastrado")
        else:
            op = st.selectbox("Atualização de Servicos", Servicos)
            descricao = st.text_input("Informe o novo descricao", op.get_descricao())
            valor = st.text_input("Informe o novo valor", op.get_valor())
            if st.button("Atualizar"):
                id = op.get_id()
                View.Servico_atualizar(id, descricao, valor)
                st.success("Servico atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        Servicos = View.Servico_listar()
        if len(Servicos) == 0: st.write("Nenhum Servico cadastrado")
        else:
            op = st.selectbox("Exclusão de Servicos", Servicos)
            if st.button("Excluir"):
                id = op.get_id()
                View.Servico_excluir(id)
                st.success("Servico excluído com sucesso")
                time.sleep(2)
                st.rerun()