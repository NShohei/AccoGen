from app import App
import logging
import streamlit as st


from session_manager import SessionManager


from services.account_name_generator import (
    LengthBasedAccountNameGenerator,
    FakerBasedAccountNameGenerator,
)


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


logger = logging.getLogger(__name__)


if __name__ == "__main__":
    logger.info("App Init")

    if st.session_state.get("App") is None:
        sm = SessionManager()

        gen = LengthBasedAccountNameGenerator()

        faker_acc_gen = FakerBasedAccountNameGenerator()

        app = App(gen, faker_acc_gen, sm)

        st.session_state["App"] = app

    else:
        app = st.session_state.get("App")

    app.render()

    logger.info("App Exit")
