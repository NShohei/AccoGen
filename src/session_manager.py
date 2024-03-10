import streamlit as st


class SessionManager:
    def __init__(self):
        st.session_state["account_name"] = ""
        st.session_state["e_mail"] = ""

    @property
    def account_name(self) -> str:
        return st.session_state["account_name"]

    @account_name.setter
    def account_name(self, value):
        st.session_state["account_name"] = value

    @property
    def e_mail(self) -> str:
        return st.session_state["e_mail"]

    @e_mail.setter
    def e_mail(self, value):
        st.session_state["e_mail"] = value
