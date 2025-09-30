import streamlit as st
import pandas as pd
from views import View
import time

class ProfissionalUI:
    def main():
        st.header("Cadastro de Profissional")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ProfissionalUI.listar()
        with tab2: ProfissionalUI.inserir()
        with tab3: ProfissionalUI.atualizar()
        with tab4: ProfissionalUI.excluir()

    def listar():
        Profissionals = View.Profissional_listar()
        if len(Profissionals) == 0: st.write("Nenhum Profissional cadastrado")
        else:
            list_dic = []
            for obj in Profissionals: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome")
        especialidade = st.text_input("Informe a especialidade")
        conselho = st.text_input("Informe o conselho")
        if st.button("Inserir"):
            View.Profissional_inserir(nome, especialidade, conselho)
            st.success("Profissional inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        Profissionals = View.Profissional_listar()
        if len(Profissionals) == 0: st.write("Nenhum Profissional cadastrado")
        else:
            op = st.selectbox("Atualização de Profissionals", Profissionals)
            nome = st.text_input("Informe o novo nome", op.get_nome())
            especialidade = st.text_input("Informe a nova especialidade", op.get_especialidade())
            conselho = st.text_input("Informe o novo conselho", op.get_conselho())
            if st.button("Atualizar"):
                id = op.get_id()
                View.Profissional_atualizar(id, nome, especialidade, conselho)
                st.success("Profissional atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        Profissionals = View.Profissional_listar()
        if len(Profissionals) == 0: st.write("Nenhum Profissional cadastrado")
        else:
            op = st.selectbox("Exclusão de Profissionals", Profissionals)
            if st.button("Excluir"):
                id = op.get_id()
                View.Profissional_excluir(id)
                st.success("Profissional excluído com sucesso")
                time.sleep(2)
                st.rerun()