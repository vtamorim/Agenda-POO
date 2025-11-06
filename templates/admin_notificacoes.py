import streamlit as st
from views import View

class admin_notificacoesUI:
    def main():
        st.header("Notificações de Indisponibilidade (Admin)")

        pendentes = View.listar_indisponibilidades("pendente")
        if not pendentes:
            st.info("Nenhuma indisponibilidade pendente.")
        else:
            for item in pendentes:
                profs = View._read_json("profissional.json")
                prof = next((p for p in profs if str(p.get("id") or p.get("profissionalId")) == str(item.get("profissionalId"))), {})
                nome = prof.get("nome") or prof.get("nome_completo") or f"Profissional {item.get('profissionalId')}"
                st.markdown(f"**Nome:** {nome}")
                st.markdown(f"- **Data:** {item.get('data')}")
                st.markdown(f"- **Motivo:** {item.get('motivo')}")
                cols = st.columns([1,1])
                aprovar_key = f"aprovar-{item.get('id')}"
                recusar_key = f"recusar-{item.get('id')}"
                if cols[0].button("Aprovar", key=aprovar_key):
                    View.aprovar_indisponibilidade(item.get("id"))
                    st.success("Indisponibilidade aprovada e profissional ocultado.")
                    st.rerun()
                if cols[1].button("Recusar", key=recusar_key):
                    View.recusar_indisponibilidade(item.get("id"))
                    st.warning("Indisponibilidade recusada.")
                    st.rerun()