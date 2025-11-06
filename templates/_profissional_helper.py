class ProfissionalHelper:
    def render_prof_card(st, prof, select_callback=None):
        """
        Renderiza cartão de profissional:
        - mostra dados básicos
        - se prof['disponivel'] == False: exibe legenda de indisponibilidade, motivo/data e botão desabilitado
        - se disponível: mostra botão ativo que chama select_callback(prof)
        """
        from datetime import datetime
        with st.container():
            col1, col2 = st.columns([3,1])
            with col1:
                st.subheader(prof.get('nome', '—'))
                st.write(f"Especialidade: {prof.get('especialidade','')}")
                st.write(f"Conselho: {prof.get('conselho','')}")
            with col2:
                if not prof.get('disponivel', True):
                    st.error("⚠️ INDISPONÍVEL")
                    data = prof.get('data_indisponibilidade')
                    if data:
                        try:
                            data_fmt = datetime.fromisoformat(data).strftime("%d/%m/%Y")
                        except Exception:
                            data_fmt = str(data)
                        st.info(f"Até: {data_fmt}")
                    motivo = prof.get('motivo_indisponibilidade')
                    if motivo:
                        with st.expander("Ver motivo"):
                            st.write(motivo)
                    # botão visual mas desabilitado (não permite seleção)
                    st.button("Selecionar", key=f"btn_{prof.get('id')}_disabled", disabled=True)
                else:
                    st.success("✅ DISPONÍVEL")
                    if st.button("Selecionar", key=f"btn_{prof.get('id')}"):
                        if callable(select_callback):
                            select_callback(prof)
            st.divider()