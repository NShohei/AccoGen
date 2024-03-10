import random
import string


from typing import List
import logging


from models.param import LenghBasedGeneratorParam, FakerBasedGeneratorParam


from faker import Faker


logger = logging.getLogger(__name__)


class LengthBasedAccountNameGenerator:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def generate(self, param: LenghBasedGeneratorParam) -> str:
        self.logger.info(f"generate init:{str(param)}")

        generated_name: List[str] = []

        if param.alphabet_max_length > 0:
            generated_name += random.choices(
                string.ascii_letters, k=param.alphabet_max_length
            )

        if param.number_max_length > 0:
            generated_name += random.choices(string.digits, k=param.number_max_length)

        if param.symbol_max_length > 0:
            generated_name += random.choices("_.", k=param.symbol_max_length)

        random.shuffle(generated_name)

        ret = "".join(generated_name)

        if param.use_leet:
            ret = _text_convert_to_leet(ret)

        self.logger.info(f"generate exit:{ret}")

        return ret


class FakerBasedAccountNameGenerator:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def generate(self, param: FakerBasedGeneratorParam) -> str:
        self.logger.info(param.locale)

        fake = Faker(param.locale.value)

        self.logger.info(fake.locales)

        name = fake.ascii_email().split("@")[0]

        if param.use_leet:
            name = _text_convert_to_leet(name)

        name = name.replace(" ", ".")

        return name


def _text_convert_to_leet(text: str):
    table = str.maketrans(
        {
            "A": "4",
            "a": "4",
            "E": "3",
            "e": "3",
            "G": "6",
            "g": "6",
            "I": "1",
            "i": "1",
            "L": "1",
            "l": "1",
            "O": "0",
            "o": "0",
            "P": "9",
            "p": "9",
            "S": "5",
            "s": "5",
            "T": "7",
            "t": "7",
            "Z": "2",
            "z": "2",
        }
    )

    return text.translate(table)
