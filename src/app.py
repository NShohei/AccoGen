import streamlit as st


import logging


from typing import Union


from models.param import FakerBasedGeneratorParam, LenghBasedGeneratorParam


from models.enums import Locales


from services.account_name_generator import (
    LengthBasedAccountNameGenerator,
    FakerBasedAccountNameGenerator,
)


from session_manager import SessionManager


class App:
    def __init__(
        self,
        account_name_generator: LengthBasedAccountNameGenerator,
        faker_account_name_generator: FakerBasedAccountNameGenerator,
        session_manager: SessionManager,
    ):
        self.account_name_generator = account_name_generator

        self.faker_account_name_generator = faker_account_name_generator
        self.session_manager = session_manager

        self.logger = logging.getLogger(self.__class__.__name__)

    def render(self):
        self.logger.info("Rendering App init")

        method = st.selectbox("生成方法", options=["文字列長指定", "Faker"])

        match method:
            case "文字列長指定":
                self._render_for_account_name_generator()

            case "Faker":
                self._render_for_faker_account_name_generator()

        if len(self.session_manager.account_name) > 0:
            st.subheader(f"アカウント名：{self.session_manager.account_name}")

        if len(self.session_manager.e_mail) > 0:
            st.subheader(f"e-mail：{self.session_manager.e_mail}")

        self.logger.info("Rendering App exit")

    def _generate_account_name(
        self,
        generator,
        param: Union[LenghBasedGeneratorParam, FakerBasedGeneratorParam],
    ):
        self.logger.info(f"generate_account_name init:{str(param)}")

        account_name = generator.generate(param)

        self.session_manager.account_name = account_name

        self.logger.info(f"generate_account_name exit:{account_name}")
        return account_name

    def _render_for_account_name_generator(self):
        alphabet_max_length: int = st.slider(
            label="Alphabet Max Length",
            min_value=0,
            max_value=32,
            step=1,
            value=10,
        )

        number_max_length: int = st.slider(
            label="Number Max Length",
            min_value=0,
            max_value=32,
            step=1,
            value=5,
        )

        symbol_max_length: int = st.slider(
            label="Symbol Max Length", min_value=0, max_value=4, step=1, value=1
        )

        use_leet: bool = st.toggle(label="use_leet", value=False)

        param = LenghBasedGeneratorParam(
            alphabet_max_length=alphabet_max_length,
            number_max_length=number_max_length,
            symbol_max_length=symbol_max_length,
            use_leet=use_leet,
        )

        st.button(
            label="生成",
            on_click=self._generate_account_name,
            args=(
                self.account_name_generator,
                param,
            ),
        )

    def _render_for_faker_account_name_generator(self):
        locale: Locales = st.selectbox(
            "ロケール", options=[Locales.EN_US, Locales.JA_JP]
        )

        use_leet: bool = st.toggle(label="use_leet", value=False)

        param = FakerBasedGeneratorParam(locale=locale, use_leet=use_leet)

        st.button(
            label="生成",
            on_click=self._generate_account_name,
            args=(
                self.faker_account_name_generator,
                param,
            ),
        )
