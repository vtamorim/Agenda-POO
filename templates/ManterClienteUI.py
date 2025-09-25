import streamlit as st
import pandas as pd
from views import View
import time

class ClienteUI:
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ClienteUI.listar()
        with tab2: ClienteUI.inserir()
        with tab3: ClienteUI.atualizar()
        with tab4: ClienteUI.excluir()

    def listar():
        Clientes = View.Cliente_listar()
        if len(Clientes) == 0: st.write("Nenhum Cliente cadastrado")
        else:
            list_dic = []
            for obj in Clientes: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        if st.button("Inserir"):
            View.Cliente_inserir(nome, email, fone)
            st.success("Cliente inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        Clientes = View.Cliente_listar()
        if len(Clientes) == 0: st.write("Nenhum Cliente cadastrado")
        else:
            op = st.selectbox("Atualização de Clientes", Clientes)
            nome = st.text_input("Informe o novo nome", op.get_nome())
            email = st.text_input("Informe o novo e-mail", op.get_email())
            fone = st.text_input("Informe o novo fone", op.get_fone())
            if st.button("Atualizar"):
                id = op.get_id()
                View.Cliente_atualizar(id, nome, email, fone)
                st.success("Cliente atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        Clientes = View.Cliente_listar()
        if len(Clientes) == 0: st.write("Nenhum Cliente cadastrado")
        else:
            op = st.selectbox("Exclusão de Clientes", Clientes)
            if st.button("Excluir"):
                id = op.get_id()
                View.Cliente_excluir(id)
                st.success("Cliente excluído com sucesso")
                time.sleep(2)
                st.rerun()