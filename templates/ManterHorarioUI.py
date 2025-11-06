import streamlit as st
import pandas as pd
from views import View
import time
from datetime import datetime

class ManterHorarioUI:
    def main():
        st.header("Cadastro de Horários")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterHorarioUI.listar()
        with tab2: ManterHorarioUI.inserir()
        with tab3: ManterHorarioUI.atualizar()
        with tab4: ManterHorarioUI.excluir()

    def listar():
        horarios = View.horario_listar()
        if len(horarios) == 0: 
            st.write("Nenhum horário cadastrado")
        else: 
            dic = []
            for obj in horarios:
                cliente = View.cliente_listar_id(obj.get_id_cliente())
                servico = View.servico_listar_id(obj.get_id_servico())
                profissional = View.profissional_listar_id(obj.get_id_profissional())
                if cliente != None: cliente = cliente.get_nome()
                if profissional != None: profissional = profissional.get_nome()
                if servico != None: servico = servico.get_descricao()
                dic.append({
                    "id" : obj.get_id(), 
                    "data" : obj.get_data(), 
                    "confirmado" : obj.get_confirmado(), 
                    "cliente" : cliente, 
                    "serviço" : servico,
                    "profissional" : profissional
                })
            df = pd.DataFrame(dic)
            st.dataframe(df, hide_index=True)
        
    def inserir():
        clientes = View.cliente_listar()
        servicos = View.servico_listar()

        # Carrega e normaliza profissionais
        profissionais_raw = View.listar_profissionais()  # lista de dicts
        profissionais = []

        for p in profissionais_raw:
            p_copy = p.copy()
            val = p_copy.get("disponivel")

            # Normaliza "S"/"N" para booleano
            if isinstance(val, str):
                p_copy["disponivel"] = val.upper() == "S"
            else:
                p_copy["disponivel"] = bool(val)

            profissionais.append(p_copy)

        # Campo de data e hora
        data = st.text_input(
            "Informe a data e horário do serviço",
            datetime.now().strftime("%d/%m/%Y %H:%M")
        )
        confirmado = st.checkbox("Confirmado")

        # Seleção de cliente
        cliente = st.selectbox(
            "Informe o cliente",
            clientes,
            index=None,
            key="mh_inserir_cliente"
        )

        # Seleção de profissional (mostra todos, indica indisponíveis)
        if not profissionais:
            st.info("Nenhum profissional cadastrado.")
            profissional = None
        else:
            profissional = st.selectbox(
                "Informe o profissional",
                profissionais,
                index=None,
                format_func=lambda p: f"{p.get('nome')} {'❌ Indisponível' if not p.get('disponivel') else '✅ Disponível'}",
                key="mh_inserir_profissional"
            )

        # Seleção de serviço
        servico = st.selectbox(
            "Informe o serviço",
            servicos,
            index=None,
            key="mh_inserir_servico"
        )

        # Botão de inserir
        if st.button("Inserir", key="mh_inserir_btn"):
            # Verifica disponibilidade antes de inserir
            if profissional is not None and not profissional.get("disponivel", True):
                st.error("Este profissional está indisponível nesta data.")
                return

            id_cliente = cliente.get_id() if hasattr(cliente, "get_id") else cliente.get("id") if cliente else None
            id_profissional = profissional.get("id") if profissional else None
            id_servico = servico.get_id() if hasattr(servico, "get_id") else servico.get("id") if servico else None

            View.horario_inserir(
                datetime.strptime(data, "%d/%m/%Y %H:%M"),
                confirmado,
                id_cliente,
                id_servico,
                id_profissional
            )

            st.success("Horário inserido com sucesso.")
            time.sleep(2)
            st.rerun()

    def atualizar():
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
            return

        clientes = View.cliente_listar()
        # carrega e normaliza profissionais (mesma lógica)
        profissionais_raw = View.listar_profissionais(incluir_ocultos=True)
        profissionais = []
        for p in profissionais_raw:
            p_copy = p.copy()
            val = p_copy.get("disponivel")
            if isinstance(val, str):
                p_copy["disponivel"] = True if val.upper() == "S" else False
            else:
                p_copy["disponivel"] = bool(val)
            profissionais.append(p_copy)

        servicos = View.servico_listar()
        op = st.selectbox("Atualização de Horários", horarios, key="mh_atualizar_select_horario")

        data = st.text_input("Informe a nova data e horário do serviço", op.get_data().strftime("%d/%m/%Y %H:%M"))
        confirmado = st.checkbox("Nova confirmação", op.get_confirmado())

        id_cliente = None if op.get_id_cliente() in [0, None] else op.get_id_cliente()
        id_profissional = None if op.get_id_profissional() in [0, None] else op.get_id_profissional()
        id_servico = None if op.get_id_servico() in [0, None] else op.get_id_servico()

        # determina indices iniciais (compatível com dict ou objeto)
        cliente_index = next((i for i, c in enumerate(clientes) if (hasattr(c, "get_id") and c.get_id() == id_cliente) or (not hasattr(c, "get_id") and c.get("id") == id_cliente)), None)

        # profissionais mostrados: todos (incluir ocultos) ou só disponíveis? aqui usa todos para permitir alteração
        prof_index = next(
            (i for i, p in enumerate(profissionais) if (p.get("id") == id_profissional)),
            None
        )

        servico_index = next((i for i, s in enumerate(servicos) if (hasattr(s, "get_id") and s.get_id() == id_servico) or (not hasattr(s, "get_id") and s.get("id") == id_servico)), None)

        cliente = st.selectbox("Informe o novo cliente", clientes, index = cliente_index if cliente_index is not None else 0, key="mh_atualizar_cliente")
        profissional = st.selectbox(
            "Informe o novo profissional",
            profissionais,
            index = prof_index if prof_index is not None else 0,
            format_func=lambda p: (f'{p.get("nome")} (Indisponível)' if not p.get("disponivel", True) else p.get("nome")),
            key="mh_atualizar_profissional"
        )
        servico = st.selectbox("Informe o novo serviço", servicos, index = servico_index if servico_index is not None else 0, key="mh_atualizar_servico")

        if st.button("Atualizar", key="mh_atualizar_btn"):
            id_cliente = cliente.get_id() if hasattr(cliente, "get_id") else cliente.get("id")
            id_profissional = profissional.get("id")
            id_servico = servico.get_id() if hasattr(servico, "get_id") else servico.get("id")
            View.horario_atualizar(op.get_id(), datetime.strptime(data, "%d/%m/%Y %H:%M"), confirmado, id_cliente, id_servico, id_profissional)
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